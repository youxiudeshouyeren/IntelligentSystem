from PyQt5.QtGui import QStandardItemModel
import sys

sys.path.append('../')
import util
from FuzzySet_manage import *
from PyQt5.QtWidgets import QDialog
from UI.fuzzyset_page.fuzzyset_page import *


# 可行度知识库页面设计
class FuzzySet_window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_fuzzyset_dialog()
        self.child.setupUi(self)

        self.load_data()

        self.child.fuzzyset_search_btn.clicked.connect(self.search_data)  # 绑定查询函数
        self.child.fuzzyset_add_btn.clicked.connect(self.add_data)#绑定增加按钮
        self.child.fuzzyset_delete_btn.clicked.connect(self.delete_data) #绑定删除按钮
        self.child.fuzzyset_update_btn.clicked.connect(self.update_data)#绑定更新按钮


    def load_data(self):

        self.fuzzyset_tv_header=['ID', '模糊集id', '元素id', '点段标识', '左边界',
                                  '右边界', '隶属度','更新时间']

        data = fuzzySet_search()
        self.model = QStandardItemModel(len(data), 8)  # 行 列
        util.load_data_to_table(self.fuzzyset_tv_header,data, len(data), 8, self.model)
        self.child.fuzzyset_tv.setModel(self.model)
        self.child.fuzzyset_tv.resizeColumnsToContents()

    # 点击查询按钮
    def search_data(self):
        print('调用查询')
        id = self.child.fuzzyset_id_le.text()
        self.search_thread = fuzzySet_search_by_id_thread(id)


        self.search_thread.start()
        self.search_thread.sinOut.connect(self.search_data_flush)

    def search_data_flush(self, sqldata):
        print('执行刷新')
        print(sqldata)
        self.child.fuzzyset_setid_le.setText(str(sqldata[1]))
        self.child.fuzzyset_eleid_le.setText(str(sqldata[2]))
        self.child.fuzzyset_pointOrline_le.setText(str(sqldata[3]))
        self.child.fuzzyset_left_le.setText(str(sqldata[4]))
        self.child.fuzzyset_right_le.setText(str(sqldata[5]))
        self.child.fuzzyset_belong_le.setText(str(sqldata[6]))

    # 点击新增按钮
    def add_data(self):
        print('点击新增')
        fuzzySetId = self.child.fuzzyset_setid_le.text()
        elementId = self.child.fuzzyset_eleid_le.text()
        pointOrline = self.child.fuzzyset_pointOrline_le.text()
        leftBound = self.child.fuzzyset_left_le.text()
        rightBound=self.child.fuzzyset_right_le.text()
        belong=self.child.fuzzyset_belong_le.text()

        print('点击新增')

        data=[]
        print('获取')
        data.append(fuzzySetId)
        data.append(elementId)
        data.append(pointOrline)
        data.append(leftBound)
        data.append(rightBound)
        data.append(belong)
        print(data)
        self.add_thread=fuzzy_set_add_thread(data)
        self.add_thread.start()
        self.add_thread.sinOut.connect(self.table_data_flush)





    # 点击删除按钮
    def delete_data(self):
        print('调用删除')
        id = self.child.fuzzyset_id_le.text()
        self.delete_thread = fuzzy_set_delete_thread(id)
        self.delete_thread.start()
        self.delete_thread.sinOut.connect(self.table_data_flush)

    # 点击更新按钮
    def update_data(self):
        id_value=self.child.fuzzyset_id_le.text()
        fuzzySetId = self.child.fuzzyset_setid_le.text()
        elementId = self.child.fuzzyset_eleid_le.text()
        pointOrline = self.child.fuzzyset_pointOrline_le.text()
        leftBound = self.child.fuzzyset_left_le.text()
        rightBound=self.child.fuzzyset_right_le.text()
        belong=self.child.fuzzyset_belong_le.text()
        data=[]
        print('获取')
        data.append(id_value)
        data.append(fuzzySetId)
        data.append(elementId)
        data.append(pointOrline)
        data.append(leftBound)
        data.append(rightBound)
        data.append(belong)
        print(data)
        self.update_thread=fuzzy_set_update_thread(data)
        self.update_thread.start()
        self.update_thread.sinOut.connect(self.table_data_flush)

    # 刷新左边表格数据
    def table_data_flush(self,sqldata):
        print(sqldata)
        self.model = QStandardItemModel(len(sqldata), 8)  # 行 列
        util.load_data_to_table(self.fuzzyset_tv_header,sqldata, len(sqldata), 8, self.model)
        self.child.fuzzyset_tv.setModel(self.model)
        self.child.fuzzyset_tv.resizeColumnsToContents()