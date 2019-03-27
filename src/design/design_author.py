# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_author.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogAuthor(object):
    def setupUi(self, DialogAuthor):
        DialogAuthor.setObjectName("DialogAuthor")
        DialogAuthor.resize(392, 106)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/icon0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogAuthor.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(DialogAuthor)
        self.label.setGeometry(QtCore.QRect(10, 10, 281, 41))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogAuthor)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 491, 71))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(DialogAuthor)
        QtCore.QMetaObject.connectSlotsByName(DialogAuthor)

    def retranslateUi(self, DialogAuthor):
        _translate = QtCore.QCoreApplication.translate
        DialogAuthor.setWindowTitle(_translate("DialogAuthor", "Тут должно это быть"))
        self.label.setText(_translate("DialogAuthor", "Waldemar\n"
"hellodoge@tuta.io\n"
""))
        self.label_2.setText(_translate("DialogAuthor", "Icons made by Gregor Cresnar, OHCA, Freepik from а flaticon.com\n"
"Flaticon is licensed by Creative Commons BY 3.0"))

