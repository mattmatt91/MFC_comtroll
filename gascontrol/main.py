from fastapi import FastAPI
from hardware.GasManagement import GasManagement
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn")

# Initialize FastAPI app and GasManagement
app = FastAPI()
gas_management = GasManagement('config.json')

@app.get("/")
async def root():
    logger.info("Root endpoint called")
    """
    Root endpoint returning a simple JSON response.
    """
    return {'response': "alive"}

@app.get("/data")
async def get_data():
    """
    Endpoint to get device states.
    Returns the current state of the devices.
    """
    try:
        data = gas_management.get_device_states()
        return data
    except Exception as e:
        logger.error(f"Error in get_data: {e}")
        return {"error": str(e)}

@app.post("/exec_cmds")
async def set_cmds(cmds: dict):
    """
    Endpoint to execute commands on devices.
    Accepts a dictionary of commands and executes them.
    """
    try:
        gas_management.exec_cmds(cmds)
        return {"status": "Commands executed"}
    except Exception as e:
        logger.error(f"Error in set_cmds: {e}")
        return {"error": str(e)}
