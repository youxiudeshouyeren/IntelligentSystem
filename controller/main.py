from PyQt5.QtWidgets import *
import sys

sys.path.append('../UI/trustknowledge_page/')
sys.path.append('../UI/main_window/')
sys.path.append('../')
from knowledge_page import *
from main_window import *
from trustknowledge import *
from fuzzyset import *
from util import *


class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = parentWindow()
    child = TrustKnow_window()
    child3 = FuzzySet_window()

    # 通过toolButton将两个窗体关联
    btn = window.main_ui.main_knowledge_btn
    btn.clicked.connect(child.show)

    btn3=window.main_ui.main_fuzzyset_btn
    btn3.clicked.connect(child3.show)

    # 显示
    window.show()
    sys.exit(app.exec_())
