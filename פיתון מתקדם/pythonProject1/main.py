from fastapi import FastAPI
from pydantic import BaseModel, constr

app = FastAPI()

class Task(BaseModel):
    id :int
    name: constr(min_length=2,max_length=20)
    description: str
    time:int

@app.post('/')
async def creat_task(task:Task):
    return "creat succedd"

