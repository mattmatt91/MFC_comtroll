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
if __name__ == "__main__":
    gas_management = GasManagement('config.json')
    print(gas_management.get_device_states())
