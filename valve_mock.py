class MockValves:
    def __init__(self, valve_config:dict):
 
        # valve_config is a dict with valve names and corresponding mock pin numbers
        self.valves = valve_config
        self.valve_states = {valve: False for valve in self.valves}  # False indicates closed

    def operate_valve(self, valve_operations):
        # valve_operations is a list of dicts, each dict contains valve name and a Boolean
        for operation in valve_operations:
                print(operation)
                valve,state = operation.popitem()
                print(state, valve)
                if valve in self.valves:
                    self.valve_states[valve] = state
                else:
                    print(f"Valve '{valve}' not found.")

    def get_states(self):
        return self.valve_states

if __name__ == "__main__":
    # Example usage
    valve_config = {"valve_1": 1, "valve_2": 2, "valve_3": 3}  # Mock pin numbers
    mock_valves = MockValves(valve_config)

    # Operate valves
    mock_valves.operate_valve([{"valve_1": True}, {"valve_2": False}])

    # Get current states
    print(mock_valves.get_valve_states())
