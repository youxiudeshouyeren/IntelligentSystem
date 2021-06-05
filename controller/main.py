from PyQt5.QtWidgets import *
import sys
from PyQt5.Qt import *
sys.path.append('../UI/trustknowledge_page/')
sys.path.append('../UI/main_window/')
sys.path.append('../')
from UI.main_window.main_window import Ui_MainWindow
from controller.fuzzyKnowledge import FuzzyKnow_window
from controller.fuzzyset import FuzzySet_window
from controller.startCollect import StartCollect_window
from controller.statisticalanalysis import StatisticalAnalysis_window
from controller.trustknowledge import TrustKnow_window


from knowledge_page import *
from main_window import *
from trustknowledge import *
from fuzzyset import *
from startCollect import *
from fuzzyKnowledge import *
from util import *


class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

        #设置背景图片
        palette = QPalette()
        pix=QPixmap("back.jpg")
        pix = pix.scaled(self.width(),self.height())
        palette.setBrush(QPalette.Background,QBrush(pix))
        self.setPalette(palette)

        #关联可信度窗口
        self.child=TrustKnow_window()
        btn = self.main_ui.main_knowledge_btn
        btn.clicked.connect(self.child.show)

        #关联模糊集窗口
        self.child2=FuzzySet_window()
        btn2=self.main_ui.main_fuzzyset_btn
        btn2.clicked.connect(self.child2.show)

        #关联模糊知识窗口
        self.child3=FuzzyKnow_window()
        btn3=self.main_ui.main_fuzzyknowledge_btn
        btn3.clicked.connect(self.child3.show)

        #关联开始演示窗口
        self.child4=StartCollect_window()
        btn4=self.main_ui.main_startcollect_btn
        btn4.clicked.connect(self.child4.show)

        # 关联统计分析
        self.child5 = StatisticalAnalysis_window()
        btn5 = self.main_ui.main_analysis_btn_2
        btn5.clicked.connect(self.child5.show)

        #退出系统按钮
        btn6=self.main_ui.main_exc_btn
        btn6.clicked.connect(self.close)











if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = parentWindow()
    # child = TrustKnow_window()
    # child3 = FuzzySet_window()
    #
    # # 通过toolButton将两个窗体关联
    # btn = window.main_ui.main_knowledge_btn
    # btn.clicked.connect(child.show)
    #
    # btn3=window.main_ui.main_fuzzyset_btn
    # btn3.clicked.connect(child3.show)

    # 显示
    window.show()
    sys.exit(app.exec_())

    
