# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fuzzy_knowledge_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FuzzyKnowledge_dialog(object):
    def setupUi(self, FuzzyKnowledge_dialog):
        FuzzyKnowledge_dialog.setObjectName("FuzzyKnowledge_dialog")
        FuzzyKnowledge_dialog.resize(1364, 1067)
        self.knowledge_tv = QtWidgets.QTableView(FuzzyKnowledge_dialog)
        self.knowledge_tv.setGeometry(QtCore.QRect(30, 50, 731, 951))
        self.knowledge_tv.setObjectName("knowledge_tv")
        self.label = QtWidgets.QLabel(FuzzyKnowledge_dialog)
        self.label.setGeometry(QtCore.QRect(800, 110, 31, 41))
        self.label.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label.setObjectName("label")
        self.fuzzyknowledge_id_le = QtWidgets.QLineEdit(FuzzyKnowledge_dialog)
        self.fuzzyknowledge_id_le.setGeometry(QtCore.QRect(800, 160, 471, 41))
        self.fuzzyknowledge_id_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.fuzzyknowledge_id_le.setObjectName("fuzzyknowledge_id_le")
        self.label_2 = QtWidgets.QLabel(FuzzyKnowledge_dialog)
        self.label_2.setGeometry(QtCore.QRect(800, 210, 61, 51))
        self.label_2.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(FuzzyKnowledge_dialog)
        self.label_3.setGeometry(QtCore.QRect(800, 330, 61, 31))
        self.label_3.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_3.setObjectName("label_3")
        self.fuzzyknowledge_precondition_le = QtWidgets.QLineEdit(FuzzyKnowledge_dialog)
        self.fuzzyknowledge_precondition_le.setGeometry(QtCore.QRect(800, 260, 471, 41))
        self.fuzzyknowledge_precondition_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.fuzzyknowledge_precondition_le.setObjectName("fuzzyknowledge_precondition_le")
        self.label_4 = QtWidgets.QLabel(FuzzyKnowledge_dialog)
        self.label_4.setGeometry(QtCore.QRect(800, 530, 211, 31))
        self.label_4.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(FuzzyKnowledge_dialog)
        self.label_5.setGeometry(QtCore.QRect(800, 630, 241, 31))
        self.label_5.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_5.setObjectName("label_5")
        self.fuzzyknowledge_conclusion_le = QtWidgets.QLineEdit(FuzzyKnowledge_dialog)
        self.fuzzyknowledge_conclusion_le.setGeometry(QtCore.QRect(800, 370, 471, 41))
        self.fuzzyknowledge_conclusion_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.fuzzyknowledge_conclusion_le.setObjectName("fuzzyknowledge_conclusion_le")
        self.fuzzyknowledge_pre_probability_le = QtWidgets.QLineEdit(FuzzyKnowledge_dialog)
        self.fuzzyknowledge_pre_probability_le.setGeometry(QtCore.QRect(800, 570, 471, 41))
        self.fuzzyknowledge_pre_probability_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.fuzzyknowledge_pre_probability_le.setObjectName("fuzzyknowledge_pre_probability_le")
        self.fuzzyknowledge_con_probability_le = QtWidgets.QLineEdit(FuzzyKnowledge_dialog)
        self.fuzzyknowledge_con_probability_le.setGeometry(QtCore.QRect(800, 670, 471, 41))
        self.fuzzyknowledge_con_probability_le.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.fuzzyknowledge_con_probability_le.setObjectName("fuzzyknowledge_con_probability_le")
        self.fuzzyknowledge_search_btn = QtWidgets.QPushButton(FuzzyKnowledge_dialog)
        self.fuzzyknowledge_search_btn.setGeometry(QtCore.QRect(940, 870, 111, 41))
        self.fuzzyknowledge_search_btn.setStyleSheet("\n"
"font: 14pt \"宋体\";")
        self.fuzzyknowledge_search_btn.setObjectName("fuzzyknowledge_search_btn")
        self.fuzzyknowledge_add_btn = QtWidgets.QPushButton(FuzzyKnowledge_dialog)
        self.fuzzyknowledge_add_btn.setGeometry(QtCore.QRect(1100, 870, 111, 41))
        self.fuzzyknowledge_add_btn.setStyleSheet("\n"
"font: 14pt \"宋体\";")
        self.fuzzyknowledge_add_btn.setObjectName("fuzzyknowledge_add_btn")
        self.fuzzyknowledge_delete_btn = QtWidgets.QPushButton(FuzzyKnowledge_dialog)
        self.fuzzyknowledge_delete_btn.setGeometry(QtCore.QRect(1250, 870, 111, 41))
        self.fuzzyknowledge_delete_btn.setStyleSheet("\n"
"font: 14pt \"宋体\";")
        self.fuzzyknowledge_delete_btn.setObjectName("fuzzyknowledge_delete_btn")
        self.fuzzyknowledge_update_btn = QtWidgets.QPushButton(FuzzyKnowledge_dialog)
        self.fuzzyknowledge_update_btn.setGeometry(QtCore.QRect(780, 870, 111, 41))
        self.fuzzyknowledge_update_btn.setStyleSheet("\n"
"font: 14pt \"宋体\";")
        self.fuzzyknowledge_update_btn.setObjectName("fuzzyknowledge_update_btn")
        self.label_6 = QtWidgets.QLabel(FuzzyKnowledge_dialog)
        self.label_6.setGeometry(QtCore.QRect(1010, 40, 171, 41))
        self.label_6.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(FuzzyKnowledge_dialog)
        self.label_7.setGeometry(QtCore.QRect(800, 430, 61, 31))
        self.label_7.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_7.setObjectName("label_7")
        self.fuzzyknowledge_conclusion_le_2 = QtWidgets.QLineEdit(FuzzyKnowledge_dialog)
        self.fuzzyknowledge_conclusion_le_2.setGeometry(QtCore.QRect(800, 460, 471, 41))
        self.fuzzyknowledge_conclusion_le_2.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.fuzzyknowledge_conclusion_le_2.setObjectName("fuzzyknowledge_conclusion_le_2")
        self.label_8 = QtWidgets.QLabel(FuzzyKnowledge_dialog)
        self.label_8.setGeometry(QtCore.QRect(800, 730, 241, 31))
        self.label_8.setStyleSheet("\n"
"font: 16pt \"宋体\";")
        self.label_8.setObjectName("label_8")
        self.fuzzyknowledge_con_probability_le_2 = QtWidgets.QLineEdit(FuzzyKnowledge_dialog)
        self.fuzzyknowledge_con_probability_le_2.setGeometry(QtCore.QRect(800, 780, 471, 41))
        self.fuzzyknowledge_con_probability_le_2.setStyleSheet("\n"
"font: 12pt \"宋体\";")
        self.fuzzyknowledge_con_probability_le_2.setObjectName("fuzzyknowledge_con_probability_le_2")

        self.retranslateUi(FuzzyKnowledge_dialog)
        QtCore.QMetaObject.connectSlotsByName(FuzzyKnowledge_dialog)

    def retranslateUi(self, FuzzyKnowledge_dialog):
        _translate = QtCore.QCoreApplication.translate
        FuzzyKnowledge_dialog.setWindowTitle(_translate("FuzzyKnowledge_dialog", "Dialog"))
        self.label.setText(_translate("FuzzyKnowledge_dialog", "ID"))
        self.label_2.setText(_translate("FuzzyKnowledge_dialog", "Aid"))
        self.label_3.setText(_translate("FuzzyKnowledge_dialog", "Bid"))
        self.label_4.setText(_translate("FuzzyKnowledge_dialog", "模糊矩阵ID"))
        self.label_5.setText(_translate("FuzzyKnowledge_dialog", "前提可信度"))
        self.fuzzyknowledge_search_btn.setText(_translate("FuzzyKnowledge_dialog", "查询"))
        self.fuzzyknowledge_add_btn.setText(_translate("FuzzyKnowledge_dialog", "新增"))
        self.fuzzyknowledge_delete_btn.setText(_translate("FuzzyKnowledge_dialog", "删除"))
        self.fuzzyknowledge_update_btn.setText(_translate("FuzzyKnowledge_dialog", "修改"))
        self.label_6.setText(_translate("FuzzyKnowledge_dialog", "模糊知识库"))
        self.label_7.setText(_translate("FuzzyKnowledge_dialog", "Cid"))
        self.label_8.setText(_translate("FuzzyKnowledge_dialog", "结论可信度"))
