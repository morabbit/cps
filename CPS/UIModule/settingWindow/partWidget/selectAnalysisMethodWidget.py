# coding=utf8

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from UIModule.settingWindow.partWidget.selectAnalysisMethodWidget_ui import Ui_selectAnalysisMethodWidget


class selectAnalysisMethodWidget(Ui_selectAnalysisMethodWidget, QWidget):
    def __init__(self, parent=None):
        # 调用父类初始化
        super(selectAnalysisMethodWidget, self).__init__(parent)

        # 创建界面
        self.setupUi(self)

    def set_sub_window(self, subWindow):
        subWindow.setParent(self.widget_for_sub_window, Qt.Widget)        # 将参数传递的对象设置到主窗口中
        self.gridLayoutWidget.addWidget(subWindow, 0, 0, 1, 1)            # 将参数传来的子窗口，放入布局器中