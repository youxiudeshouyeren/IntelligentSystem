import UpperMachine
import time
if __name__ == '__main__':

    # 要先像下面这样声明一个对象并运行
    my_upper_machine=UpperMachine.UpperMachine()
    my_upper_machine.initial()
    my_upper_machine.start()

    # 如果想改一个路口的绿灯时间，使用changeTime()函数
    cross1_time=5
    my_upper_machine.changeTime(0,cross1_time)
    # 如果想获得一个路口经过的车辆数目，使用getCount函数
    time.sleep(5)
    cross1_num=my_upper_machine.getCount(0)
    beginTime,endTime=my_upper_machine.getBETime(0)
    print("经过路口1的时间为%d " % cross1_num)
    print("经过时间，开始：%s    结束：%s" % (beginTime,endTime) )
    time.sleep(100)