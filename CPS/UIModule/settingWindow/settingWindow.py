# coding=utf8

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from UIModule.settingWindow.settingWindow_ui import Ui_settingWindow
from UIModule.settingWindow.partWidget.welcomeWidget import welcomeWidget
from UIModule.settingWindow.partWidget.selectDetectionPositionWidget import selectDetectionPositionWidget
from UIModule.settingWindow.partWidget.selectExperimentMethodWidget import selectExperimentMethodWidget
from UIModule.settingWindow.partWidget.selectAnalysisMethodWidget import selectAnalysisMethodWidget


class settingWindow(Ui_settingWindow, QWidget):
    def __init__(self, parent=None):
        # 调用父类初始化
        super(settingWindow, self).__init__(parent)

        # 创建界面
        self.setupUi(self)

        #################################### 将所有的子界面导入并隐藏（Start）##########################################

        self.welcomeWidget = welcomeWidget()                                    # 实例化欢迎界面对象（创建）
        self.set_sub_window(self.welcomeWidget)                                 # 将欢迎界面设置到设定窗口中
        self.welcomeWidget.show()                                               # 将欢迎界面设置为显示状态

        self.selectDetectionPositionWidget = selectDetectionPositionWidget()    # 实例化定位界面对象（创建）
        self.set_sub_window(self.selectDetectionPositionWidget)                 # 将定位界面设置到设定窗口中
        self.selectDetectionPositionWidget.hide()                               # 将定位界面设置为隐藏状态

        self.selectExperimentMethodWidget = selectExperimentMethodWidget()      # 实例化实验界面对象（创建）
        self.set_sub_window(self.selectExperimentMethodWidget)                  # 将实验界面设置到设定窗口中
        self.selectExperimentMethodWidget.hide()                                # 将实验界面设置为隐藏状态

        self.selectAnalysisMethodWidget = selectAnalysisMethodWidget()          # 实例化分析界面对象（创建）
        self.set_sub_window(self.selectAnalysisMethodWidget)                    # 将分析界面设置到设定窗口中
        self.selectAnalysisMethodWidget.hide()                                  # 将分析界面设置为隐藏状态
        ##################################### 将所有的子界面导入并隐藏（End）###########################################


        ######################################## 所有信号与槽的连接(Start) #############################################

        self.btn_select_position.clicked.connect(self.on_btn_select_position_clicked)
        self.btn_select_experiment.clicked.connect(self.on_btn_select_experiment_clicked)
        self.btn_select_analyze.clicked.connect(self.on_btn_select_analyze_clicked)
        ######################################## 所有信号与槽的连接(Start) #############################################

    # 设置子窗口界面
    def set_sub_window(self, subWindow):
        subWindow.setParent(self.widget_for_sub_window, Qt.Widget)        # 将参数传递的对象设置到主窗口中
        self.gridLayout.addWidget(subWindow, 0, 0, 1, 1)                  # 将参数传来的子窗口，放入布局器中

    # "选择检测位置"按钮操函数
    def on_btn_select_position_clicked(self):
        self.welcomeWidget.hide()
        self.selectExperimentMethodWidget.hide()
        self.selectAnalysisMethodWidget.hide()
        self.selectDetectionPositionWidget.show()

        # "选择实验方法"按钮操函数
    def on_btn_select_experiment_clicked(self):
        self.welcomeWidget.hide()
        self.selectDetectionPositionWidget.hide()
        self.selectAnalysisMethodWidget.hide()
        self.selectExperimentMethodWidget.show()

        # "选择分析方法"按钮操函数
    def on_btn_select_analyze_clicked(self):
        self.welcomeWidget.hide()
        self.selectDetectionPositionWidget.hide()
        self.selectExperimentMethodWidget.hide()
        self.selectAnalysisMethodWidget.show()
