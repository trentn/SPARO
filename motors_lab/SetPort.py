# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SetPort.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from Serial import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog, build_serial_config):
        Dialog.setObjectName("Dialog")
        Dialog.resize(369, 172)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)
        self.port_name = QtWidgets.QLineEdit(Dialog)
        self.port_name.setObjectName("port_name")
        self.gridLayout.addWidget(self.port_name, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.baud_rate = QtWidgets.QLineEdit(Dialog)
        self.baud_rate.setObjectName("baud_rate")
        self.gridLayout.addWidget(self.baud_rate, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(build_serial_config(self.port_name, self.baud_rate, Dialog.accept))
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Set Port"))
        self.label.setText(_translate("Dialog", "Port"))
        self.label_2.setText(_translate("Dialog", "Baud"))

def build_show_serial_config(serial_thread):
    def show_serial_config():
        dialog = QtWidgets.QDialog()
        d_ui = Ui_Dialog()
        d_ui.setupUi(dialog, serial_thread.build_serial_config)
        dialog.show()
        dialog.exec_()
    return show_serial_config