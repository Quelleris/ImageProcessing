# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\sugil\OneDrive\Pulpit\APO\dialogs\Informacja o programie.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.resize(215, 88)
        aboutDialog.setMaximumSize(QtCore.QSize(215, 88))
        self.verticalLayout = QtWidgets.QVBoxLayout(aboutDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(aboutDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(aboutDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(aboutDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(aboutDialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        self.retranslateUi(aboutDialog)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "O programie"))
        self.label.setText(_translate("aboutDialog", "Aplikacja zbiorcza z ćwiczeń laboratoryjnych"))
        self.label_2.setText(_translate("aboutDialog", "Autor: Maja Frydrych"))
        self.label_3.setText(_translate("aboutDialog", "Prowadzący: mgr inż. Łukasz Roszkowiak"))
        self.label_4.setText(_translate("aboutDialog", "WIT Grupa ID: IO1"))
