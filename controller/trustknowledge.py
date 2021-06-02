from PyQt5.QtGui import QStandardItemModel
import sys

sys.path.append('../')
import util
from TrustKnowledge_manage import *
from PyQt5.QtWidgets import QDialog
from UI.trustknowledge_page.knowledge_page import *


# 可行度知识库页面设计
class TrustKnow_window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_TrusKnowledge_dialog()
        self.child.setupUi(self)

        self.load_data()

        self.child.trustknowledge_search_btn.clicked.connect(self.search_data)  # 绑定查询函数
        self.child.trustknowledge_add_btn.clicked.connect(self.add_data)#绑定增加按钮
        self.child.trustknowledge_delete_btn.clicked.connect(self.delete_data) #绑定删除按钮
        self.child.trustknowledge_update_btn.clicked.connect(self.update_data)#绑定更新按钮
        

    def load_data(self):
        self.model = QStandardItemModel(15, 7)  # 行 列
        self.model.setHorizontalHeaderLabels(['ID', '前提', '结论', '前提可信度', '结论可信度',
                                              '使用次数', '上次使用时间'])
        data = TrustKnowledge_search()
        util.load_data_to_table(data, 15, 7, self.model)
        self.child.knowledge_tv.setModel(self.model)
        self.child.knowledge_tv.resizeColumnsToContents()

    # 点击查询按钮
    def search_data(self):
        print('调用查询')
        id = self.child.trustknowledge_id_le.text()
        self.search_thread = TrustKnowledge_search_by_id_thread(id)

        
        self.search_thread.start()
        self.search_thread.sinOut.connect(self.search_data_flush)

    def search_data_flush(self, sqldata):
        print('执行刷新')
        print(sqldata)
        self.child.trustknowledge_precondition_le.setText(str(sqldata[1]))
        self.child.trustknowledge_conclusion_le.setText(str(sqldata[2]))
        self.child.trustknowledge_pre_probability_le.setText(str(sqldata[3]))
        self.child.trustknowledge_con_probability_le.setText(str(sqldata[4]))

    # 点击新增按钮
    def add_data(self):
        print('点击新增')
        precondition_value = self.child.trustknowledge_precondition_le.text()
        conclusion_value = self.child.trustknowledge_conclusion_le.text()
        pre_probablity_value = self.child.trustknowledge_pre_probability_le.text()
        con_probablity_value = self.child.trustknowledge_con_probability_le.text()
        use_count_value = 0
        print('点击新增')
        last_use_value = datetime.datetime.now().strftime(config.time_format)
        data=[]
        print('获取')
        data.append(precondition_value)
        data.append(conclusion_value)
        data.append(pre_probablity_value)
        data.append(con_probablity_value)
        data.append(use_count_value)
        data.append(last_use_value)
        print(data)
        self.add_thread=TrustKnowledge_add_thread(data)
        self.add_thread.start()
        self.add_thread.sinOut.connect(self.table_data_flush)





    # 点击删除按钮
    def delete_data(self):
        print('调用删除')
        id = self.child.trustknowledge_id_le.text()
        self.delete_thread = TrustKnowledge_delete_thread(id)
        self.delete_thread.start()
        self.delete_thread.sinOut.connect(self.table_data_flush)

    # 点击更新按钮
    def update_data(self):
        id_value=self.child.trustknowledge_id_le.text()
        precondition_value = self.child.trustknowledge_precondition_le.text()
        conclusion_value = self.child.trustknowledge_conclusion_le.text()
        pre_probablity_value = self.child.trustknowledge_pre_probability_le.text()
        con_probablity_value = self.child.trustknowledge_con_probability_le.text()
        use_count_value = 0
        print('点击新增')
        last_use_value = datetime.datetime.now().strftime(config.time_format)
        data=[]
        print('获取')
        data.append(id_value)
        data.append(precondition_value)
        data.append(conclusion_value)
        data.append(pre_probablity_value)
        data.append(con_probablity_value)
        data.append(use_count_value)
        data.append(last_use_value)
        print(data)
        self.update_thread=TrustKnowledge_update_thread(data)
        self.update_thread.start()
        self.update_thread.sinOut.connect(self.table_data_flush)

    # 刷新左边表格数据
    def table_data_flush(self,sqldata):
        print(sqldata)
        util.load_data_to_table(sqldata, 15, 7, self.model)
        self.child.knowledge_tv.setModel(self.model)
        self.child.knowledge_tv.resizeColumnsToContents()