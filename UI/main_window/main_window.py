# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_knowledge_btn = QtWidgets.QPushButton(self.centralwidget)
        self.main_knowledge_btn.setGeometry(QtCore.QRect(90, 150, 181, 131))
        self.main_knowledge_btn.setObjectName("main_knowledge_btn")
        self.main_fuzzyknowledge_btn = QtWidgets.QPushButton(self.centralwidget)
        self.main_fuzzyknowledge_btn.setGeometry(QtCore.QRect(490, 150, 171, 131))
        self.main_fuzzyknowledge_btn.setObjectName("main_fuzzyknowledge_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_knowledge_btn.setText(_translate("MainWindow", "可信度知识维护"))
        self.main_fuzzyknowledge_btn.setText(_translate("MainWindow", "模糊知识维护"))
