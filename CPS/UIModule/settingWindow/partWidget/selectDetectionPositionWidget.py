# coding=utf8

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from UIModule.sampleMapWidget.sampleStageWidget import sampleStageWidget
from UIModule.settingWindow.partWidget.selectDetectionPositionWidget_ui import Ui_selectDetectionPositionWidget


class selectDetectionPositionWidget(Ui_selectDetectionPositionWidget, QWidget):
    def __init__(self, parent=None):
        # 调用父类初始化
        super(selectDetectionPositionWidget, self).__init__(parent)

        # 创建界面
        self.setupUi(self)

        self.sampleStageWidget = sampleStageWidget()    # 实例化样品台界面对象（创建）
        self.set_sub_window(self.sampleStageWidget)     # 将样品台界面设置到设定窗口中
        self.sampleStageWidget.show()                   # 将样品台界面设置为显示状态

    def set_sub_window(self, subWindow):
        subWindow.setParent(self.widget_for_samples, Qt.Widget)                 # 将参数传递的对象设置到主窗口中
        self.gridLayout_for_samples.addWidget(subWindow, 0, 0, 1, 1)            # 将参数传来的子窗口，放入布局器中
