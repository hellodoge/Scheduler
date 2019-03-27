# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_lesson.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogLesson(object):
    def setupUi(self, DialogLesson):
        DialogLesson.setObjectName("DialogLesson")
        DialogLesson.resize(327, 294)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/icon0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogLesson.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(DialogLesson)
        self.gridLayout.setObjectName("gridLayout")
        self.pushAdd = QtWidgets.QPushButton(DialogLesson)
        self.pushAdd.setObjectName("pushAdd")
        self.gridLayout.addWidget(self.pushAdd, 1, 1, 1, 1)
        self.listView = QtWidgets.QListWidget(DialogLesson)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 3)
        self.lineEdit = QtWidgets.QLineEdit(DialogLesson)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.pushRemove = QtWidgets.QPushButton(DialogLesson)
        self.pushRemove.setObjectName("pushRemove")
        self.gridLayout.addWidget(self.pushRemove, 1, 2, 1, 1)

        self.retranslateUi(DialogLesson)
        QtCore.QMetaObject.connectSlotsByName(DialogLesson)

    def retranslateUi(self, DialogLesson):
        _translate = QtCore.QCoreApplication.translate
        DialogLesson.setWindowTitle(_translate("DialogLesson", "Добавление предметов"))
        self.pushAdd.setText(_translate("DialogLesson", "Добавить"))
        self.pushRemove.setText(_translate("DialogLesson", "Удалить"))

