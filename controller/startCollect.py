from PyQt5.QtWidgets import QDialog
import sys
sys.path.append('../')
from UI.startcollect_page.startcollect_page import *

#开始演示页面
class StartCollect_window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_startCollect_dialog()
        self.child.setupUi(self)

        self.child.startcollect_btn.clicked.connect(self.start_collect)#点击开始演示按钮

        self.child.stopcollect_btn.clicked.connect(self.stop_collect)


    def start_collect(self):


        self.ew_machine=("可信度" if self.child.ew_trust_rbtn.isChecked() else "模糊")
        # 根据单选按钮判断选择哪个推理机

        self.sn_machine=("可信度" if self.child.sn_trust_rbtn.isChecked() else "模糊")

        print(self.ew_machine)
        print(self.sn_machine)

    def stop_collect(self):
        print('停止演示')



