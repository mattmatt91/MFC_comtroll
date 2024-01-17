
from pyModbusTCP.client import ModbusClient  # Modbus TCP Client
import struct
import os
import time


def ints_to_float(arr):
    try:
        a = arr[0].to_bytes(2, "big")
        b = arr[1].to_bytes(2, "big")
        arr = a+b
        aa = bytearray(arr)
        return (struct.unpack('>f', aa)[0])
    except:
        return None


def ints_to_long(arr):
    a = arr[0].to_bytes(2, "big")
    b = arr[1].to_bytes(2, "big")
    arr = a+b
    aa = bytearray(arr)
    return (struct.unpack('>l', aa)[0])


def float_to_ints(flo):
    arr = struct.pack('>f', flo)
    a = arr[:2]
    b = arr[2:]
    int_a = int.from_bytes(a, "big")
    int_b = int.from_bytes(b, "big")
    return [int_a, int_b]


class MFC():
    def __init__(self, host, port, max_flow):
        self.bus = ModbusClient(host=host, port=port, auto_open=True)
        time.sleep(0.2)
        self.bus.open()
        self.max_flow = max_flow
        print("init")
        # self.open_valve(False)
        # self.close_valve(True)
        self.reset()

    def open_valve(self, state):
        self.bus.write_single_coil(int('0xE001', 16), state)

    def close_valve(self, state):
        self.bus.write_single_coil(int('0xE002', 16), state)

    def valve_state(self):
        return self.bus.read_coils(int('0xE001', 16), bit_nb=1)

    def reset(self):
        self.bus.write_single_coil(int('0xE000', 16), '0xFF00h')
        time.sleep(1)
        self.bus.write_single_coil(int('0xE000', 16), '0x0000')

    def zero_flow(self):
        self.bus.write_single_coil(int('0xE003', 16), '0xFF00h')

    def get_temp(self):
        response = self.bus.read_input_registers(int('0x4002', 16), 2)
        return ints_to_float(response)

    def get_flow_total(self):
        response = self.bus.read_input_registers(int('0x400A', 16), 2)
        return ints_to_long(response)

    def get_flow(self):
        response = self.bus.read_input_registers(int('0x4000', 16), 2)
        # print('flow response raw: ', response)
        # print('flow response float: ', ints_to_float(response))
        return ints_to_float(response)

    def get_valve_pos(self):
        response = self.bus.read_input_registers(int('0x4004', 16), 2)
        return ints_to_float(response)

    def get_point(self):
        response = self.bus.read_holding_registers(int('0xA000', 16), 2)
        # print('point response raw: ', response)
        # print('point response float: ', ints_to_float(response))
        return ints_to_float(response)

    def set_point(self, flow):
        if flow > self.max_flow:
            raise ValueError("flow can't be bigger than max_flow")
        data = float_to_ints(flow)
        # print(data)
        self.bus.write_multiple_registers(int('0xA000', 16), data)

    def get_data(self):
        try:
            temp = self.get_temp()
            flow = self.get_flow()
            flow_total = self.get_flow_total()
            valve_state = self.valve_state()
            point = self.get_point()
            valve_pos = self.get_valve_pos()
            data = {'temp': temp, 'flow': flow, 'flow_total': flow_total,
                    'valve_state': valve_state, 'point': point, 'valve_pos': valve_pos}
            return data
        except Exception as e:
            print(f'Error reading mfc: {e}, returning empty dict')
            return {}

    def close(self):
        self.close_valve(True)
        self.open_valve(False)
        self.bus.close()


if __name__ == "__main__":
    mfc_config = {
        "port": 502,
        "ip": "192.168.2.141",
        "max_flow": 1000.0,
        "name": "air_dry"
    }
    mfc = MFC(host=mfc_config["ip"], port=mfc_config["port"], max_flow=mfc_config["max_flow"])
    print(mfc.get_data())
