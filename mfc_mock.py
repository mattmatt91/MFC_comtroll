class MockMFC:
    def __init__(self, host, port, max_flow):
        self.max_flow = max_flow
        self.valve_open = False
        self.valve_closed = True
        self.reset()

    def open_valve(self, state):
        self.valve_open = state

    def close_valve(self, state):
        self.valve_closed = state

    def valve_state(self):
        return self.valve_open

    def reset(self):
        self.flow = 0
        self.flow_total = 0
        self.temp = 25.0  # Default temperature
        self.valve_pos = 0
        self.point = 0

    def zero_flow(self):
        self.flow = 0

    def get_temp(self):
        return self.temp

    def get_flow_total(self):
        return self.flow_total

    def get_flow(self):
        return self.flow

    def get_valve_pos(self):
        return self.valve_pos

    def get_point(self):
        return self.point

    def set_point(self, flow):
        if flow > self.max_flow:
            raise ValueError("Flow can't be bigger than max_flow")
        self.point = flow

    def get_data(self):
        try:
            data = {'temp': self.get_temp(), 'flow': self.get_flow(), 'flow_total': self.get_flow_total(), 
                    'valve_state': self.valve_state(), 'point': self.get_point(), 'valve_pos': self.get_valve_pos()}
            return data
        except Exception as e:
            print(f'Error in mock MFC: {e}, returning empty dict')
            return {}

    def close(self):
        self.close_valve(True)
        self.open_valve(False)
