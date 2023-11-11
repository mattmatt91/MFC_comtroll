from hardware.GasManagement import GasManagement


if __name__ == "__main__":
    gas_management = GasManagement('config.json')
    print(gas_management.get_device_states()["mfcs"])
    valve_states = [
            {"air_wet_a": True},
            {"solid_a": False},
            {"solid_b": False},
            {"test_gas_1_a": True},
            {"test_gas_2_a": False}
            ]
    mfc_points = [
            {"test_gas_1": 20},
            {"test_gas_2": 10},
            {"air_dry": 200},
            {"air_wet": 200}
            ]
    print(gas_management.set_valve_states(valve_states))
    print(gas_management.set_mfc_states(mfc_points))
    print(gas_management.get_device_states()["mfcs"])
    gas_management.close_devices() 
