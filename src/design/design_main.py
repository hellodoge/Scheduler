# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/waldemar/PycharmProjects/Scheduler/src/design/design_main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(539, 297)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/icon0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(190, 0, 21, 301))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 201, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushLesson = QtWidgets.QPushButton(self.layoutWidget)
        self.pushLesson.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushLesson.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("media/icon1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushLesson.setIcon(icon1)
        self.pushLesson.setCheckable(False)
        self.pushLesson.setChecked(False)
        self.pushLesson.setFlat(True)
        self.pushLesson.setObjectName("pushLesson")
        self.verticalLayout.addWidget(self.pushLesson)
        self.pushTeacher = QtWidgets.QPushButton(self.layoutWidget)
        self.pushTeacher.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushTeacher.setFocusPolicy(QtCore.Qt.NoFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("media/icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushTeacher.setIcon(icon2)
        self.pushTeacher.setCheckable(False)
        self.pushTeacher.setFlat(True)
        self.pushTeacher.setObjectName("pushTeacher")
        self.verticalLayout.addWidget(self.pushTeacher)
        self.pushClass = QtWidgets.QPushButton(self.layoutWidget)
        self.pushClass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushClass.setFocusPolicy(QtCore.Qt.NoFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("media/icon3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushClass.setIcon(icon3)
        self.pushClass.setCheckable(False)
        self.pushClass.setFlat(True)
        self.pushClass.setObjectName("pushClass")
        self.verticalLayout.addWidget(self.pushClass)
        self.pushSchedule = QtWidgets.QPushButton(self.layoutWidget)
        self.pushSchedule.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushSchedule.setFocusPolicy(QtCore.Qt.NoFocus)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("media/icon4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushSchedule.setIcon(icon4)
        self.pushSchedule.setFlat(True)
        self.pushSchedule.setObjectName("pushSchedule")
        self.verticalLayout.addWidget(self.pushSchedule)
        self.pushConfig = QtWidgets.QPushButton(self.layoutWidget)
        self.pushConfig.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushConfig.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushConfig.setAutoFillBackground(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("media/icon5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushConfig.setIcon(icon5)
        self.pushConfig.setFlat(True)
        self.pushConfig.setObjectName("pushConfig")
        self.verticalLayout.addWidget(self.pushConfig)
        self.pushAuthor = QtWidgets.QPushButton(self.centralwidget)
        self.pushAuthor.setGeometry(QtCore.QRect(440, 260, 87, 29))
        self.pushAuthor.setDefault(False)
        self.pushAuthor.setFlat(False)
        self.pushAuthor.setObjectName("pushAuthor")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 180, 341, 111))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Татьяна3000"))
        self.pushLesson.setText(_translate("MainWindow", "Добавить предметы"))
        self.pushTeacher.setText(_translate("MainWindow", "Добавить учителей"))
        self.pushClass.setText(_translate("MainWindow", "Добавить классы"))
        self.pushSchedule.setText(_translate("MainWindow", "Генерировать расписание"))
        self.pushConfig.setText(_translate("MainWindow", "Настройки"))
        self.pushAuthor.setText(_translate("MainWindow", "Автор"))
        self.label.setText(_translate("MainWindow", "Татьяна3000 позволит вам автоматически составить\n"
"школьное расписание для каждого класса и сохранить\n"
"его в удобной для учеников и учителей форме. \n"
"От вас потребуется лишь занести настройки в \n"
"соответствующие поля, а остальное \n"
"сделает алгоритм программы."))

