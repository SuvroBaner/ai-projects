import os

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

def callOpenAI(animal):
    response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = generate_prompt(animal),
            temperature = 0.8,        
        )
    result = response.choices[0].text
    return result

def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.
Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(animal)

if __name__ == '__main__':
    animal = input("Which animal do you want to name: ")
    print(callOpenAI(animal))