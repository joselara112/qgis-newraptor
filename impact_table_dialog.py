# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'impact_table.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgimpacts(object):
    def setupUi(self, dlgimpacts):
        dlgimpacts.setObjectName("dlgimpacts")
        dlgimpacts.resize(483, 207)
        self.tableimpacts = QtWidgets.QTableWidget(dlgimpacts)
        self.tableimpacts.setGeometry(QtCore.QRect(10, 0, 461, 192))
        self.tableimpacts.setAlternatingRowColors(True)
        self.tableimpacts.setObjectName("tableimpacts")
        self.tableimpacts.setColumnCount(3)
        self.tableimpacts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableimpacts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableimpacts.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableimpacts.setHorizontalHeaderItem(2, item)

        self.retranslateUi(dlgimpacts)
        QtCore.QMetaObject.connectSlotsByName(dlgimpacts)

    def retranslateUi(self, dlgimpacts):
        _translate = QtCore.QCoreApplication.translate
        dlgimpacts.setWindowTitle(_translate("dlgimpacts", "Impacts Table"))
        item = self.tableimpacts.horizontalHeaderItem(0)
        item.setText(_translate("dlgimpacts", "Project"))
        item = self.tableimpacts.horizontalHeaderItem(1)
        item.setText(_translate("dlgimpacts", "Type"))
        item = self.tableimpacts.horizontalHeaderItem(2)
        item.setText(_translate("dlgimpacts", "Distance"))

