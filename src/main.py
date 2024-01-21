from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def hello(name: str):
  return {'Hello ' + name + '!'} 
