from PyQt5.QtWidgets import *
import sys

from UI.main_window.main_window import Ui_MainWindow
from controller.fuzzyKnowledge import FuzzyKnow_window
from controller.trustknowledge import TrustKnow_window

sys.path.append('../UI/trustknowledge_page/')
sys.path.append('../UI/main_window/')
sys.path.append('../')
from knowledge_page import *
from main_window import *
from trustknowledge import *
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

    child2 = FuzzyKnow_window()


    # 通过toolButton将两个窗体关联
    btn = window.main_ui.main_knowledge_btn
    btn.clicked.connect(child.show)

    btn2 = window.main_ui.main_fuzzyknowledge_btn
    btn2.clicked.connect(child2.show)

    # 显示
    window.show()
    sys.exit(app.exec_())
