"""
    This code implements a -
    Python app, that records your voice and also transcribes it instantly using the OpenAI Whisper API
"""

'''
    If you are running it on Macbook with Apple M1 chip, you need to do the following to install 'pyaudio' module
    https://medium.com/@wagnernoise/installing-pyaudio-on-macos-9a5557176c4d
    1. Install Homebrew : https://brew.sh/
    2. brew install portaudio
    3. pip3 install pyaudio
'''

import openai
import os
import pyaudio
import wave
import threading
import sys
import queue

'''
    Recording will be handled in a separate thread
    Storing audio data will be done in a queue.
'''

openai.api_key = os.environ["OPENAI_API_KEY"]

def record_audio(filename, stop_event, audio_queue):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024

    audio = pyaudio.PyAudio()
    stream = audio.open(format = FORMAT,
                        channels = CHANNELS,
                        rate = RATE,
                        input = True,
                        frames_per_buffer = CHUNK)

    print('Recording ... Press return key to stop.')

    while not stop_event.is_set():
        data = stream.read(CHUNK)
        audio_queue.put(data)

    print("Finished Recording")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filename, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(list(audio_queue.queue)))

def transcribe_audio(filename):
    with open(filename, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript["text"]

def main():
    audio_filename = "your_recorded_audio.wav"
    stop_event = threading.Event()
    audio_queue = queue.Queue()

    record_thread = threading.Thread(target = record_audio, args = (audio_filename, stop_event, audio_queue))
    record_thread.start()

    input("Press the return key to stop recording ... \n")
    stop_event.set()
    record_thread.join() # we wait for the recording thread to finish
    
    transcription = transcribe_audio(audio_filename)
    print("Transcription: ", transcription)

if __name__ == '__main__':
    main()