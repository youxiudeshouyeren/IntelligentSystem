# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fuzzyset_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fuzzyset_dialog(object):
    def setupUi(self, fuzzyset_dialog):
        fuzzyset_dialog.setObjectName("fuzzyset_dialog")
        fuzzyset_dialog.resize(1058, 978)
        self.fuzzyset_id_le = QtWidgets.QLineEdit(fuzzyset_dialog)
        self.fuzzyset_id_le.setGeometry(QtCore.QRect(700, 100, 321, 41))
        self.fuzzyset_id_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.fuzzyset_id_le.setObjectName("fuzzyset_id_le")
        self.fuzzyset_setid_le = QtWidgets.QLineEdit(fuzzyset_dialog)
        self.fuzzyset_setid_le.setGeometry(QtCore.QRect(700, 210, 321, 41))
        self.fuzzyset_setid_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.fuzzyset_setid_le.setObjectName("fuzzyset_setid_le")
        self.fuzzyset_left_le = QtWidgets.QLineEdit(fuzzyset_dialog)
        self.fuzzyset_left_le.setGeometry(QtCore.QRect(700, 530, 321, 41))
        self.fuzzyset_left_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.fuzzyset_left_le.setObjectName("fuzzyset_left_le")
        self.label_4 = QtWidgets.QLabel(fuzzyset_dialog)
        self.label_4.setGeometry(QtCore.QRect(700, 390, 161, 31))
        self.label_4.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(fuzzyset_dialog)
        self.label_5.setGeometry(QtCore.QRect(700, 490, 151, 31))
        self.label_5.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_5.setObjectName("label_5")
        self.fuzzyset_search_btn = QtWidgets.QPushButton(fuzzyset_dialog)
        self.fuzzyset_search_btn.setGeometry(QtCore.QRect(700, 800, 111, 41))
        self.fuzzyset_search_btn.setStyleSheet("\n"
"font: 14pt \"宋体\";")
        self.fuzzyset_search_btn.setObjectName("fuzzyset_search_btn")
        self.fuzzyset_delete_btn = QtWidgets.QPushButton(fuzzyset_dialog)
        self.fuzzyset_delete_btn.setGeometry(QtCore.QRect(700, 880, 111, 41))
        self.fuzzyset_delete_btn.setStyleSheet("\n"
"font: 14pt \"宋体\";")
        self.fuzzyset_delete_btn.setObjectName("fuzzyset_delete_btn")
        self.fuzzyset_eleid_le = QtWidgets.QLineEdit(fuzzyset_dialog)
        self.fuzzyset_eleid_le.setGeometry(QtCore.QRect(700, 320, 321, 41))
        self.fuzzyset_eleid_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.fuzzyset_eleid_le.setObjectName("fuzzyset_eleid_le")
        self.fuzzyset_pointOrline_le = QtWidgets.QLineEdit(fuzzyset_dialog)
        self.fuzzyset_pointOrline_le.setGeometry(QtCore.QRect(700, 430, 321, 41))
        self.fuzzyset_pointOrline_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.fuzzyset_pointOrline_le.setObjectName("fuzzyset_pointOrline_le")
        self.fuzzyset_add_btn = QtWidgets.QPushButton(fuzzyset_dialog)
        self.fuzzyset_add_btn.setGeometry(QtCore.QRect(910, 800, 111, 41))
        self.fuzzyset_add_btn.setStyleSheet("\n"
"font: 14pt \"宋体\";")
        self.fuzzyset_add_btn.setObjectName("fuzzyset_add_btn")
        self.fuzzyset_update_btn = QtWidgets.QPushButton(fuzzyset_dialog)
        self.fuzzyset_update_btn.setGeometry(QtCore.QRect(910, 880, 111, 41))
        self.fuzzyset_update_btn.setStyleSheet("\n"
"font: 14pt \"宋体\";")
        self.fuzzyset_update_btn.setObjectName("fuzzyset_update_btn")
        self.label_3 = QtWidgets.QLabel(fuzzyset_dialog)
        self.label_3.setGeometry(QtCore.QRect(700, 280, 121, 31))
        self.label_3.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_3.setObjectName("label_3")
        self.fuzzyset_tv = QtWidgets.QTableView(fuzzyset_dialog)
        self.fuzzyset_tv.setGeometry(QtCore.QRect(20, 50, 641, 871))
        self.fuzzyset_tv.setObjectName("fuzzyset_tv")
        self.label_2 = QtWidgets.QLabel(fuzzyset_dialog)
        self.label_2.setGeometry(QtCore.QRect(700, 150, 191, 51))
        self.label_2.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(fuzzyset_dialog)
        self.label_6.setGeometry(QtCore.QRect(780, 10, 171, 41))
        self.label_6.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(fuzzyset_dialog)
        self.label.setGeometry(QtCore.QRect(700, 60, 31, 41))
        self.label.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(fuzzyset_dialog)
        self.label_7.setGeometry(QtCore.QRect(700, 590, 151, 31))
        self.label_7.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_7.setObjectName("label_7")
        self.fuzzyset_right_le = QtWidgets.QLineEdit(fuzzyset_dialog)
        self.fuzzyset_right_le.setGeometry(QtCore.QRect(700, 630, 321, 41))
        self.fuzzyset_right_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.fuzzyset_right_le.setObjectName("fuzzyset_right_le")
        self.label_8 = QtWidgets.QLabel(fuzzyset_dialog)
        self.label_8.setGeometry(QtCore.QRect(700, 690, 151, 31))
        self.label_8.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_8.setObjectName("label_8")
        self.fuzzyset_belong_le = QtWidgets.QLineEdit(fuzzyset_dialog)
        self.fuzzyset_belong_le.setGeometry(QtCore.QRect(700, 730, 321, 41))
        self.fuzzyset_belong_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.fuzzyset_belong_le.setObjectName("fuzzyset_belong_le")

        self.retranslateUi(fuzzyset_dialog)
        QtCore.QMetaObject.connectSlotsByName(fuzzyset_dialog)

    def retranslateUi(self, fuzzyset_dialog):
        _translate = QtCore.QCoreApplication.translate
        fuzzyset_dialog.setWindowTitle(_translate("fuzzyset_dialog", "Dialog"))
        self.label_4.setText(_translate("fuzzyset_dialog", "点段标识"))
        self.label_5.setText(_translate("fuzzyset_dialog", "左边界"))
        self.fuzzyset_search_btn.setText(_translate("fuzzyset_dialog", "查询"))
        self.fuzzyset_delete_btn.setText(_translate("fuzzyset_dialog", "删除"))
        self.fuzzyset_add_btn.setText(_translate("fuzzyset_dialog", "新增"))
        self.fuzzyset_update_btn.setText(_translate("fuzzyset_dialog", "修改"))
        self.label_3.setText(_translate("fuzzyset_dialog", "元素ID"))
        self.label_2.setText(_translate("fuzzyset_dialog", "模糊集ID"))
        self.label_6.setText(_translate("fuzzyset_dialog", "模糊集库"))
        self.label.setText(_translate("fuzzyset_dialog", "ID"))
        self.label_7.setText(_translate("fuzzyset_dialog", "右边界"))
        self.label_8.setText(_translate("fuzzyset_dialog", "隶属度"))
