# coding=utf8

import serial
import serial.tools.list_ports
from CommunionModule.communication_handshake import CommunicationHandShake


class SendMessageToArduino:
    def __init__(self, message):
        self.__message = message
        self.__port = CommunicationHandShake.get_serial_port_number()

    # 发送消息
    def send_message_to_arduino(self):
        # 打开端口
        serial_port = serial.Serial(port=self.__port,
                                    baudrate=9600,
                                    bytesize=8,
                                    parity='E',
                                    stopbits=1,
                                    timeout=2)

        # 发送命令
        serial_port.write(self.__message)

        # 关闭串口
        serial_port.close()
