import json
from hardware import MFC
from hardware import Valves
import hardware.calculator as ca


class GasManagement:
    def __init__(self, config_file):
        self.devices = {'valves': {}, 'mfcs': {}}
        self.load_config(config_file)

    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            self.config = json.load(file)
            self.init_valves(self.config["valves"])
            self.init_mfcs(self.config.get('mfcs', []))

    def init_valves(self, valve_config):
        self.devices['valves'] = Valves(valve_config)

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
        # Assuming Valve class has a get_state method
        states['valves'] = valve.get_states()
        for name, mfc in self.devices['mfcs'].items():
            # Assuming MFC class has a get_state method
            states['mfcs'][name] = mfc.get_data()
        return states

    def exec_cmds(self, cmds:dict):
        
        computed_cmds = ca.compute_cmd(cmds, self.config["test_gases"])
        cmds_mfcs = computed_cmds["mfc"]
        cmds_valves = computed_cmds["valve"]
        
        self.set_mfc_states(cmds_mfcs)
        self.set_valve_states(cmds_valves)

    def set_valve_states(self, valve_states):
        self.devices['valves'].operate_valve(valve_states)
        return "Operation successful for valves."

    def set_mfc_states(self, mfc_states):
        for mfc_info in mfc_states:
            for name, point in mfc_info.items():
                if name in self.devices['mfcs']:
                    # Assuming MFC class has a set_state method
                    self.devices['mfcs'][name].set_point(point)
        return "Operation successful for MFCs."

    def close_devices(self):
        # Closes all devices
        self.devices['valves'].close() 
        for mfc in self.devices['mfcs'].values():
            mfc.close()  # Assuming MFC class has a close method
        return "All devices closed."



