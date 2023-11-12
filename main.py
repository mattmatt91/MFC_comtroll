from fastapi import FastAPI
from hardware.GasManagement import GasManagement




gas_management = GasManagement('config.json')
app = FastAPI()


def open_devices():
    pass

@app.on_event("startup")
async def startup_event():
    # print(gas_management.get_device_states()["mfcs"])
    pass

@app.get("/data")
async def get_data():
    data = gas_management.get_device_states()
    print(data)
    return data

@app.post("/exec_cmds")
async def set_cmds(cmds:dict):
    gas_management.exec_cmds(cmds)



