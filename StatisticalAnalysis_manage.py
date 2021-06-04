#车流量数据查询
#1.查询全部
#2.查询时间区间

# 查询全部
import sys
sys.path.append('..')
import config


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
def StatisticalAnalysis_search_by_time(beginTime,endTime):
    print('*****统计分析时间区段查询*****')
    cursor=config.connect.cursor()
    sql='''select * from %s,%s   where DATE_FORMAT(%s,'%s')=DATE_FORMAT(%s,'%s') and DATE_FORMAT(%s,'%s')=DATE_FORMAT(%s,'%s') and DATE_FORMAT( %s,'%s') >= DATE_FORMAT ('%s','%s') and DATE_FORMAT (%s,'%s') <= DATE_FORMAT ('%s','%s') order by %s desc;
        '''%(config.VehicleData.tablename,config.ControlData.tablename,
             config.VehicleData.tablename+".beginTime",config.time_format,config.ControlData.tablename+".beginTime",config.time_format,
             config.VehicleData.tablename+".endTime",config.time_format,config.ControlData.tablename+".endTime",config.time_format,
             config.VehicleData.tablename+".beginTime",
             config.time_format,
             beginTime,
             config.time_format,
             config.VehicleData.tablename+".endTime",
             config.time_format,
             endTime,
             config.time_format,
             config.VehicleData.tablename+".beginTime") #倒序查询 保证新数据再最上面
    print(sql)
    data_temp = []
    res= cursor.execute(sql)
    #成功取回数据则打印
    if(res):
        temp=cursor.rowcount
        for i in range(temp):
            cursor.scroll(i, mode="absolute")
            data = cursor.fetchone()
            print(data)
            data_temp.append([data[1], data[2], data[3], data[4], data[6], data[7], data[8], data[9]])
            #id type beginTime endTime vehicleCount
            #id light_1 light_2 light_3 light_4 beginTime endTime
    return data_temp
    cursor.close()

if __name__=='__main__':
    StatisticalAnalysis_search_all()
    StatisticalAnalysis_search_by_time('2019-05-20 20:00:00','2022-05-02 20:01:02')