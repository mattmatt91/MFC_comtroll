



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
desired_concentrations = {
    "test_gas_1": 500,  # Desired concentration for test gas 1 in ppm
    "test_gas_2": 300,  # Desired concentration for test gas 2 in ppm
    "test_gas_3": 200   # Desired concentration for test gas 3 in ppm
}

max_flows = {
    "dry_air": 4000,    # Max flow for dry air in sccm
    "wet_air": 4000,    # Max flow for wet air in sccm
    "test_gas_1": 20,   # Max flow for test gas 1 in sccm
    "test_gas_2": 20,   # Max flow for test gas 2 in sccm
    "test_gas_3": 20    # Max flow for test gas 3 in sccm
}