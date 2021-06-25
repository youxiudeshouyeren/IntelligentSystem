from PyQt5.QtWidgets import QDialog
import sys
import matplotlib.pyplot as plt
import start_show
import showVehicle
import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
sys.path.append('../')
from UI.startcollect_page.startcollect_page import *
from machine_main import *


# 开始演示页面
class StartCollect_window(QDialog):
    def __init__(self):
        self.lineShow = start_show.StartShow()
        self.vehicleShow = showVehicle.win()
        QDialog.__init__(self)

        self.child = Ui_startCollect_dialog()
        self.child.setupUi(self)

        self.child.startcollect_btn.clicked.connect(self.start_collect)  # 点击开始演示按钮

        self.child.stopcollect_btn.clicked.connect(self.stop_collect)

    def start_collect(self):

        # 数据源的选择 下位机或百度
        self.dataSourse = ('low' if self.child.low_rbtn.isChecked() else 'baidu')

        self.ew_machine = ("可信度" if self.child.ew_trust_rbtn.isChecked() else "模糊")
        # 根据单选按钮判断选择哪个推理机

        self.sn_machine = ("可信度" if self.child.sn_trust_rbtn.isChecked() else "模糊")

        print(self.ew_machine)
        print(self.sn_machine)

        # self.start_thread=TheardMain_thread()
        self.port = self.child.port_le.text()
        self.min_time = self.child.mintime_le.text()
        self.max_time = self.child.maxtime_le.text()
        self.start_thread = Machine_thread(self.ew_machine, self.sn_machine, self.port, self.min_time, self.max_time,self.dataSourse)
        self.start_thread.start()

        self.start_thread.sinOut.connect(self.flush_process)

    def stop_collect(self):
        # self.start_thread.stop_thra()
        print('停止演示')

    def time_data1(time_sj):  # 传入单个时间比如'2019-8-01 00:00:00'，类型为str
        data_sj = time.strptime(time_sj, "%Y-%m-%d %H:%M:%S")  # 定义格式
        time_int = int(time.mktime(data_sj))
        return time_int  # 返回传入时间的时间戳，类型为int

    # 刷新GUI
    def flush_process(self, data):
        print("flush_process")
        print(data)
        print('GUI获取数据')
        # 东西方向

        if (data[0] == '0'):
            self.vehicleShow.direction = 0
            self.child.ew_vehichecount_le.setText(str(data[1]))
            self.child.ew_vehiche_begintime_le.setText(str(data[2]))
            self.child.ew_vehiche_endtime_le.setText(str(data[3]))
            self.child.ew_light_time.setText(str(data[5]))
            self.child.ew_light_le.setText('红灯')
            self.child.sn_light_le.setText('绿灯')
            self.child.ew_process_text.setText(str(data[4]))
        else:
            self.vehicleShow.direction = 1
            self.child.sn_vehichecount_le.setText(str(data[1]))
            self.child.sn_vehiche_begintime_le.setText(str(data[2]))
            self.child.sn_vehiche_endtime_le.setText(str(data[3]))
            self.child.sn_light_time.setText(str(data[5]))
            self.child.sn_light_le.setText('红灯')
            self.child.ew_light_le.setText('绿灯')
            self.child.sn_process_text.setText(str(data[4]))
        print("ui show")
        print(str(data[2]))
        if (data[0] == '0'):
            timeArray = time.strptime(str(data[2]), "%Y-%m-%d %H:%M:%S")
            timeStamp = int(time.mktime(timeArray))  # 1524822540
            ftime = timeStamp / 10
            print("ftime")
            print(ftime)
            print("data[1]")
            print(data[1])
            print("data[5]")
            print(data[5])
            self.lineShow.add_data(1, int(ftime), int(data[1]), int(data[5]))
        else:
            timeArray = time.strptime(str(data[2]), "%Y-%m-%d %H:%M:%S")
            timeStamp = int(time.mktime(timeArray))  # 1524822540
            ftime = timeStamp / 10
            print("else")
            print("ftime")
            print(ftime)
            print("data[1]")
            print(data[1])
            print("data[5]")
            print(data[5])
            self.lineShow.add_data(2, int(ftime), int(data[1]), int(data[5]))
