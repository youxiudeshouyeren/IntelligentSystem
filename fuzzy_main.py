import sys

sys.path.append('./LowerMachine')
sys.path.append('./Vehicle')

from LowerMachine import UpperMachine
from Vehicle import VehicleData_add
import FuzzyInfrerence
import TrustInfernce
import time
import datetime


def TheardMain():
    '''
    主线程，不断循环，完成传感器控制和推理机的控制
    '''

    # 先声明一个对象
    my_upper_machine = UpperMachine.UpperMachine()
    my_upper_machine.initial()
    my_upper_machine.start()

    STANDARD_SECONDS = 10
    MINI_SECONDS = 10
    MAX_SECONDS = 60

    while True:
        for i in range(2):
            # 获取等待时间
            wait_time = my_upper_machine.getTime(i)
            print("wait for %.3f seconds" % wait_time)
            # 等待对应时间
            time.sleep(wait_time)
            # 获取车辆数目并且添加到数据库中
            counts = my_upper_machine.getCount(i)
            beginTime, endTime = my_upper_machine.getBETime(i)
            VehicleData_add.vehicleData_add(i, counts, beginTime, endTime)
            # 南北1用模糊，东西0用可信度
            if i == 0:
                # 用可信度推理机进行推理
                conclusion = TrustInfernce.getConclusion(i)
                print(conclusion)

                # 根据结论对传感器进行修改
                # 暂时只用可信度结论进行修改
                if (conclusion[0] == "本轮绿灯时间不变"):
                    # do Nothing
                    print("")
                elif (conclusion[0] == "本轮绿灯时间增加"):
                    wait_time += wait_time * conclusion[1] * STANDARD_SECONDS
                    if wait_time > MAX_SECONDS:
                        wait_time = MAX_SECONDS
                elif conclusion[0] == "本轮绿灯时间减少":
                    wait_time -= wait_time * conclusion[1] * STANDARD_SECONDS
                    if wait_time < MINI_SECONDS:
                        wait_time = MINI_SECONDS
                else:
                    print("Error!")
            elif i == 1:
                # 用模糊推理机进行推理
                count1, count2 = FuzzyInfrerence.getCount(i)
                conclusion, fuzzy_train = FuzzyInfrerence.Defuzzification(i)
                # print(count1, count2)
                # print(fuzzy_train)
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

            my_upper_machine.changeTime(i, wait_time)

if __name__ == '__main__':
    TheardMain()




