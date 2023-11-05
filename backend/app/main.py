from fastapi import FastAPI
from datetime import timedelta

api = FastAPI()

@api.get("/home")
async def index():
    return {"messages": "Hello Welcome !!"}