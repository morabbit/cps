# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcomeWidget_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_welcomeWidget(object):
    def setupUi(self, welcomeWidget):
        welcomeWidget.setObjectName("welcomeWidget")
        welcomeWidget.resize(601, 478)
        self.gridLayout = QtWidgets.QGridLayout(welcomeWidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(220, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label_company_logo = QtWidgets.QLabel(welcomeWidget)
        self.label_company_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_company_logo.setObjectName("label_company_logo")
        self.gridLayout.addWidget(self.label_company_logo, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(219, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 195, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(220, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.label_welcome = QtWidgets.QLabel(welcomeWidget)
        self.label_welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.label_welcome.setObjectName("label_welcome")
        self.gridLayout.addWidget(self.label_welcome, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(219, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 195, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 1, 1, 1)

        self.retranslateUi(welcomeWidget)
        QtCore.QMetaObject.connectSlotsByName(welcomeWidget)

    def retranslateUi(self, welcomeWidget):
        _translate = QtCore.QCoreApplication.translate
        welcomeWidget.setWindowTitle(_translate("welcomeWidget", "Form"))
        self.label_company_logo.setText(_translate("welcomeWidget", "Company Logo"))
        self.label_welcome.setText(_translate("welcomeWidget", "欢迎使用XXX公司的产品"))

