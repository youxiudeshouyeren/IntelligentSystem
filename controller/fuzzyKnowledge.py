from PyQt5.QtGui import QStandardItemModel
import sys


from FuzzyKnowledge_manage import *
sys.path.append('../')
import util
# from TrustKnowledge_manage import *
from PyQt5.QtWidgets import QDialog
from UI.fuzzyKnowledge.fuzzy_knowledge_page import *


# 可行度知识库页面设计
class FuzzyKnow_window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_FuzzyKnowledge_dialog()
        self.child.setupUi(self)

        self.load_data()

        self.child.fuzzyknowledge_search_btn.clicked.connect(self.search_data)  # 绑定查询函数
        self.child.fuzzyknowledge_add_btn.clicked.connect(self.add_data)  # 绑定增加按钮
        self.child.fuzzyknowledge_delete_btn.clicked.connect(self.delete_data)  # 绑定删除按钮
        self.child.fuzzyknowledge_update_btn.clicked.connect(self.update_data)  # 绑定更新按钮

    def load_data(self):
        self.model = QStandardItemModel(50, 9)  # 行 列
        self.knowledge_tv_header = ['模糊知识ID', '模糊集Aid', '模糊集Bid', '模糊集Cid', '模糊矩阵ID',
                                              '前提可信度', '结论可信度','更新时间','使用次数']
       # self.model.setHorizontalHeaderLabels(['模糊知识ID', '模糊集Aid', '模糊集Bid', '模糊集Cid', '模糊矩阵ID',
                  #                            '前提可信度', '结论可信度','更新时间','使用次数'])
        data = FuzzyKnowledge_search()

        util.load_data_to_table(self.knowledge_tv_header,data, 50, 9, self.model)
        self.child.knowledge_tv.setModel(self.model)
        self.child.knowledge_tv.resizeColumnsToContents()

    # 点击查询按钮
    def search_data(self):
        print('调用查询')
        id = self.child.fuzzyknowledge_id_le.text()
        self.search_thread = FuzzyKnowledge_search_by_id_thread(id)

        self.search_thread.start()
        self.search_thread.sinOut.connect(self.search_data_flush)

    def search_data_flush(self, sqldata):
        print('执行刷新')
        print(sqldata)
        self.child.fuzzyknowledge_precondition_le.setText(str(sqldata[1]))
        self.child.fuzzyknowledge_conclusion_le.setText(str(sqldata[2]))
        self.child.fuzzyknowledge_conclusion_le_2.setText(str(sqldata[3]))
        self.child.fuzzyknowledge_pre_probability_le.setText(str(sqldata[4]))
        self.child.fuzzyknowledge_con_probability_le.setText(str(sqldata[5]))
        self.child.fuzzyknowledge_con_probability_le_2.setText(str(sqldata[6]))

    # 点击新增按钮
    def add_data(self):
        print('点击新增')


        precondition_a = self.child.fuzzyknowledge_precondition_le.text()
        precondition_b= self.child.fuzzyknowledge_conclusion_le.text()
        conclusion_c= self.child.fuzzyknowledge_conclusion_le_2.text()
        fuzzyMatrixId= self.child.fuzzyknowledge_pre_probability_le.text()
        pre_probablity_value= self.child.fuzzyknowledge_con_probability_le.text()
        con_probablity_value= self.child.fuzzyknowledge_con_probability_le_2.text()

        print('点击新增')
        data = []
        print('获取')
        data.append(precondition_a)
        data.append(precondition_b)
        data.append(conclusion_c)
        data.append(fuzzyMatrixId)
        data.append(pre_probablity_value)
        data.append(con_probablity_value)
        print(data)
        self.add_thread = FuzzyKnowledge_add_thread(data)
        self.add_thread.start()
        self.add_thread.sinOut.connect(self.table_data_flush)

    # 点击删除按钮
    def delete_data(self):
        print('调用删除')
        id = self.child.fuzzyknowledge_id_le.text()
        self.delete_thread = FuzzyKnowledge_delete_thread(id)
        self.delete_thread.start()
        self.delete_thread.sinOut.connect(self.table_data_flush)

    # 点击更新按钮
    def update_data(self):
        # id_value = self.child.trustknowledge_id_le.text()
        # precondition_value = self.child.trustknowledge_precondition_le.text()
        # conclusion_value = self.child.trustknowledge_conclusion_le.text()
        # pre_probablity_value = self.child.trustknowledge_pre_probability_le.text()
        # con_probablity_value = self.child.trustknowledge_con_probability_le.text()
        # use_count_value = 0
        id_value = self.child.fuzzyknowledge_id_le.text()
        precondition_a = self.child.fuzzyknowledge_precondition_le.text()
        precondition_b= self.child.fuzzyknowledge_conclusion_le.text()
        conclusion_c= self.child.fuzzyknowledge_conclusion_le_2.text()
        fuzzyMatrixId= self.child.fuzzyknowledge_pre_probability_le.text()
        pre_probablity_value= self.child.fuzzyknowledge_con_probability_le.text()
        con_probablity_value= self.child.fuzzyknowledge_con_probability_le_2.text()


        print('点击新增')
        
        data = []
        print('获取')
        data.append(id_value)
        data.append(precondition_a)
        data.append(precondition_b)
        data.append(conclusion_c)
        data.append(fuzzyMatrixId)
        data.append(pre_probablity_value)
        data.append(con_probablity_value)
        print(data)
        self.update_thread = FuzzyKnowledge_update_thread(data)
        self.update_thread.start()
        self.update_thread.sinOut.connect(self.table_data_flush)

    # 刷新左边表格数据
    def table_data_flush(self, sqldata):
        print("sqldata:")
        print(sqldata)

        util.load_data_to_table(self.knowledge_tv_header,sqldata, 50, 9, self.model)
        self.child.knowledge_tv.setModel(self.model)
        self.child.knowledge_tv.resizeColumnsToContents()