import json

def compute_cmd(cmds:dict, test_gas_conc:dict):
    cmds_valves = {
        "air_wet_a": True, # default opened
        "solid_a": False,
        "solid_b": False,
        "test_gas_1_a": False,
        "test_gas_2_a": False
    }
  

    routes_wash = [i for i in list(cmds["wash"].keys())if cmds["wash"][i]]
    routes_master_mix = [i for i in list(cmds["mix"].keys())]
    routes_master_mix = [route for route in routes_master_mix if route not in routes_wash]

    if "gas_1" in routes_master_mix:
        cmds_valves["test_gas_1_a"] = True
    if "gas_2" in routes_master_mix:
        cmds_valves["test_gas_2_a"] = True
    if "solid" in routes_master_mix:
        cmds_valves["solid_a"] = True
        cmds_valves["solid_b"] = True
    elif "solid" in routes_wash:
        cmds_valves["solid_a"] = True

    desired_concentrations = {
            "gas_1": cmds["mix"]["gas_1"],  # Desired concentration for test gas 1 in ppm
            "gas_2": cmds["mix"]["gas_2"],  # Desired concentration for test gas 2 in ppm
            "solid": cmds["mix"]["solid"]   # Desired concentration for test gas 3 in ppm
            }
    portion_wet = cmds["portion_wet"]
    flow_wash = cmds["flow_wash"]
    total_flow = cmds["total_flow"]
    sccm_flowrates = calculate_flow_rates(desired_concentrations, total_flow, portion_wet, test_gas_conc)
    
    cmds_mfc = [{key: value} for key, value in sccm_flowrates.items()]
    return {"mfc": cmds_mfc, "valve":cmds_valves}
    

def calculate_flow_rates(desired_concentrations, F_total:int, portion_wet:float, test_gas_conc:dict):
    # Constants
    C_test1, C_test2, C_test3 = test_gas_conc["test_gas_1"], test_gas_conc["test_gas_2"], test_gas_conc["test_gas_solid"]  # Concentrations of test gases in ppm
    # Desired concentrations
    C_desired1 = desired_concentrations.get("gas_1", 0)
    C_desired2 = desired_concentrations.get("gas_2", 0)
    C_desired3 = desired_concentrations.get("solid", 0)

    # Calculating flow rates for each test gas
    F_test1 = (C_desired1 * F_total) / C_test1
    F_test2 = (C_desired2 * F_total) / C_test2
    F_test3 = (C_desired3 * F_total) / C_test3


    # Calculating flow rates for wet air
    F_wet = F_total * portion_wet

    if F_wet > F_total - F_test1 + F_test2 + F_test3:
        return "air_wet portion to big"

    # Calculating flow rate for dry air
    F_dry = F_total - (F_test1 + F_test2 + F_test3 + F_wet)

    print("flow total: ",F_total)
    print("flow dry: ",F_dry)
    print("flow wet: ",F_wet)
    print("F_test1", F_test1) 
    print("F_test2", F_test2) 
    print("F_test3", F_test3) 

    
    if F_test1 < 0 or F_test2 < 0 or F_test3 < 0 or F_dry < 0 or F_wet <0:
        return "Mixture not possible: Test gas flow must be bigger than 0."""

    # Return flow rates in a dictionary
    return {
        "dry_air": F_dry,
        "wet_air": F_wet,
        "gas_1": F_test1,
        "gas_2": F_test2,
        "solid": F_test3
    }

