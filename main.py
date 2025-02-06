from fastapi import FastAPI, Query, Header, Response
from typing import Annotated, Union
from pydantic import BaseModel
import asyncio

app = FastAPI()

@app.get("/sleep_time/")
async def sleep_time(sec: int):
    await asyncio.sleep(sec)
    return {"message": "I slept for {} seconds".format(sec)}