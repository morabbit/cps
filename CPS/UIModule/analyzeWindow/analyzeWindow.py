# coding=utf8

from PyQt5.QtWidgets import QWidget
from UIModule.analyzeWindow.analyzeWindow_ui import Ui_analyzeWindow


class analyzeWindow(Ui_analyzeWindow, QWidget):
    def __init__(self, parent=None):
        # 调用父类初始化
        super(analyzeWindow, self).__init__(parent)

        # 创建界面
        self.setupUi(self)
