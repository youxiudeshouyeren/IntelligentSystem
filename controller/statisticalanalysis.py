from PyQt5.QtGui import QStandardItemModel
import sys

from StatisticalAnalysis_manage import *
from UI.StatisticalAnalysis.statistical_analysis import *

sys.path.append('../')
import util
# from TrustKnowledge_manage import *
from PyQt5.QtWidgets import QDialog
from UI.fuzzyKnowledge.fuzzy_knowledge_page import *


# 可行度知识库页面设计
class StatisticalAnalysis_window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_StatisticalAnalysis()
        self.child.setupUi(self)

        self.load_data()

        self.child.pushButton.clicked.connect(self.search_data_by_time)  # 绑定开始统计的点击事件


    def load_data(self):
        self.model = QStandardItemModel(50, 8)  # 行 列
        self.knowledge_tv_header = ['类型', '开始时间', '结束时间', '车辆数量', '红绿灯1',
                                              '红绿灯2', '红绿灯3','红绿灯4']
        data = StatisticalAnalysis_search_all()
        util.load_data_to_table(self.knowledge_tv_header,data, 50, 8, self.model)
        self.child.tableView.setModel(self.model)
        self.child.tableView.resizeColumnsToContents()

    # 点击查询按钮
    def search_data_by_time(self):
        print('调用查询')
        id1 = self.child.dateTimeEdit.text()
        id2 = self.child.dateTimeEdit_3.text()

        self.search_thread = StatisticalAnalysis_search_by_time(id1,id2)

        self.search_thread.start()
        self.search_thread.sinOut.connect(self.table_data_flush)


    # 刷新左边表格数据
    def table_data_flush(self, sqldata):
        print("sqldata:")
        print(sqldata)
        util.load_data_to_table(self.knowledge_tv_header,sqldata, 50, 8, self.model)
        self.child.tableView.setModel(self.model)
        self.child.tableView.resizeColumnsToContents()