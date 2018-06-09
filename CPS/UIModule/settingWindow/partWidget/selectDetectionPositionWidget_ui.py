# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectDetectionPositionWidget_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectDetectionPositionWidget(object):
    def setupUi(self, selectDetectionPositionWidget):
        selectDetectionPositionWidget.setObjectName("selectDetectionPositionWidget")
        selectDetectionPositionWidget.resize(625, 579)
        self.horizontalLayout = QtWidgets.QHBoxLayout(selectDetectionPositionWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_all = QtWidgets.QCheckBox(selectDetectionPositionWidget)
        self.checkBox_all.setObjectName("checkBox_all")
        self.buttonGroup = QtWidgets.QButtonGroup(selectDetectionPositionWidget)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.checkBox_all)
        self.verticalLayout.addWidget(self.checkBox_all)
        self.checkBox_before_ten = QtWidgets.QCheckBox(selectDetectionPositionWidget)
        self.checkBox_before_ten.setObjectName("checkBox_before_ten")
        self.buttonGroup.addButton(self.checkBox_before_ten)
        self.verticalLayout.addWidget(self.checkBox_before_ten)
        self.checkBox_half = QtWidgets.QCheckBox(selectDetectionPositionWidget)
        self.checkBox_half.setObjectName("checkBox_half")
        self.buttonGroup.addButton(self.checkBox_half)
        self.verticalLayout.addWidget(self.checkBox_half)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget_for_samples = QtWidgets.QWidget(selectDetectionPositionWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_for_samples.sizePolicy().hasHeightForWidth())
        self.widget_for_samples.setSizePolicy(sizePolicy)
        self.widget_for_samples.setObjectName("widget_for_samples")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget_for_samples)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 140, 361, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_for_samples = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_for_samples.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_for_samples.setObjectName("gridLayout_for_samples")
        self.horizontalLayout.addWidget(self.widget_for_samples)

        self.retranslateUi(selectDetectionPositionWidget)
        QtCore.QMetaObject.connectSlotsByName(selectDetectionPositionWidget)

    def retranslateUi(self, selectDetectionPositionWidget):
        _translate = QtCore.QCoreApplication.translate
        selectDetectionPositionWidget.setWindowTitle(_translate("selectDetectionPositionWidget", "Form"))
        self.checkBox_all.setText(_translate("selectDetectionPositionWidget", "全选"))
        self.checkBox_before_ten.setText(_translate("selectDetectionPositionWidget", "前10个"))
        self.checkBox_half.setText(_translate("selectDetectionPositionWidget", "一半"))

