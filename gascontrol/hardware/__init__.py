import os

# Use a more descriptive variable name
operating_mode = os.environ.get('OPERATING_SYSTEM', 'default')

# Avoid repeating the import statement
if operating_mode == 'mock':
    # Import mock classes
    from hardware.valve_mock import MockValves as Valves
    from hardware.mfc_mock import MockMFC as MFC
else:
    # Import real sensor classes
    from hardware.valve import Valves
    from hardware.mfc import MFC

# The script allows other modules to import Valves and MFC,
# which will be the correct version based on the operating_mode.
