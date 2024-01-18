from mfc import MFC
from valve import Valves
from time import sleep

if __name__ == "__main__":
    valve_config =  {
        "air_wet_a": 18,
        "solid_a": 23,
        "solid_b": 15,
        "test_gas_1_a": 24,
        "test_gas_2_a": 14
    }
    mfc_config = {
        "port": 502,
        "ip": "192.168.2.157",
        "max_flow": 20.0,
        "name": "test_gas_2"
    }

    mfc = MFC(host=mfc_config["ip"], port=mfc_config["port"], max_flow=mfc_config["max_flow"])
    my_valves = Valves(valve_config)
    
    while True:
            mfc.set_point(20)
            print(mfc.get_data())
            
            my_valves.operate_valve({"test_gas_2_a": True})

            
            sleep(5)
            
            my_valves.operate_valve({"test_gas_2_a": False})
            
            sleep(5)

    

