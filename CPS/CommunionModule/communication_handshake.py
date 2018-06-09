# coding=utf-8

import serial
import serial.tools.list_ports


class CommunicationHandShake:
    def __init__(self, sn=None):
        pass

    @classmethod
    def communication_hand_shake_with_arduino(cls):
        port_list = list(serial.tools.list_ports.comports())

        for port in port_list:
            port_info = list(port)
            # print(port_info)
            port_name = port_info[1]
            if "Arduino" in port_name:
                return True
            else:
                continue

        return False

    @classmethod
    def get_serial_port_info(cls):
        port_list = list(serial.tools.list_ports.comports())

        for port in port_list:
            port_info = list(port)
            port_name = port_info[1]
            if "Arduino" in port_name:
                return port_info

        return []

    @classmethod
    def get_serial_port_number(cls):
        serial_port_info = cls.get_serial_port_info()

        if serial_port_info is []:
            return ""

        return serial_port_info[0]
