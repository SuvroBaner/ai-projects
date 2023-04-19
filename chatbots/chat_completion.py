import os

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the name of the cricket stadium in Bangalore ?"},
        {"role": "assistant", "content": "The cricket stadium in Bangalore is called M. Chinnaswamy Stadium."},
        {"role": "user", "content": "What is the nearest Metro station"}
    ]
)

print(completion.choices[0].message)