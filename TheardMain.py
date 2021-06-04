import sys
sys.path.append('./LowerMachine')
sys.path.append('./Vehicle')
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from LowerMachine import UpperMachine
from  Vehicle import  VehicleData_add
import TrustInfernce
import time
import datetime

class TheardMain_thread(QThread):
    sinOut = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def run(self):


        '''
        主线程，不断循环，完成传感器控制和推理机的控制
        '''
        data=[]
        # 先声明一个对象
        my_upper_machine=UpperMachine.UpperMachine()
        my_upper_machine.initial()
        my_upper_machine.start()

        while True:

            for i in range(4):
                data=[]
                # 获取等待时间
                wait_time=my_upper_machine.getTime(i)
                print("wait for %.3f seconds" % wait_time)
                # 等待对应时间
                time.sleep(wait_time)
                # 获取车辆数目并且添加到数据库中
                counts=my_upper_machine.getCount(i)
                beginTime,endTime=my_upper_machine.getBETime(i)
                #添加数据
                data.extend([str(i+1),str(counts),str(beginTime),str(endTime)])
                VehicleData_add.vehicleData_add(i+1,counts,beginTime,endTime)

                # 进行推理
                conclusion = TrustInfernce.getConclusion(i+1)
                print(conclusion)
                #添加数据

                data.append(TrustInfernce.factData)
                TrustInfernce.factData=[]#清空
                # 根据结论对传感器进行修改
                # 暂时只用可信度结论进行修改
                if(conclusion[0]=="本轮绿灯时间不变"):
                    # do Nothing
                    print("")
                elif (conclusion[0]=="本轮绿灯时间增加"):
                    wait_time+=wait_time*conclusion[1]*4
                elif conclusion[0]=="本轮绿灯时间减少":
                    wait_time-=wait_time*conclusion[1]
                else:
                    print("Error!")
                data.append(str(wait_time))
                my_upper_machine.changeTime(i,wait_time)
                self.sinOut.emit(data)




        
        
# if __name__ == '__main__':
#     TheardMain()
#



