import requests
import json

def post_test_data(url, data):
    response = requests.post(url, json=data)
    return response


def get_test_data(url):
    response = requests.get(url)
    return response


example_cmd = {
    "wash": {
        "gas_1": False,
        "gas_2": True,
        "solid": False
    },

    "mix": {"gas_1": 1, # ppm
            "gas_2": 0,
            "solid": 110},

    "total_flow": 800, # sccm 
    "portion_wet": 0.9,
    "flow_wash": 20,


}

def flatten_mfc_valve_data(data):
    # Initialize a new dictionary to hold the flattened data
    flattened_data = {"points":{}, "valves":{}}
    
    # Extract and add MFC flow information
    for mfc, details in data.get("mfcs", {}).items():
        # Use the MFC name with a suffix to denote the flow
        flattened_data["points"][f"{mfc}_point"] = details.get("point", 0)
    
    # Add valve states directly
    for valve, state in data.get("valves", {}).items():
        # Use the valve name directly
        flattened_data["valves"][valve] = state
    
    return flattened_data

if __name__ == "__main__":
    # URL for POST request
    host_url = "http://172.17.0.2:9000"

    if 1:
        post_url = f'{host_url}/'
        print(post_url)
        post_response = post_test_data(host_url, example_cmd)
        print("POST Request Response:", post_response.status_code, post_response.json())
        
    if 1:
        # URL for GET request
        get_url = f'{host_url}/data'
        get_response = get_test_data(get_url)
        print(json.dumps(flatten_mfc_valve_data(get_response.json()), indent=4, sort_keys=True))

