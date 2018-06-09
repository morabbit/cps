# coding=utf8

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from UIModule.detectionWindow.detectionWindow_ui import Ui_detectionWindow
from CommunionModule.send_message_to_arduino import SendMessageToArduino


class detectionWindow(Ui_detectionWindow, QWidget):
    def __init__(self, parent=None):
        # 调用父类初始化
        super(detectionWindow, self).__init__(parent)

        # 创建界面
        self.setupUi(self)

    # 键盘响应事件
    def keyPressEvent(self, event):
        # 方向键：上
        if event.key() == Qt.Key_Up:
            message = SendMessageToArduino(b'U')
            message.send_message_to_arduino()

        # 方向键：下
        if event.key() == Qt.Key_Down:
            message = SendMessageToArduino(b'D')
            message.send_message_to_arduino()

        # 方向键：左
        if event.key() == Qt.Key_Left:
            message = SendMessageToArduino(b'L')
            message.send_message_to_arduino()

        # 方向键：右
        if event.key() == Qt.Key_Right:
            message = SendMessageToArduino(b'R')
            message.send_message_to_arduino()
