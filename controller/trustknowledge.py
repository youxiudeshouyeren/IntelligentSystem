from PyQt5.QtGui import QStandardItemModel
import util
from TrustKnowledge_manage import *
from PyQt5.QtWidgets import QDialog
from UI.trustknowledge_page.knowledge_page import *

# 可行度知识库页面设计
class TrustKnow_window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_TrusKnowledge_dialog()
        self.child.setupUi(self)

        self.data=TrustKnowledge_search()
        self.load_data()

    def load_data(self):
        self.model=QStandardItemModel(15,7)#行 列
        self.model.setHorizontalHeaderLabels(['ID','前提','结论','前提可信度','结论可信度',
                                              '使用次数','上次使用时间'])

        util.load_data_to_table(self.data,15,7,self.model)
        self.child.knowledge_tv.setModel(self.model)
        self.child.knowledge_tv.resizeColumnsToContents()

    #点击查询按钮
    def search_data(self):
        pass

    #点击新增按钮
    def add_data(self):
        pass

    #点击删除按钮
    def delete_data(self):
        pass

    #点击更新按钮
    def update_data(self):
        pass


