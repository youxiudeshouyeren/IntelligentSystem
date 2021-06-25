from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton
import matplotlib.pyplot as plt
import matplotlib
import datetime
from PyQt5.QtCore import QTimer
import sys
import random
import time
import numpy as np
sys.path.append('../')
from LowerMachine import UpperMachine

matplotlib.use("Qt5Agg")  # 声明使用QT5

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']



class win(QWidget): #创建一个类，为了集成控件
    def __init__(self):
        super(win, self).__init__()

        self.setWindowTitle('定时器的使用')
        self.resize(0,0)
        self.setup_ui()
        self.lastcount=0
        self.nowcount=0
        self.plt=matplotlib.pyplot
        self.plt.ion()
        self.stage=1
        self.direction=0
        self.chang_count=0








    def setup_ui(self):
        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.change)  # 每次计时到时间时发出信号
        self.timer.start(250)  # 设置计时间隔并启动；单位毫秒



    def operate(self):

        self.plt.cla()#清除
        self.plt.xlim((-3, 3))
        self.plt.ylim((-3, 3))
        self.plt.axis('off')
        self.nowcount=UpperMachine.vehicleCount
       # self.nowcount=random.randint(1,100)

        self.chang_count=self.nowcount-self.lastcount
        if(self.chang_count<0):
            self.chang_count=0

        eastColor="red" if self.direction==0 else 'green'
        northColor='green' if self.direction==0 else 'red'

        time=datetime.datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S'
        )
        x = np.linspace(-2,-0.5,100)
        y=np.zeros(x.shape)
        plt.plot(x,y+0.5, '-k')
        plt.plot(x,y-0.5, '-k')
        plt.plot(y+0.5,x, '-k')
        plt.plot(y-0.5,x, '-k')
        x = np.linspace(0.5,2,100)
        y=np.zeros(x.shape)
        plt.plot(x,y+0.5, '-k')
        plt.plot(x,y-0.5, '-k')
        plt.plot(y+0.5,x, '-k')
        plt.plot(y-0.5,x, '-k')

        self.plt.text(2.5, 2.5, time, size=12,ha="center", va="center",)
        self.plt.text(2.5, 3, '刷新频率：60hz', size=12,ha="center", va="center",)

        self.plt.text(2.5, 2,'车流量'+str(self.nowcount) , size=18,ha="center", va="center",)


        self.plt.text(0, 2, "north", size=15, ha="center", va="center",bbox=dict(boxstyle="circle",ec=(1, 0.5, 0.5),fc=northColor,))
        self.plt.text(0, -2, "south", size=15,ha="center", va="center",bbox=dict(boxstyle="circle",ec=(1, 0.2, 0.5),fc=northColor,))
        self.plt.text(-2, 0, "west", size=15, ha="center", va="center",bbox=dict(boxstyle="circle",ec=(1, 0.5, 0.5),fc=eastColor,))
        self.plt.text(2, 0, "east", size=15,ha="center", va="center",bbox=dict(boxstyle="circle",ec=(1, 0.2, 0.5),fc=eastColor,))




        self.plt.show()
        self.lastcount=self.nowcount

    def change(self):



        if(self.chang_count!=0):
            if self.direction==0:

                self.plt.annotate(str(self.chang_count),size=20, xy=(0, self.stage*0.8), xytext=(0, 0), arrowprops=dict(facecolor='black', shrink=0.05))
                self.plt.annotate(str(self.chang_count),size=20, xy=(0,  -self.stage*0.8), xytext=(0, 0), arrowprops=dict(facecolor='black', shrink=0.05))

            else:

                self.plt.annotate(str(self.chang_count),size=20, xy=(self.stage*0.8,0), xytext=(0, 0), arrowprops=dict(facecolor='black', shrink=0.05))
                self.plt.annotate(str(self.chang_count),size=20, xy=(-self.stage*0.8,0), xytext=(0, 0), arrowprops=dict(facecolor='black', shrink=0.05))


        if(self.stage==3):
            self.operate()
            self.stage=1
        else:
            self.stage=self.stage+1

        self.plt.show()




# print("定时器读取：",UpperMachine.vehicleCount)

if __name__=='__main__':
    app=QApplication(sys.argv)  #创建应用
    window=win()
    window.show()

    sys.exit(app.exec_())