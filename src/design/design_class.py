# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/waldemar/PycharmProjects/Scheduler/src/design/design_class.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogClass(object):
    def setupUi(self, DialogClass):
        DialogClass.setObjectName("DialogClass")
        DialogClass.resize(477, 294)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/icon0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogClass.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(DialogClass)
        self.gridLayout.setObjectName("gridLayout")
        self.pushDelete = QtWidgets.QPushButton(DialogClass)
        self.pushDelete.setObjectName("pushDelete")
        self.gridLayout.addWidget(self.pushDelete, 4, 2, 1, 1)
        self.listView = QtWidgets.QListWidget(DialogClass)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 2, 0, 1, 7)
        self.pushOk = QtWidgets.QPushButton(DialogClass)
        self.pushOk.setObjectName("pushOk")
        self.gridLayout.addWidget(self.pushOk, 3, 6, 1, 1)
        self.comboDelete = QtWidgets.QComboBox(DialogClass)
        self.comboDelete.setObjectName("comboDelete")
        self.gridLayout.addWidget(self.comboDelete, 4, 0, 1, 2)
        self.comboTeacher = QtWidgets.QComboBox(DialogClass)
        self.comboTeacher.setObjectName("comboTeacher")
        self.gridLayout.addWidget(self.comboTeacher, 3, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(DialogClass)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 2)
        self.comboLesson = QtWidgets.QComboBox(DialogClass)
        self.comboLesson.setObjectName("comboLesson")
        self.gridLayout.addWidget(self.comboLesson, 3, 3, 1, 2)
        self.comboImport = QtWidgets.QComboBox(DialogClass)
        self.comboImport.setObjectName("comboImport")
        self.gridLayout.addWidget(self.comboImport, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(DialogClass)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushImport = QtWidgets.QPushButton(DialogClass)
        self.pushImport.setObjectName("pushImport")
        self.gridLayout.addWidget(self.pushImport, 0, 3, 1, 1)
        self.spinDays = QtWidgets.QSpinBox(DialogClass)
        self.spinDays.setObjectName("spinDays")
        self.gridLayout.addWidget(self.spinDays, 0, 6, 1, 1)
        self.spinLesson = QtWidgets.QSpinBox(DialogClass)
        self.spinLesson.setObjectName("spinLesson")
        self.gridLayout.addWidget(self.spinLesson, 3, 5, 1, 1)
        self.line = QtWidgets.QFrame(DialogClass)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 7)
        self.nameEdit = QtWidgets.QLineEdit(DialogClass)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.pushSave = QtWidgets.QPushButton(DialogClass)
        self.pushSave.setObjectName("pushSave")
        self.gridLayout.addWidget(self.pushSave, 4, 4, 1, 3)
        self.checkShift = QtWidgets.QCheckBox(DialogClass)
        self.checkShift.setObjectName("checkShift")
        self.gridLayout.addWidget(self.checkShift, 4, 3, 1, 1)

        self.retranslateUi(DialogClass)
        QtCore.QMetaObject.connectSlotsByName(DialogClass)

    def retranslateUi(self, DialogClass):
        _translate = QtCore.QCoreApplication.translate
        DialogClass.setWindowTitle(_translate("DialogClass", "Редактирование классов"))
        self.pushDelete.setText(_translate("DialogClass", "Удалить"))
        self.pushOk.setText(_translate("DialogClass", "ОК"))
        self.label_2.setText(_translate("DialogClass", "Дней в неделю:"))
        self.label.setText(_translate("DialogClass", "Класс:"))
        self.pushImport.setText(_translate("DialogClass", "Импорт"))
        self.pushSave.setText(_translate("DialogClass", "Добавить класс"))
        self.checkShift.setText(_translate("DialogClass", "2 Смена"))

