import os

# Read the environment variable
operating_mode = os.environ.get('operating_system', 'default')

if operating_mode == 'mock':
    # Import mock classes
    from hardware.valve_mock import MockValves as Valves
    from hardware.mfc_mock import MockMFC as MFC
else:
    # Import real sensor classes
    from hardware.valve import Valves as Valves
    from hardware.mfc import MFC as MFC

# Now, other modules can simply import Sensor from this package,
# and they'll get the correct version based on the environment variable.
