import matplotlib
import matplotlib.pyplot as plt
import math
import time
matplotlib.use("Qt5Agg")  # 声明使用QT5

class StartShow():
    def __init__(self):
        self.fig =plt.figure(figsize=(18,6))
        self.ax_1 = self.fig.add_subplot(1, 3, 1)
        self.ax_1.set_xlabel('Time')
        self.ax_1.set_ylabel('Num')

        self.ax_1.set_title('WE')
        self.line1 = None
        self.line2 = None
        plt.grid(True)  # 添加网格
        plt.ion()  # interactive mode on
        self.obsX = []
        self.obsY1 = []
        self.obsY2 = []

        self.ax_2 = self.fig.add_subplot(1, 3, 2)
        self.ax_2.set_title('SN')
        self.ax_2.set_xlabel('T')
        self.ax_2.set_ylabel('N')
        self.line1_2 = None
        self.line2_2 = None
        plt.grid(True)  # 添加网格
        plt.ion()  # interactive mode on
        self.obsX_2 = []
        self.obsY1_2 = []
        self.obsY2_2 = []

        self.ax_3 = self.fig.add_subplot(1, 3, 3)

    def add_data(self,type,time,car,greentime):
        if type==1:
            self.obsX.append(time)
            self.obsY1.append(car)
            self.obsY2.append(greentime)

            if self.line1 is None:
                self.line1 = self.ax_1.plot(self.obsX, self.obsY1, '-g', marker='*')[0]
            if self.line2 is None:
                self.line2 = self.ax_1.plot(self.obsX, self.obsY2, '-r', marker='*')[0]

            self.line1.set_xdata(self.obsX)
            self.line1.set_ydata(self.obsY1)

            self.line2.set_xdata(self.obsX)
            self.line2.set_ydata(self.obsY2)
            if len(self.obsX)<10:
                min=self.obsX[0]
            else:
                min = self.obsX[len(self.obsX)-10]
            max=min+10
            self.ax_1.set_xlim([min,max])
            self.ax_1.set_ylim([0,60])

            plt.pause(0.1)
        else:
            self.obsX_2.append(time)
            self.obsY1_2.append(car)
            self.obsY2_2.append(greentime)

            if self.line1_2 is None:
                self.line1_2 = self.ax_2.plot(self.obsX_2, self.obsY1_2, '-g', marker='*')[0]
            if self.line2_2 is None:
                self.line2_2 = self.ax_2.plot(self.obsX_2, self.obsY2_2, '-r', marker='*')[0]

            self.line1_2.set_xdata(self.obsX_2)
            self.line1_2.set_ydata(self.obsY1_2)

            self.line2_2.set_xdata(self.obsX_2)
            self.line2_2.set_ydata(self.obsY2_2)
            if len(self.obsX_2) < 10:
                min = self.obsX_2[0]
            else:
                min = self.obsX_2[len(self.obsX_2) - 10]
            max = min + 10
            self.ax_2.set_xlim([min, max])
            self.ax_2.set_ylim([0, 60])

            plt.pause(0.1)

import random


if __name__ == '__main__':
    nsShow = StartShow()

    t0 = time.time()
    t1 = time.time()
    while True:
        t2 = time.time()-t0
        t3 = time.time() - t1
        if(random.randint(1,2)==1):
            nsShow.add_data(1,int(t2), random.randint(0,9) ,random.randint(0,40))
            nsShow.add_data(2, int(t2), random.randint(0, 9), random.randint(0, 40))
        else:
            nsShow.add_data(2, int(t3), random.randint(0, 9), random.randint(0, 40))
            nsShow.add_data(1, int(t3), random.randint(0, 9), random.randint(0, 40))
        time.sleep(2)
