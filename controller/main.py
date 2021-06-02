from PyQt5.QtGui import QStandardItemModel
import util
from TrustKnowledge_manage import *
from UI.main_window.main_window import *

from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
import sys

from controller.trustknowledge import TrustKnow_window


class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)


if __name__=='__main__':

    app=QApplication(sys.argv)
    window=parentWindow()
    child=TrustKnow_window()

    #通过toolButton将两个窗体关联
    btn=window.main_ui.main_knowledge_btn
    btn.clicked.connect(child.show)


    # 显示
    window.show()
    sys.exit(app.exec_())
