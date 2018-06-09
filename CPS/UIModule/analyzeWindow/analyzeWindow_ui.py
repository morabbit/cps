# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyzeWindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_analyzeWindow(object):
    def setupUi(self, analyzeWindow):
        analyzeWindow.setObjectName("analyzeWindow")
        analyzeWindow.resize(752, 556)
        self.horizontalLayout = QtWidgets.QHBoxLayout(analyzeWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_for_image = QtWidgets.QWidget(analyzeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_for_image.sizePolicy().hasHeightForWidth())
        self.widget_for_image.setSizePolicy(sizePolicy)
        self.widget_for_image.setObjectName("widget_for_image")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget_for_image)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 170, 160, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_for_image = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_for_image.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_for_image.setObjectName("gridLayout_for_image")
        self.horizontalLayout.addWidget(self.widget_for_image)
        self.textEdit_for_results_of_analysis = QtWidgets.QTextEdit(analyzeWindow)
        self.textEdit_for_results_of_analysis.setObjectName("textEdit_for_results_of_analysis")
        self.horizontalLayout.addWidget(self.textEdit_for_results_of_analysis)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_comeback_homeWindow = QtWidgets.QPushButton(analyzeWindow)
        self.btn_comeback_homeWindow.setObjectName("btn_comeback_homeWindow")
        self.verticalLayout.addWidget(self.btn_comeback_homeWindow)
        self.btn_comeback_detectionWindow = QtWidgets.QPushButton(analyzeWindow)
        self.btn_comeback_detectionWindow.setObjectName("btn_comeback_detectionWindow")
        self.verticalLayout.addWidget(self.btn_comeback_detectionWindow)
        self.btn_generate_and_save_report = QtWidgets.QPushButton(analyzeWindow)
        self.btn_generate_and_save_report.setObjectName("btn_generate_and_save_report")
        self.verticalLayout.addWidget(self.btn_generate_and_save_report)
        self.btn_generate_and_print_report = QtWidgets.QPushButton(analyzeWindow)
        self.btn_generate_and_print_report.setObjectName("btn_generate_and_print_report")
        self.verticalLayout.addWidget(self.btn_generate_and_print_report)
        spacerItem = QtWidgets.QSpacerItem(20, 368, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 9)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 2)

        self.retranslateUi(analyzeWindow)
        QtCore.QMetaObject.connectSlotsByName(analyzeWindow)

    def retranslateUi(self, analyzeWindow):
        _translate = QtCore.QCoreApplication.translate
        analyzeWindow.setWindowTitle(_translate("analyzeWindow", "Form"))
        self.btn_comeback_homeWindow.setText(_translate("analyzeWindow", "返回主界面"))
        self.btn_comeback_detectionWindow.setText(_translate("analyzeWindow", "返检测界面"))
        self.btn_generate_and_save_report.setText(_translate("analyzeWindow", "生成并储存报告"))
        self.btn_generate_and_print_report.setText(_translate("analyzeWindow", "生成并打印报告"))

