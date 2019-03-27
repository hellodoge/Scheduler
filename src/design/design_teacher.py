# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_teacher.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogTeacher(object):
    def setupUi(self, DialogTeacher):
        DialogTeacher.setObjectName("DialogTeacher")
        DialogTeacher.resize(326, 294)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/icon0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogTeacher.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(DialogTeacher)
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QtWidgets.QListWidget(DialogTeacher)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(DialogTeacher)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.pushAdd = QtWidgets.QPushButton(DialogTeacher)
        self.pushAdd.setObjectName("pushAdd")
        self.gridLayout.addWidget(self.pushAdd, 1, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(DialogTeacher)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 1)
        self.pushRemove = QtWidgets.QPushButton(DialogTeacher)
        self.pushRemove.setObjectName("pushRemove")
        self.gridLayout.addWidget(self.pushRemove, 2, 1, 1, 1)

        self.retranslateUi(DialogTeacher)
        QtCore.QMetaObject.connectSlotsByName(DialogTeacher)

    def retranslateUi(self, DialogTeacher):
        _translate = QtCore.QCoreApplication.translate
        DialogTeacher.setWindowTitle(_translate("DialogTeacher", "Добавление учителей"))
        self.pushAdd.setText(_translate("DialogTeacher", "Добавить"))
        self.pushRemove.setText(_translate("DialogTeacher", "Удалить"))

