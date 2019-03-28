# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/waldemar/PycharmProjects/Scheduler/src/design/design_config.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogConfig(object):
    def setupUi(self, DialogConfig):
        DialogConfig.setObjectName("DialogConfig")
        DialogConfig.resize(400, 103)
        self.gridLayout = QtWidgets.QGridLayout(DialogConfig)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(DialogConfig)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinLesson = QtWidgets.QSpinBox(DialogConfig)
        self.spinLesson.setObjectName("spinLesson")
        self.gridLayout.addWidget(self.spinLesson, 0, 1, 1, 1)
        self.pushSave = QtWidgets.QPushButton(DialogConfig)
        self.pushSave.setObjectName("pushSave")
        self.gridLayout.addWidget(self.pushSave, 1, 1, 1, 1)

        self.retranslateUi(DialogConfig)
        QtCore.QMetaObject.connectSlotsByName(DialogConfig)

    def retranslateUi(self, DialogConfig):
        _translate = QtCore.QCoreApplication.translate
        DialogConfig.setWindowTitle(_translate("DialogConfig", "Настройки"))
        self.label.setText(_translate("DialogConfig", "Вторая смена начинается после урока номер "))
        self.pushSave.setText(_translate("DialogConfig", "Сохранить"))

