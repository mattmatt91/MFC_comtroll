from fastapi import FastAPI, Depends
from pydantic import BaseModel
import json
from typing import List
from hardware.mfc import MFC


class MFCConfig(BaseModel):
    port: int
    ip: str
    max_flow: float
    name: str

app = FastAPI()
mfc_list: List[MFC] = []

def open_devices():
    pass

@app.on_event("startup")
async def startup_event():
    get_mfcs()

@app.get("/mfcs")
async def read_mfcs(mfcs: List[MFC] = Depends(get_mfcs)):
    return mfcs


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
