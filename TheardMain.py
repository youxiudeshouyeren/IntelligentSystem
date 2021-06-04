import sys
sys.path.append('./LowerMachine')
sys.path.append('./Vehicle')

import UpperMachine
import VehicleData_add
import TrustInfernce
import time
import datetime

def TheardMain():
    '''
    主线程，不断循环，完成传感器控制和推理机的控制
    '''

    # 先声明一个对象
    my_upper_machine=UpperMachine.UpperMachine()
    my_upper_machine.initial()
    my_upper_machine.start()

    STANDARD_SECONDS=10
    MINI_SECONDS=4

    while True:
        for i in range(4):
            # 获取等待时间
            wait_time=my_upper_machine.getTime(i)
            print("wait for %.3f seconds" % wait_time)
            # 等待对应时间
            time.sleep(wait_time)
            # 获取车辆数目并且添加到数据库中
            counts=my_upper_machine.getCount(i)
            beginTime,endTime=my_upper_machine.getBETime(i)
            VehicleData_add.vehicleData_add(i+1,counts,beginTime,endTime)

            # 进行推理
            conclusion = TrustInfernce.getConclusion(i+1)
            print(conclusion)

            # 根据结论对传感器进行修改
            # 暂时只用可信度结论进行修改
            if(conclusion[0]=="本轮绿灯时间不变"):
                # do Nothing
                print("")
            elif (conclusion[0]=="本轮绿灯时间增加"):
                wait_time+=wait_time*conclusion[1]*STANDARD_SECONDS
            elif conclusion[0]=="本轮绿灯时间减少":
                wait_time-=wait_time*conclusion[1]*STANDARD_SECONDS
                if wait_time<MINI_SECONDS :
                    wait_time=MINI_SECONDS
            else:
                print("Error!")
            my_upper_machine.changeTime(i,wait_time)
            

if __name__ == '__main__':
    TheardMain()




