import requests


def post_test_data(url, data):
    response = requests.post(url, json=data)
    return response


def get_test_data(url):
    response = requests.get(url)
    return response


example_cmd = {
    "wash": {
        "gas_1": True,
        "gas_2": True,
        "solid": False
    },

    "mix": {"gas_1": 100, # ppm
            "gas_2": 100,
            "solid": 0},

    "total_flow": 200, # sccm
    "portion_wet": 0.9,
    "flow_wash": 20,


}

# URL for POST request
post_url = 'http://localhost:9000/exec_cmds'
post_response = post_test_data(post_url, example_cmd)
print("POST Request Response:", post_response.status_code, post_response.json())

# URL for GET request
get_url = 'http://localhost:9000/data'
get_response = get_test_data(get_url)
print("GET Request Response:", get_response.status_code, get_response.json())
