from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from hardware.GasManagement import GasManagement
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn")

# Initialize FastAPI app 
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Specify the React app's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# init and GasManagement
gas_management = GasManagement('config.json')


@app.get("/data")
async def get_data():
    data = gas_management.get_device_states()
    return data
 

@app.post("/")
async def set_cmds(cmds: dict):
    logger.info("exec cmds")
    gas_management.exec_cmds(cmds)
    return {"status": "Commands executed"}
   




