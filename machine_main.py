import sys
sys.path.append('./LowerMachine')
sys.path.append('./Vehicle')
sys.path.append('./DataControl')

# import TheardMain
# import fuzzy_main
from DataControl import ControlData_add
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from LowerMachine import UpperMachine
from  Vehicle import  VehicleData_add
import TrustInfernce
import FuzzyInfrerence
import time
import datetime






class Machine_thread(QThread):
    sinOut = pyqtSignal(list)


    #ew是东西方向的推理机  sn是南北方向的推理机
    def __init__(self,ew,sn,port,mintime,maxtime,dataSourse):
        super().__init__()
        self.ew=ew
        self.sn=sn
        self.port=port
        self.mintime=int(mintime)
        self.maxtime=int(maxtime)
        self.dataSourse=dataSourse
        print('推理机初始化')
        print(self.ew)


    def run(self):
        

        my_upper_machine=UpperMachine.UpperMachine(self.dataSourse)

        my_upper_machine.serialPort=self.port
        my_upper_machine.initial()
        my_upper_machine.start()

        STANDARD_SECONDS = 10
        MINI_SECONDS = self.mintime
        MAX_SECONDS = self.maxtime
        while True:
           
            for i in range(2):
                ########################
                data=[]
                wait_time=my_upper_machine.getTime(i)
                print("wait for %.3f seconds" % wait_time)
                # 等待对应时间
                time.sleep(wait_time+2)
                # 获取车辆数目并且添加到数据库中
                counts=my_upper_machine.getCount(i)
                beginTime,endTime=my_upper_machine.getBETime(i)
                VehicleData_add.vehicleData_add(i,counts,beginTime,endTime)
                data.append(str(i))
                data.append(str(counts))
                data.append(str(beginTime))
                data.append(str(endTime))
                # print(data)

                if(i==0):
                    ControlData_add.ControlData_add(0,0,2,2,beginTime,endTime)
                else:
                    ControlData_add.ControlData_add(2,2,0,0,beginTime,endTime)

                #南北1用模糊，东西0用可信度
                print(self.ew)
                print(self.sn)
                if((i==0 and self.ew=="可信度") or (i==1 and self.sn=="可信度")):
                    # 用可信度推理机进行推理
                    # print('nnnnnnn')
                    conclusion = TrustInfernce.getConclusion(i+1)
                    print(conclusion)
                    if (conclusion[0] == "本轮绿灯时间不变"):
                        # do Nothing
                        print("")
                    elif (conclusion[0] == "本轮绿灯时间增加"):
                        wait_time += conclusion[1] * STANDARD_SECONDS
                        if wait_time > MAX_SECONDS:
                            wait_time = MAX_SECONDS
                    elif conclusion[0] == "本轮绿灯时间减少":
                        wait_time -= conclusion[1] * STANDARD_SECONDS
                        if wait_time < MINI_SECONDS:
                            wait_time = MINI_SECONDS

                    else:
                        print("Error!")

                    process_data=TrustInfernce.getInferenceChain()
                    data.append(str(process_data))

                    print(data)

                elif((i==0 and self.ew=="模糊") or (i==1 and self.sn=="模糊")):
                    
                    # 用模糊推理机进行推理
                    print('进入模糊')
                    count1, count2 = FuzzyInfrerence.getCount(i)
                    conclusion, fuzzy_train = FuzzyInfrerence.Defuzzification(i)
                    # print(count1, count2)
                    # print(fuzzy_train)
                    fuzzy_train=[ str(i)+'\n'  for i in fuzzy_train ]
                    data.append(' '.join(fuzzy_train))
                    print(fuzzy_train)
                    for th in fuzzy_train:
                        print(th)
                    if (count1 == count2):
                        wait_time = wait_time
                        pass
                    elif (count1 < count2):
                        wait_time -= conclusion
                        # print('绿灯时长减少{}秒'.format(conclusion))
                        if wait_time < MINI_SECONDS:
                            wait_time = MINI_SECONDS
                    elif (count1 > count2):
                        wait_time += conclusion
                        # print('绿灯时长增加{}秒'.format(conclusion))
                        if wait_time > MAX_SECONDS:
                            wait_time = MAX_SECONDS
                data.append(str(wait_time))
                my_upper_machine.changeTime(i,wait_time)
                print('测试响应结果')
                print(data)
                self.sinOut.emit(data)

