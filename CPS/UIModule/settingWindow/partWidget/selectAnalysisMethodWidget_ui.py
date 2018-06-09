# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectAnalysisMethodWidget_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectAnalysisMethodWidget(object):
    def setupUi(self, selectAnalysisMethodWidget):
        selectAnalysisMethodWidget.setObjectName("selectAnalysisMethodWidget")
        selectAnalysisMethodWidget.resize(249, 561)
        self.verticalLayout = QtWidgets.QVBoxLayout(selectAnalysisMethodWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget_select_analysis_method = QtWidgets.QTableWidget(selectAnalysisMethodWidget)
        self.tableWidget_select_analysis_method.setObjectName("tableWidget_select_analysis_method")
        self.tableWidget_select_analysis_method.setColumnCount(0)
        self.tableWidget_select_analysis_method.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget_select_analysis_method)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_ok = QtWidgets.QPushButton(selectAnalysisMethodWidget)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout.addWidget(self.btn_ok)
        self.btn_cancel = QtWidgets.QPushButton(selectAnalysisMethodWidget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(selectAnalysisMethodWidget)
        QtCore.QMetaObject.connectSlotsByName(selectAnalysisMethodWidget)

    def retranslateUi(self, selectAnalysisMethodWidget):
        _translate = QtCore.QCoreApplication.translate
        selectAnalysisMethodWidget.setWindowTitle(_translate("selectAnalysisMethodWidget", "Form"))
        self.btn_ok.setText(_translate("selectAnalysisMethodWidget", "确定"))
        self.btn_cancel.setText(_translate("selectAnalysisMethodWidget", "取消"))

