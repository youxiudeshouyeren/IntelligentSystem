import sys
sys.path.append('./LowerMachine')
sys.path.append('./Vehicle')

from LowerMachine import UpperMachine
from Vehicle import VehicleData_add
import TrustInfernce
import FuzzyInfrerence
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
            #南北34用模糊，东西12用可信度
            if i in [1,2]:
                # 用可信度推理机进行推理
                conclusion = TrustInfernce.getConclusion(i+1)
                print(conclusion)
                # 根据结论对传感器进行修改
                # 暂时只用可信度结论进行修改
                if (conclusion[0] == "本轮绿灯时间不变"):
                    # do Nothing
                    print("")
                elif (conclusion[0] == "本轮绿灯时间增加"):
                    wait_time += wait_time * conclusion[1] * 4
                elif conclusion[0] == "本轮绿灯时间减少":
                    wait_time -= wait_time * conclusion[1]
                else:
                    print("Error!")
            elif i in [3,4]:
                # 用模糊推理机进行推理
                count1, count2 = FuzzyInfrerence.getCount(i)
                print(count1, count2)
                if (count1 == count2):
                    print('本轮绿灯时间不变')
                elif (count1 < count2):
                    conclusion = FuzzyInfrerence.Defuzzification()
                    wait_time -=conclusion
                    print('绿灯时长减少{}秒'.format(conclusion))
                elif (count1 > count2):
                    conclusion = FuzzyInfrerence.Defuzzification()
                    wait_time += conclusion
                    print('绿灯时长增加{}秒'.format(conclusion))

            my_upper_machine.changeTime(i,wait_time)
            

if __name__ == '__main__':
    TheardMain()




