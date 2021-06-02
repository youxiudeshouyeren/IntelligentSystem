# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knowledge_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TrusKnowledge_dialog(object):
    def setupUi(self, TrusKnowledge_dialog):
        TrusKnowledge_dialog.setObjectName("TrusKnowledge_dialog")
        TrusKnowledge_dialog.resize(1125, 753)
        self.knowledge_tv = QtWidgets.QTableView(TrusKnowledge_dialog)
        self.knowledge_tv.setGeometry(QtCore.QRect(30, 50, 731, 671))
        self.knowledge_tv.setObjectName("knowledge_tv")
        self.label = QtWidgets.QLabel(TrusKnowledge_dialog)
        self.label.setGeometry(QtCore.QRect(780, 90, 31, 41))
        self.label.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label.setObjectName("label")
        self.trustknowledge_id_le = QtWidgets.QLineEdit(TrusKnowledge_dialog)
        self.trustknowledge_id_le.setGeometry(QtCore.QRect(780, 130, 321, 41))
        self.trustknowledge_id_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.trustknowledge_id_le.setObjectName("trustknowledge_id_le")
        self.label_2 = QtWidgets.QLabel(TrusKnowledge_dialog)
        self.label_2.setGeometry(QtCore.QRect(780, 190, 61, 51))
        self.label_2.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(TrusKnowledge_dialog)
        self.label_3.setGeometry(QtCore.QRect(780, 310, 61, 31))
        self.label_3.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_3.setObjectName("label_3")
        self.trustknowledge_precondition_le = QtWidgets.QLineEdit(TrusKnowledge_dialog)
        self.trustknowledge_precondition_le.setGeometry(QtCore.QRect(780, 240, 321, 41))
        self.trustknowledge_precondition_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.trustknowledge_precondition_le.setObjectName("trustknowledge_precondition_le")
        self.label_4 = QtWidgets.QLabel(TrusKnowledge_dialog)
        self.label_4.setGeometry(QtCore.QRect(780, 420, 161, 31))
        self.label_4.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(TrusKnowledge_dialog)
        self.label_5.setGeometry(QtCore.QRect(780, 520, 151, 31))
        self.label_5.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_5.setObjectName("label_5")
        self.trustknowledge_conclusion_le = QtWidgets.QLineEdit(TrusKnowledge_dialog)
        self.trustknowledge_conclusion_le.setGeometry(QtCore.QRect(780, 350, 321, 41))
        self.trustknowledge_conclusion_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.trustknowledge_conclusion_le.setObjectName("trustknowledge_conclusion_le")
        self.trustknowledge_pre_probability_le = QtWidgets.QLineEdit(TrusKnowledge_dialog)
        self.trustknowledge_pre_probability_le.setGeometry(QtCore.QRect(780, 460, 321, 41))
        self.trustknowledge_pre_probability_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.trustknowledge_pre_probability_le.setObjectName("trustknowledge_pre_probability_le")
        self.trustknowledge_con_probability_le = QtWidgets.QLineEdit(TrusKnowledge_dialog)
        self.trustknowledge_con_probability_le.setGeometry(QtCore.QRect(780, 560, 321, 41))
        self.trustknowledge_con_probability_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.trustknowledge_con_probability_le.setObjectName("trustknowledge_con_probability_le")
        self.trustknowledge_search_btn = QtWidgets.QPushButton(TrusKnowledge_dialog)
        self.trustknowledge_search_btn.setGeometry(QtCore.QRect(780, 620, 111, 41))
        self.trustknowledge_search_btn.setStyleSheet("\n"
"font: 14pt \"宋体\";")
        self.trustknowledge_search_btn.setObjectName("trustknowledge_search_btn")
        self.trustknowledge_add_btn = QtWidgets.QPushButton(TrusKnowledge_dialog)
        self.trustknowledge_add_btn.setGeometry(QtCore.QRect(990, 620, 111, 41))
        self.trustknowledge_add_btn.setStyleSheet("\n"
"font: 14pt \"宋体\";")
        self.trustknowledge_add_btn.setObjectName("trustknowledge_add_btn")
        self.trustknowledge_delete_btn = QtWidgets.QPushButton(TrusKnowledge_dialog)
        self.trustknowledge_delete_btn.setGeometry(QtCore.QRect(780, 680, 111, 41))
        self.trustknowledge_delete_btn.setStyleSheet("\n"
"font: 14pt \"宋体\";")
        self.trustknowledge_delete_btn.setObjectName("trustknowledge_delete_btn")
        self.trustknowledge_update_btn = QtWidgets.QPushButton(TrusKnowledge_dialog)
        self.trustknowledge_update_btn.setGeometry(QtCore.QRect(990, 680, 111, 41))
        self.trustknowledge_update_btn.setStyleSheet("\n"
"font: 14pt \"宋体\";")
        self.trustknowledge_update_btn.setObjectName("trustknowledge_update_btn")
        self.label_6 = QtWidgets.QLabel(TrusKnowledge_dialog)
        self.label_6.setGeometry(QtCore.QRect(860, 40, 171, 41))
        self.label_6.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(TrusKnowledge_dialog)
        QtCore.QMetaObject.connectSlotsByName(TrusKnowledge_dialog)

    def retranslateUi(self, TrusKnowledge_dialog):
        _translate = QtCore.QCoreApplication.translate
        TrusKnowledge_dialog.setWindowTitle(_translate("TrusKnowledge_dialog", "Dialog"))
        self.label.setText(_translate("TrusKnowledge_dialog", "ID"))
        self.label_2.setText(_translate("TrusKnowledge_dialog", "前提"))
        self.label_3.setText(_translate("TrusKnowledge_dialog", "结论"))
        self.label_4.setText(_translate("TrusKnowledge_dialog", "前提可信度"))
        self.label_5.setText(_translate("TrusKnowledge_dialog", "结论可信度"))
        self.trustknowledge_search_btn.setText(_translate("TrusKnowledge_dialog", "查询"))
        self.trustknowledge_add_btn.setText(_translate("TrusKnowledge_dialog", "新增"))
        self.trustknowledge_delete_btn.setText(_translate("TrusKnowledge_dialog", "删除"))
        self.trustknowledge_update_btn.setText(_translate("TrusKnowledge_dialog", "修改"))
        self.label_6.setText(_translate("TrusKnowledge_dialog", "可信度知识库"))
