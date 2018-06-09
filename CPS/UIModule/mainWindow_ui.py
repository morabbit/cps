# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

########################################################################################################################
# 主窗口界面设计类文件：mainWindow_ui
# 本文件所维护的类，用于实现mainWindow的界面布局，以及各个控件的实现
# 本类将会由主窗口界面逻辑类文件：mainWindow文件继承，并实现界面的交互逻辑
########################################################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QGridLayout


class Ui_MainWindow_ui(QMainWindow):
    def setupUi(self, MainWindow_ui):
        MainWindow_ui.setObjectName("MainWindow_ui")
        MainWindow_ui.resize(800, 600)
        self.gridLayout_for_subWindow = QtWidgets.QWidget(MainWindow_ui)
        self.gridLayout_for_subWindow.setObjectName("gridLayout_for_subWindow")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayout_for_subWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.subWindow_container = QtWidgets.QWidget(self.gridLayout_for_subWindow)
        self.subWindow_container.setObjectName("widget")
        self.gridLayout.addWidget(self.subWindow_container, 0, 0, 1, 1)
        MainWindow_ui.setCentralWidget(self.gridLayout_for_subWindow)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_ui)
        self.statusbar.setObjectName("statusbar")
        MainWindow_ui.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow_ui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.gridLayout_in_subWindow = QGridLayout(self.subWindow_container)  # 在包含子窗口的widget里面在设置一个小布局
        MainWindow_ui.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow_ui)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_ui)

    def retranslateUi(self, MainWindow_ui):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_ui.setWindowTitle(_translate("MainWindow_ui", "CPS"))

