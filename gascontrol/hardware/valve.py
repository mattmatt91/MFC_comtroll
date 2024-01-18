import RPi.GPIO as GPIO

class Valves:
    def __init__(self, valve_config):
        # valve_config is a dict with valve names and corresponding GPIO pin numbers
        self.valves = valve_config
        self.valve_states = {valve: False for valve in self.valves}  # False indicates closed

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # Setup all valves as output and initialize them to closed (False)
        for pin in self.valves.values():
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)

    def operate_valve(self, valve_operations):
        # valve_operations is a list of dicts, each dict contains valve name and a Boolean
        for valve in valve_operations:
           
            if valve in self.valves:
                GPIO.output(self.valves[valve], GPIO.LOW if valve_operations[valve] else GPIO.HIGH)
                self.valve_states[valve] = valve_operations[valve]
            else:
                print(f"Valve '{valve}' not found.")

    def get_states(self):
        return self.valve_states
if __name__ == "__main__":
    # Example usage
    valve_config =  {
        "air_wet_a": 18,
        "solid_a": 23,
        "solid_b": 15,
        "test_gas_1_a": 24,
        "test_gas_2_a": 14
    }
    my_valves = Valves(valve_config)

    # Operate valves
    my_valves.operate_valve([{"air_wet_a": True}, {"solid_a": False}])

    # Get current states
    print(my_valves.get_states())
