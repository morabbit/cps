# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingWindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_settingWindow(object):
    def setupUi(self, settingWindow):
        settingWindow.setObjectName("settingWindow")
        settingWindow.resize(684, 532)
        self.horizontalLayout = QtWidgets.QHBoxLayout(settingWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_comeback_homeWindow = QtWidgets.QPushButton(settingWindow)
        self.btn_comeback_homeWindow.setObjectName("btn_comeback_homeWindow")
        self.verticalLayout.addWidget(self.btn_comeback_homeWindow)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_select_position = QtWidgets.QPushButton(settingWindow)
        self.btn_select_position.setObjectName("btn_select_position")
        self.verticalLayout.addWidget(self.btn_select_position)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_select_experiment = QtWidgets.QPushButton(settingWindow)
        self.btn_select_experiment.setObjectName("btn_select_experiment")
        self.verticalLayout.addWidget(self.btn_select_experiment)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.btn_select_analyze = QtWidgets.QPushButton(settingWindow)
        self.btn_select_analyze.setObjectName("btn_select_analyze")
        self.verticalLayout.addWidget(self.btn_select_analyze)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.btn_ready_to_detection = QtWidgets.QPushButton(settingWindow)
        self.btn_ready_to_detection.setObjectName("btn_ready_to_detection")
        self.verticalLayout.addWidget(self.btn_ready_to_detection)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget_for_sub_window = QtWidgets.QWidget(settingWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_for_sub_window.sizePolicy().hasHeightForWidth())
        self.widget_for_sub_window.setSizePolicy(sizePolicy)
        self.widget_for_sub_window.setObjectName("widget_for_sub_window")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_for_sub_window)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget_for_sub_window)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_common_problem = QtWidgets.QLabel(settingWindow)
        self.label_common_problem.setObjectName("label_common_problem")
        self.verticalLayout_2.addWidget(self.label_common_problem)
        self.comboBox_common_problem = QtWidgets.QComboBox(settingWindow)
        self.comboBox_common_problem.setObjectName("comboBox_common_problem")
        self.verticalLayout_2.addWidget(self.comboBox_common_problem)
        self.label_help_doc = QtWidgets.QLabel(settingWindow)
        self.label_help_doc.setObjectName("label_help_doc")
        self.verticalLayout_2.addWidget(self.label_help_doc)
        self.textEdit_help_doc = QtWidgets.QTextEdit(settingWindow)
        self.textEdit_help_doc.setObjectName("textEdit_help_doc")
        self.verticalLayout_2.addWidget(self.textEdit_help_doc)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 9)
        self.horizontalLayout.setStretch(2, 4)

        self.retranslateUi(settingWindow)
        QtCore.QMetaObject.connectSlotsByName(settingWindow)

    def retranslateUi(self, settingWindow):
        _translate = QtCore.QCoreApplication.translate
        settingWindow.setWindowTitle(_translate("settingWindow", "Form"))
        self.btn_comeback_homeWindow.setText(_translate("settingWindow", "返回"))
        self.btn_select_position.setText(_translate("settingWindow", "选择检测位置"))
        self.btn_select_experiment.setText(_translate("settingWindow", "选择实验方法"))
        self.btn_select_analyze.setText(_translate("settingWindow", "选择分析方法"))
        self.btn_ready_to_detection.setText(_translate("settingWindow", "开始检测"))
        self.label_common_problem.setText(_translate("settingWindow", "常见问题："))
        self.label_help_doc.setText(_translate("settingWindow", "帮助文档："))

