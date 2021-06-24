#!
# -*- coding: utf-8 -*-

"""
这是一个类，用以实现与下位机沟通交流，并且屏蔽细节。
详情用法请看底下的main函数

"""

import sys
sys.path.append('..')
import _thread
import config
import datetime
import time
import serial

vehicleCount=0 #全局变量 用于实时刷新


class UpperMachine():
    """"""

    def __init__(self):



        # 按东南西北的顺序
        # 各个方向的车辆数目

        self.count1 = 0
        self.count2 = 0
        self.count3 = 0
        self.count4 = 0

        self.beginTime1=datetime.datetime.now().strftime(config.time_format)
        self.endTime1=datetime.datetime.now().strftime(config.time_format)
        self.beginTime2=datetime.datetime.now().strftime(config.time_format)
        self.endTime2=datetime.datetime.now().strftime(config.time_format)
        self.beginTime3=datetime.datetime.now().strftime(config.time_format)
        self.endTime3=datetime.datetime.now().strftime(config.time_format)
        self.beginTime4=datetime.datetime.now().strftime(config.time_format)
        self.endTime4=datetime.datetime.now().strftime(config.time_format)

        # 各个方向的通行时间
        self.green1_time = 10
        self.green2_time = 10
        self.green3_time = 10
        self.green4_time = 10

        # 用以判断是否更新过数据
        # 如果为真，那么表示数据为最新
        # 使用者应当在读取完数据调用函数将此变回False
        self.flag=False

        # 串口号
        self.serialPort="COM6"

        #波特率
        self.baudRate=9600

        self.ser=None

    def initial(self):

        self.ser=serial.Serial(self.serialPort, self.baudRate) # 连接串口

    def SentMessage(self):
        global  vehicleCount
        accept_nums=[1,2,3,4]
        yellow_list=[5,6,7,8]
        while True :
            # 发数据
            # 绿黄红
            for i in range(2):
                time_start = time.time()
                beginTime=datetime.datetime.now().strftime(config.time_format)
                temp_num=0
                str_last = 'YES\n'
                str1 = ''
                # 进行计数
                while (time.time() - time_start) < self.getTime(i):
                    self.ser.write(accept_nums[i].to_bytes(length=1, byteorder='big', signed=True))  # 持续发送信息
                    str1 = self.ser.readline()
                    # print('south_north '+str(str1))
                    if (str1 == b'YES\n'):
                        if str_last != str1:  # 有障碍物
                            temp_num += 1  # 障碍物加一
                            vehicleCount=temp_num # 获取实时车辆数据
                    str_last = str1

                endTime=datetime.datetime.now().strftime(config.time_format)
                self.changeBETime(i,beginTime,endTime)
                time_start = time.time()
                while(time.time() - time_start)<2:
                    self.ser.write(yellow_list[i].to_bytes(length=1, byteorder='big', signed=True))
                    str1 = self.ser.readline()
                self.changeCount(i,temp_num)
                print("index: %d  the number of cars: %d" % (i+1,self.getCount(i)) )

    def changeBETime(self,i,beginTime,endTime):
        if(i==0):
            self.beginTime1=beginTime
            self.endTime1=endTime
        elif(i==1):
            self.beginTime2=beginTime
            self.endTime2=endTime
        elif(i==2):
            self.beginTime3=beginTime
            self.endTime3=endTime
        else:
            self.beginTime4=beginTime
            self.endTime4=endTime
    
    def getBETime(self,i):
        '''
        返回开始时间和结束时间
        i的范围是[0-3]
        '''

        if(i==0):
            return self.beginTime1,self.endTime1
        elif(i==1):
            return self.beginTime2,self.endTime2
        elif(i==2):
            return self.beginTime3,self.endTime3
        else:
            return self.beginTime4,self.endTime4
    
    def changeCount(self,i,num):
        if(i==0):
            self.count1=num
        elif(i==1):
            self.count2 = num
        elif (i == 2):
            self.count3 = num
        else:
            self.count4 = num

    def getTime(self,i):
        '''
        获得路口经过车辆的函数
        i从0开始，0-3代表4个路口
        '''
        if (i == 0):
            return self.green1_time
        elif (i == 1):
            return self.green2_time
        elif (i == 2):
            return self.green3_time
        else:
            return self.green4_time

    def getCount(self,i):
        if (i == 0):
            return self.count1
        elif (i == 1):
            return self.count2
        elif (i == 2):
            return self.count3
        else:
            return self.count4

    def changeTime(self,i,time):
        '''
        改变路口绿灯时间的函数
        i从0开始，0-3代表4个路口
        '''
        if(i==0):
            self.green1_time=time
        elif (i == 1):
            self.green2_time = time
        elif (i == 2):
            self.green3_time = time
        else:
            self.green4_time = time

    def start(self):
        _thread.start_new_thread(self.SentMessage,())



if __name__ == '__main__':

    my_upper_machine=UpperMachine()
    my_upper_machine.initial()
    my_upper_machine.start()




