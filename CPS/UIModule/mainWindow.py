# coding=utf8

########################################################################################################################
# 主窗口界面逻辑类文件：mainWindow
# 本文件所维护的类，用于实现mainWindow的界面交互逻辑，以及各个控件的功能
# 本类通过对主窗口界面设计类文件：mainWindow_ui文件的继承，并实现界面与逻辑代码的分离管理
# 最终，main函数通过对本类的调用，实例化出主窗口界面对象
########################################################################################################################

from PyQt5.QtCore import Qt
from UIModule.mainWindow_ui import Ui_MainWindow_ui
from UIModule.homeWindow.homeWindow import homeWindow
from UIModule.settingWindow.settingWindow import settingWindow
from UIModule.detectionWindow.detectionWindow import detectionWindow
from UIModule.analyzeWindow.analyzeWindow import analyzeWindow


class MainWindow(Ui_MainWindow_ui):
    # 界面启动时的初始化方法
    def __init__(self, parent=None):
        ########################################### 创建mianWindow(Start) ##############################################

        super(MainWindow, self).__init__(parent)        # 先执行父类初始化方法
        self.setWindowTitle("ChemistryPersonSoftware")  # 设置窗口标题
        self.setMinimumSize(1024, 768)                  # 设置最小尺寸
        self.setupUi(self)                              # 创建主界面mainWindow
        # self.showFullScreen()                           # 软件启动时，自动全屏
        ############################################ 创建mianWindow(End) ###############################################

        ########################################### 创建各个子窗口(Start) ##############################################

        self.homeWindow = homeWindow()          # 实例化homeWindow窗口对象（创建）
        self.set_sub_window(self.homeWindow)    # 将homeWindow设置到主窗口中
        self.homeWindow.show()                  # 将homeWindow设置为显示状态

        self.settingWindow = settingWindow()       # 实例化settingWindow窗口对象（创建）
        self.set_sub_window(self.settingWindow)    # 将settingWindow设置到主窗口中
        self.settingWindow.hide()                  # 将settingWindow设置为隐藏状态

        self.detectionWindow = detectionWindow()    # 实例化detectionWindow窗口对象（创建）
        self.set_sub_window(self.detectionWindow)   # 将detectionWindow设置到主窗口中
        self.detectionWindow.hide()                 # 将detectionWindow设置为隐藏状态

        self.analyzeWindow = analyzeWindow()        # 实例化detectionWindow窗口对象（创建）
        self.set_sub_window(self.analyzeWindow)     # 将detectionWindow设置到主窗口中
        self.analyzeWindow.hide()                   # 将detectionWindow设置为显示状态
        ############################################ 创建各个子窗口(End) ###############################################

        ######################################## 所有信号与槽的连接(Start) #############################################

        # 主界面的界面切换按钮
        self.homeWindow.btn_setting.clicked.connect(self.on_btn_setting_clicked)
        self.homeWindow.btn_detection.clicked.connect(self.on_btn_detection_clicked)
        self.homeWindow.btn_analyze.clicked.connect(self.on_btn_analyze_clicked)

        # 设置界面的界面切换按钮
        self.settingWindow.btn_comeback_homeWindow.clicked.connect(self.on_btn_comeback_homeWindow_clicked)
        self.settingWindow.btn_ready_to_detection.clicked.connect(self.on_btn_ready_to_detection_clicked)

        # 检测界面的界面切换按钮
        self.detectionWindow.btn_comeback_homeWindow.clicked.connect(self.on_btn_comeback_homeWindow_clicked)
        self.detectionWindow.btn_comeback_settingWindow.clicked.connect(self.on_btn_comeback_settingWindow_clicked)
        self.detectionWindow.btn_go_to_analyzeWindow.clicked.connect(self.on_btn_go_to_analyzeWindow_clicked)

        # 分析界面的界面切换按钮
        self.analyzeWindow.btn_comeback_homeWindow.clicked.connect(self.on_btn_comeback_homeWindow_clicked)
        self.analyzeWindow.btn_comeback_detectionWindow.clicked.connect(self.on_btn_comeback_detectionWindow_clicked)
        ######################################## 所有信号与槽的连接(Start) #############################################

    # 将参数传递的对象设置到主窗口中
    def set_sub_window(self, subWindow):
        subWindow.setParent(self.subWindow_container, Qt.Widget)        # 将参数传递的对象设置到主窗口中
        self.gridLayout_in_subWindow.addWidget(subWindow, 0, 0, 1, 1)   # 将参数传来的子窗口，放入布局器中

    # 点击“设置”按钮的时候，隐藏homeWindow，显示“设置”界面
    def on_btn_setting_clicked(self):
        self.homeWindow.hide()
        self.settingWindow.show()

    # 点击“检测”按钮的时候，隐藏homeWindow，显示“检测”界面
    def on_btn_detection_clicked(self):
        self.homeWindow.hide()
        self.detectionWindow.show()

    # 点击“分析”按钮的时候，隐藏homeWindow，显示“分析”界面
    def on_btn_analyze_clicked(self):
        self.homeWindow.hide()
        self.analyzeWindow.show()

    # 点击“返回主界面”按钮的时候，隐藏所有其他界面，显示主界面
    def on_btn_comeback_homeWindow_clicked(self):
        self.settingWindow.hide()
        self.detectionWindow.hide()
        self.analyzeWindow.hide()
        self.homeWindow.show()

    # 点击“返回主界面”按钮的时候，隐藏所有其他界面，显示检测界面
    def on_btn_ready_to_detection_clicked(self):
        self.settingWindow.hide()
        self.detectionWindow.show()

    # 点击“返回设置界面”按钮的时候，隐藏所有其他界面，显示设置界面
    def on_btn_comeback_settingWindow_clicked(self):
        self.detectionWindow.hide()
        self.settingWindow.show()

    # 点击“前往分析”按钮的时候，隐藏所有其他界面，显示分析界面
    def on_btn_go_to_analyzeWindow_clicked(self):
        self.detectionWindow.hide()
        self.analyzeWindow.show()

    # 点击“返回检测界面”按钮的时候，隐藏所有其他界面，显示检测界面
    def on_btn_comeback_detectionWindow_clicked(self):
        self.analyzeWindow.hide()
        self.detectionWindow.show()

    # 键盘响应事件
    def keyPressEvent(self, event):
        # 方向键：上
        if event.key() == Qt.Key_Up:
            print("1" * 20)

        # 方向键：下
        if event.key() == Qt.Key_Down:
            print("2" * 20)

        # 方向键：左
        if event.key() == Qt.Key_Left:
            print("3" * 20)

        # 方向键：右
        if event.key() == Qt.Key_Right:
            print("4" * 20)