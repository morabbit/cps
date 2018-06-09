# coding=utf8

########################################################################################################################
# 主界面逻辑类文件：homeWindow
# 本文件所维护的类，用于实现homeWindow的界面交互逻辑，以及各个控件的功能
# 本类通过对主窗口界面设计类文件：homeWindow_ui文件的继承，并实现界面与逻辑代码的分离管理
# 最终，mainWindow主窗口界面通过对本类的调用，实例化出主窗口界面对象

# 由于主界面主要负责跳转其他界面，而其它界面于主界面均是平行关系，故本界面的按钮的操函数，交由主窗口界面维护
########################################################################################################################

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from UIModule.homeWindow.homeWindow_ui import Ui_homeWindow


class homeWindow(Ui_homeWindow, QWidget):
    # 界面启动时的初始化方法
    def __init__(self, parent=None):
        # 调用父类初始化
        super(homeWindow, self).__init__(parent)

        # 创建界面
        self.setupUi(self)
