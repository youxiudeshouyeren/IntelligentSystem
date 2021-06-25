#车流量数据查询
#1.查询全部
#2.查询时间区间

# 查询全部
import sys
sys.path.append('..')
import config
from PyQt5.QtCore import *
import datetime
def StatisticalAnalysis_search_all():
    print('******统计分析数据*****')
    cursor=config.connect.cursor()
    sql='''select * from %s,%s where DATE_FORMAT(%s,'%s')=DATE_FORMAT(%s,'%s') and DATE_FORMAT(%s,'%s')=DATE_FORMAT(%s,'%s');
        '''%(config.VehicleData.tablename,config.ControlData.tablename,
             config.VehicleData.tablename+".beginTime",config.time_format,config.ControlData.tablename+".beginTime",config.time_format,
             config.VehicleData.tablename+".endTime",config.time_format,config.ControlData.tablename+".endTime",config.time_format) #倒序查询 保证新数据再最上面
    print(sql)
    res= cursor.execute(sql)
    data_temp=[]
    #成功取回数据则打印
    if(res):
        temp=cursor.rowcount
        for i in range(temp):
            cursor.scroll(i, mode="absolute")
            data = cursor.fetchone()
            data_temp.append([data[1],data[2],data[3],data[4],data[6],data[7],data[8],data[9]])
            print(data)
    return data_temp
    cursor.close()


# 查询时间区段
def StatisticalAnalysis_search_by_time(interval,beginTime,endTime):
    print('*****统计分析时间区段查询*****')
    left=beginTime
    right=endTime
    cursor=config.connect.cursor()
    while datetime.datetime.strptime(left, '%Y-%m-%d %H:%M:%S')<datetime.datetime.strptime(right, '%Y-%m-%d %H:%M:%S'):
        sql='''select * from %s,%s   where DATE_FORMAT(%s,'%s')=DATE_FORMAT(%s,'%s') and DATE_FORMAT(%s,'%s')=DATE_FORMAT(%s,'%s') and DATE_FORMAT( %s,'%s') >= DATE_FORMAT ('%s','%s') and DATE_FORMAT (%s,'%s') <= DATE_FORMAT ('%s','%s') order by %s desc;
            '''%(config.VehicleData.tablename,config.ControlData.tablename,
                 config.VehicleData.tablename+".beginTime",config.time_format,config.ControlData.tablename+".beginTime",config.time_format,
                 config.VehicleData.tablename+".endTime",config.time_format,config.ControlData.tablename+".endTime",config.time_format,
                 config.VehicleData.tablename+".beginTime",
                 config.time_format,
                 left,
                 config.time_format,
                 config.VehicleData.tablename+".endTime",
                 config.time_format,
                 right,
                 config.time_format,
                 config.VehicleData.tablename+".beginTime") #倒序查询 保证新数据再最上面
        print(sql)
        data_temp = []
        res= cursor.execute(sql)
        dateTime_p = datetime.datetime.strptime(left,'%Y-%m-%d %H:%M:%S')
        timedelta = datetime.timedelta(days=0, seconds=interval, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
        left=str(dateTime_p+timedelta)
        print("left")
        print(left)

    #成功取回数据则打印
        if(res):
            temp=cursor.rowcount
            for i in range(temp):
                cursor.scroll(i, mode="absolute")
                data = cursor.fetchone()
                print(data)
                data_temp.append([data[1], data[2], data[3], data[4], data[6], data[7], data[8], data[9]])
                print('data_temp')
                print(data_temp)
                #id type beginTime endTime vehicleCount
                #id light_1 light_2 light_3 light_4 beginTime endTime

    return data_temp
    cursor.close()


# 更新数据的线程
class StatisticalAnalysis_search_by_time_thread(QThread):
    sinOut = pyqtSignal(list)

    def __init__(self, interval,beginTime, endTime):
        super().__init__()
        self.interval=interval
        self.beginTime = beginTime
        self.endTime = endTime
        print('初始化')

    def run(self):
        print('线程运行')
        res = StatisticalAnalysis_search_by_time(self.interval,self.beginTime, self.endTime)
        self.sinOut.emit(res)

# 更新数据的线程
class StatisticalAnalysis_search_all_thread(QThread):
    sinOut = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        print('初始化')

    def run(self):
        print('线程运行')
        res=StatisticalAnalysis_search_all()
        self.sinOut.emit(res)

if __name__=='__main__':
    #StatisticalAnalysis_search_all()
    StatisticalAnalysis_search_by_time(59,'2021-06-04 15:33:38','2021-06-04 15:34:39')