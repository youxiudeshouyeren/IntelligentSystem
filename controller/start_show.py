
import matplotlib
import matplotlib.pyplot as plt
import math
import time
matplotlib.use("Qt5Agg")  # 声明使用QT5

class StartShow():
    def __init__(self,n):
        self.fig =plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Num')
        if n==1:
            self.ax.set_title('WE')
        else:
            self.ax.set_title('SN')
        self.line1 = None
        self.line2 = None
        plt.grid(True)  # 添加网格
        plt.ion()  # interactive mode on
        self.obsX = []
        self.obsY1 = []
        self.obsY2 = []

    def add_data(self,time,car,greentime):
        self.obsX.append(time)
        self.obsY1.append(car)
        self.obsY2.append(greentime)

        if self.line1 is None:
            self.line1 = self.ax.plot(self.obsX, self.obsY1, '-g', marker='*')[0]
        if self.line2 is None:
            self.line2 = self.ax.plot(self.obsX, self.obsY2, '-r', marker='*')[0]

        self.line1.set_xdata(self.obsX)
        self.line1.set_ydata(self.obsY1)

        self.line2.set_xdata(self.obsX)
        self.line2.set_ydata(self.obsY2)
        if len(self.obsX)<10:
            min=self.obsX[0]
        else:
            min = self.obsX[len(self.obsX)-10]
        max=min+5
        self.ax.set_xlim([min,max])
        self.ax.set_ylim([0,60])

        plt.pause(0.1)

import random


if __name__ == '__main__':
    nsShow = StartShow(1)

    t0 = time.time()

    while True:
        t = time.time()-t0
        nsShow.add_data(int(t), random.randint(0,9) ,random.randint(0,100))
        time.sleep(1)
