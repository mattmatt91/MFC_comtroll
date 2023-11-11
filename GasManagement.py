import json
from valve_mock import MockValves as Valve
from mfc_mock import MockMFC as MFC

class GasManagement:
    def __init__(self, config_file):
        self.devices = {'valves': {}, 'mfcs': {}}
        self.load_config(config_file)

    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            config = json.load(file)
            self.init_valves(config["valves"])
            self.init_mfcs(config.get('mfcs', []))

    def init_valves(self, valve_config):
        self.devices['valves']= Valve(valve_config)

    def init_mfcs(self, mfc_config):
        # Create MFC instances
        for mfc_info in mfc_config:
            name = mfc_info.get('name')
            ip = mfc_info.get('ip')
            port = mfc_info.get('port')
            max_flow = mfc_info.get('max_flow')
            self.devices['mfcs'][name] = MFC(ip, port, max_flow)

    def get_device(self, device_type, name):
        # Get a specific device by type and name
        return self.devices.get(device_type, {}).get(name, None)

    def get_device_states(self):
        # Returns a dict with states and other properties of all devices
        states = {'valves': {}, 'mfcs': {}}
        valve = self.devices['valves']
        states['valves'] = valve.get_states()  # Assuming Valve class has a get_state method
        print(self.devices['valves'])
        for name, mfc in self.devices['mfcs'].items():
            states['mfcs'][name] = mfc.get_data()  # Assuming MFC class has a get_state method
        return states

    def set_valve_states(self, valve_states):
        # Sets the state of the valves
        for valve_info in valve_states:
            for name, state in valve_info.items():
                if name in self.devices['valves']:
                    self.devices['valves'][name].set_state(state)  # Assuming Valve class has a set_state method
        return "Operation successful for valves."

    def set_mfc_states(self, mfc_states):
        # Sets the state of the MFCs
        for mfc_info in mfc_states:
            for name, state in mfc_info.items():
                if name in self.devices['mfcs']:
                    self.devices['mfcs'][name].set_state(state)  # Assuming MFC class has a set_state method
        return "Operation successful for MFCs."

    def close_devices(self):
        # Closes all devices
        for valve in self.devices['valves'].values():
            valve.close()  # Assuming Valve class has a close method
        for mfc in self.devices['mfcs'].values():
            mfc.close()  # Assuming MFC class has a close method
        return "All devices closed."
    
def calculate_flow_rates(desired_concentrations, max_flows):
    # Constants
    F_total = 200  # Total flow rate in sccm
    C_test1, C_test2, C_test3 = 10000, 10000, 10000  # Concentrations of test gases in ppm

    # Desired concentrations
    C_desired1 = desired_concentrations.get("test_gas_1", 0)
    C_desired2 = desired_concentrations.get("test_gas_2", 0)
    C_desired3 = desired_concentrations.get("test_gas_3", 0)

    # Calculating flow rates for each test gas
    F_test1 = (C_desired1 * F_total) / C_test1
    F_test2 = (C_desired2 * F_total) / C_test2
    F_test3 = (C_desired3 * F_total) / C_test3

    # Calculating flow rates for wet air
    F_wet = F_total / 4

    # Calculating flow rate for dry air
    F_dry = F_total - (F_test1 + F_test2 + F_test3 + F_wet)

    # Check if the mixture is possible
    if F_dry < 0 or F_dry > max_flows["dry_air"]:
        return "Mixture not possible: Dry air flow out of range."

    if F_wet > max_flows["wet_air"]:
        return "Mixture not possible: Wet air flow out of range."

    if F_test1 > max_flows["test_gas_1"] or F_test2 > max_flows["test_gas_2"] or F_test3 > max_flows["test_gas_3"]:
        return "Mixture not possible: Test gas flow out of range."

    # Return flow rates in a dictionary
    return {
        "dry_air": F_dry,
        "wet_air": F_wet,
        "test_gas_1": F_test1,
        "test_gas_2": F_test2,
        "test_gas_3": F_test3
    }

# Example usage
# desired_concentrations = {
#     "test_gas_1": 500,  # Desired concentration for test gas 1 in ppm
#     "test_gas_2": 300,  # Desired concentration for test gas 2 in ppm
#     "test_gas_3": 200   # Desired concentration for test gas 3 in ppm
# }
# 
# max_flows = {
#     "dry_air": 4000,    # Max flow for dry air in sccm
#     "wet_air": 4000,    # Max flow for wet air in sccm
#     "test_gas_1": 20,   # Max flow for test gas 1 in sccm
#     "test_gas_2": 20,   # Max flow for test gas 2 in sccm
#     "test_gas_3": 20    # Max flow for test gas 3 in sccm
# }

if __name__ == "__main__":
    gas_management = GasManagement('config.json')
    print(gas_management.get_device_states())
