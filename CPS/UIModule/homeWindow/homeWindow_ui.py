# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeWindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_homeWindow(object):
    def setupUi(self, homeWindow):
        homeWindow.setObjectName("homeWindow")
        homeWindow.resize(790, 672)
        self.verticalLayout = QtWidgets.QVBoxLayout(homeWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_company_logo = QtWidgets.QLabel(homeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_company_logo.sizePolicy().hasHeightForWidth())
        self.label_company_logo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_company_logo.setFont(font)
        self.label_company_logo.setObjectName("label_company_logo")
        self.horizontalLayout.addWidget(self.label_company_logo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_for_detection = QtWidgets.QLabel(homeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_for_detection.sizePolicy().hasHeightForWidth())
        self.label_for_detection.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.label_for_detection.setFont(font)
        self.label_for_detection.setObjectName("label_for_detection")
        self.gridLayout.addWidget(self.label_for_detection, 2, 2, 1, 1)
        self.btn_analyze = QtWidgets.QPushButton(homeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_analyze.sizePolicy().hasHeightForWidth())
        self.btn_analyze.setSizePolicy(sizePolicy)
        self.btn_analyze.setMinimumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_analyze.setFont(font)
        self.btn_analyze.setObjectName("btn_analyze")
        self.gridLayout.addWidget(self.btn_analyze, 4, 0, 1, 1)
        self.label_for_analyze = QtWidgets.QLabel(homeWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.label_for_analyze.setFont(font)
        self.label_for_analyze.setObjectName("label_for_analyze")
        self.gridLayout.addWidget(self.label_for_analyze, 4, 2, 1, 1)
        self.btn_setting = QtWidgets.QPushButton(homeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_setting.sizePolicy().hasHeightForWidth())
        self.btn_setting.setSizePolicy(sizePolicy)
        self.btn_setting.setMinimumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_setting.setFont(font)
        self.btn_setting.setObjectName("btn_setting")
        self.gridLayout.addWidget(self.btn_setting, 0, 0, 1, 1)
        self.label_for_setting = QtWidgets.QLabel(homeWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.label_for_setting.setFont(font)
        self.label_for_setting.setObjectName("label_for_setting")
        self.gridLayout.addWidget(self.label_for_setting, 0, 2, 1, 1)
        self.btn_detection = QtWidgets.QPushButton(homeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_detection.sizePolicy().hasHeightForWidth())
        self.btn_detection.setSizePolicy(sizePolicy)
        self.btn_detection.setMinimumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_detection.setFont(font)
        self.btn_detection.setObjectName("btn_detection")
        self.gridLayout.addWidget(self.btn_detection, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 4, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 4, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(homeWindow)
        QtCore.QMetaObject.connectSlotsByName(homeWindow)

    def retranslateUi(self, homeWindow):
        _translate = QtCore.QCoreApplication.translate
        homeWindow.setWindowTitle(_translate("homeWindow", "CPS"))
        self.label_company_logo.setText(_translate("homeWindow", "Company Logo"))
        self.label_for_detection.setText(_translate("homeWindow", "机器自动检测"))
        self.btn_analyze.setText(_translate("homeWindow", "分析"))
        self.label_for_analyze.setText(_translate("homeWindow", "对自动分析的数据进行后处理"))
        self.btn_setting.setText(_translate("homeWindow", "设置"))
        self.label_for_setting.setText(_translate("homeWindow", "定义检测内容及检测试剂"))
        self.btn_detection.setText(_translate("homeWindow", "检测"))

