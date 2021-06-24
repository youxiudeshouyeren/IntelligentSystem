from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton
import matplotlib.pyplot as plt
import matplotlib
from PyQt5.QtCore import QTimer
import sys
import random
sys.path.append('../')
from LowerMachine import UpperMachine

matplotlib.use("Qt5Agg")  # 声明使用QT5




class win(QWidget): #创建一个类，为了集成控件
    def __init__(self):
        super(win, self).__init__()
        # global plt
        self.setWindowTitle('定时器的使用')
        self.resize(0,0)
        self.setup_ui()
        self.lastcount=0
        self.nowcount=0
        self.plt=matplotlib.pyplot
        self.plt.ion()
        self.plt.figure(figsize=(6,4))

        
        #标识当前方向
        self.direction=0
        # self.start()

    def setup_ui(self):
        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.operate)  # 每次计时到时间时发出信号
        self.timer.start(1000)  # 设置计时间隔并启动；单位毫秒

    def operate(self):
        global plt
        self.plt.clf()#清除
        self.plt.xlim((-3, 3))
        self.plt.ylim((-3, 3))
        self.plt.axis('off')
        self.nowcount=UpperMachine.vehicleCount

        # self.nowcount=random.uniform(10, 20)
        chang_count=self.nowcount-self.lastcount
        if(chang_count<0):
            chang_count=0
        eastColor="red" if self.direction==0 else 'green'
        northColor='green' if self.direction==0 else 'red'



       
        self.plt.text(0, 2, "north", size=15, ha="center", va="center",bbox=dict(boxstyle="circle",ec=(1, 0.5, 0.5),fc=northColor,))
        self.plt.text(0, -2, "south", size=15,ha="center", va="center",bbox=dict(boxstyle="circle",ec=(1, 0.2, 0.5),fc=northColor,))
        self.plt.text(-2, 0, "west", size=15, ha="center", va="center",bbox=dict(boxstyle="circle",ec=(1, 0.5, 0.5),fc=eastColor,))
        self.plt.text(2, 0, "east", size=15,ha="center", va="center",bbox=dict(boxstyle="circle",ec=(1, 0.2, 0.5),fc=eastColor,))

        if(self.direction==0):
            self.plt.annotate(str(chang_count), xy=(0, 1), xytext=(0, 0), arrowprops=dict(facecolor='black', shrink=0.05))
            self.plt.annotate(str(chang_count), xy=(0, -1), xytext=(0, 0), arrowprops=dict(facecolor='black', shrink=0.05))
        else:
            self.plt.annotate(str(chang_count), xy=(-1, 0), xytext=(0, 0), arrowprops=dict(facecolor='black', shrink=0.05))
            self.plt.annotate(str(chang_count), xy=(1, 0), xytext=(0, 0), arrowprops=dict(facecolor='black', shrink=0.05))


        self.plt.show()
        
        self.lastcount=self.nowcount

# print("定时器读取：",UpperMachine.vehicleCount)

if __name__=='__main__':
    app=QApplication(sys.argv)  #创建应用
    window=win()
    window.show()

    sys.exit(app.exec_())