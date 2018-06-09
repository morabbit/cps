# coding=utf8

import serial
import serial.tools.list_ports
from CommunionModule.communication_handshake import CommunicationHandShake


class ReceiveMessageToArduino:
    def __init__(self):
        self.__port = CommunicationHandShake.get_serial_port_number()

    # 读取串口消息
    def receive_message_to_arduino(self, mode="byte", byte_len=1):
        # 打开端口
        serial_port = serial.Serial(port=self.__port,
                                    baudrate=9600,
                                    bytesize=8,
                                    parity='E',
                                    stopbits=1,
                                    timeout=2)

        # 读取端口
        if mode == 'byte':
            message = serial_port.read(byte_len)
        elif mode == 'line':
            message = serial_port.readline()

        # 关闭串口
        serial_port.close()

        return message

    # 转成16进制的函数
    def convert_hex(self, string):
        res = []
        result = []
        for item in string:
            res.append(item)
        for i in res:
            result.append(hex(i))
        return result