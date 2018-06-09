# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectExperimentMethodWidget_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectExperimentMethodWidget(object):
    def setupUi(self, selectExperimentMethodWidget):
        selectExperimentMethodWidget.setObjectName("selectExperimentMethodWidget")
        selectExperimentMethodWidget.resize(274, 501)
        self.verticalLayout = QtWidgets.QVBoxLayout(selectExperimentMethodWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_method_title = QtWidgets.QLabel(selectExperimentMethodWidget)
        self.label_method_title.setObjectName("label_method_title")
        self.verticalLayout.addWidget(self.label_method_title, 0, QtCore.Qt.AlignHCenter)
        self.tableWidget_method = QtWidgets.QTableWidget(selectExperimentMethodWidget)
        self.tableWidget_method.setObjectName("tableWidget_method")
        self.tableWidget_method.setColumnCount(0)
        self.tableWidget_method.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget_method)
        self.label_ball_number_title = QtWidgets.QLabel(selectExperimentMethodWidget)
        self.label_ball_number_title.setObjectName("label_ball_number_title")
        self.verticalLayout.addWidget(self.label_ball_number_title, 0, QtCore.Qt.AlignHCenter)
        self.tableWidget_ball_number = QtWidgets.QTableWidget(selectExperimentMethodWidget)
        self.tableWidget_ball_number.setObjectName("tableWidget_ball_number")
        self.tableWidget_ball_number.setColumnCount(0)
        self.tableWidget_ball_number.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget_ball_number)
        self.label_speed_and_process_title = QtWidgets.QLabel(selectExperimentMethodWidget)
        self.label_speed_and_process_title.setObjectName("label_speed_and_process_title")
        self.verticalLayout.addWidget(self.label_speed_and_process_title, 0, QtCore.Qt.AlignHCenter)
        self.tableWidget_speed_and_process = QtWidgets.QTableWidget(selectExperimentMethodWidget)
        self.tableWidget_speed_and_process.setObjectName("tableWidget_speed_and_process")
        self.tableWidget_speed_and_process.setColumnCount(0)
        self.tableWidget_speed_and_process.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget_speed_and_process)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_ok = QtWidgets.QPushButton(selectExperimentMethodWidget)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout.addWidget(self.btn_ok)
        self.btn_cancel = QtWidgets.QPushButton(selectExperimentMethodWidget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(selectExperimentMethodWidget)
        QtCore.QMetaObject.connectSlotsByName(selectExperimentMethodWidget)

    def retranslateUi(self, selectExperimentMethodWidget):
        _translate = QtCore.QCoreApplication.translate
        selectExperimentMethodWidget.setWindowTitle(_translate("selectExperimentMethodWidget", "Form"))
        self.label_method_title.setText(_translate("selectExperimentMethodWidget", "选择化学发光，荧光或结合方法"))
        self.label_ball_number_title.setText(_translate("selectExperimentMethodWidget", "选择编码微球个数"))
        self.label_speed_and_process_title.setText(_translate("selectExperimentMethodWidget", "选择进样速度及之间冲洗流程"))
        self.btn_ok.setText(_translate("selectExperimentMethodWidget", "确定"))
        self.btn_cancel.setText(_translate("selectExperimentMethodWidget", "取消"))

