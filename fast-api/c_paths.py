from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    gpt = 'OpenAI GPT'
    bert = 'Google BERT'

@app.get("/")
async def root():
    return {'message': 'Hello World'}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {'item_id': item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.gpt:
        return {'model_name': model_name, "message": 'It is a transformer decoder based model by OpenAI'}
    if model_name.value == 'Google BERT':
        return {'model_name': model_name, "message": 'It is a transformer encoder based model by Google'}
    return {'model_name': model_name, "message": 'we do not support that'}