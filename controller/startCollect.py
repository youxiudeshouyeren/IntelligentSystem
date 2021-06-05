from PyQt5.QtWidgets import QDialog
import sys
sys.path.append('../')
from UI.startcollect_page.startcollect_page import *
from machine_main import *


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

        # self.start_thread=TheardMain_thread()
        self.start_thread=Machine_thread(self.ew_machine,self.sn_machine)
        self.start_thread.start()

        self.start_thread.sinOut.connect(self.flush_process)
        

    def stop_collect(self):
        print('停止演示')


    #刷新GUI
    def flush_process(self,data):
        # print(data)
        print('GUI获取数据')
        #东西方向
        if(data[0]=='0'):
            self.child.ew_vehichecount_le.setText(str(data[1]))
            self.child.ew_vehiche_begintime_le.setText(str(data[2]))
            self.child.ew_vehiche_endtime_le.setText(str(data[3]))
            self.child.ew_light_time.setText(str(data[5]))
            self.child.ew_light_le.setText('红灯')
            self.child.sn_light_le.setText('绿灯')
            self.child.ew_process_text.setText(str(data[4]))
        else:
            self.child.sn_vehichecount_le.setText(str(data[1]))
            self.child.sn_vehiche_begintime_le.setText(str(data[2]))
            self.child.sn_vehiche_endtime_le.setText(str(data[3]))
            self.child.sn_light_time.setText(str(data[5]))
            self.child.sn_light_le.setText('红灯')
            self.child.ew_light_le.setText('绿灯')
            self.child.sn_process_text.setText(str(data[4]))





