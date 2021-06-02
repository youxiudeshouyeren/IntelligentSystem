#车流量数据查询
#1.查询全部
#2.查询时间区间

# 查询全部
import config


def vehicleData_search_all():
    print('******全部车流量数据*****')
    cursor=config.connect.cursor()
    sql='''select * from %s order by %s desc;
        '''%(config.VehicleData.tablename,
             config.VehicleData.id) #倒序查询 保证新数据再最上面
    res= cursor.execute(sql)
    #成功取回数据则打印
    if(res):
        temp=cursor.rowcount
        print("ID\t\t\t方向类型\t\t\t车流量\t\t\t起始时间\t\t\t结束时间")
        for i in range(temp):
            cursor.scroll(i, mode="absolute")
            data = cursor.fetchone()
            print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t%s"%(data[0],data[1],data[4],data[2],data[3]))
    cursor.close()


# 查询时间区段
def vehicleData_search_by_time(beginTime,endTime):
    print('*****时间区段查询*****')
    cursor=config.connect.cursor()
    #DATE_FORMAT( 时间的字段名, '%Y-%m-%d' ) <= DATE_FORMAT( 时间, '%Y-%m-%d' )
    sql='''select * from %s  where DATE_FORMAT( %s,'%s') >= DATE_FORMAT ('%s','%s') and DATE_FORMAT (%s,'%s') <= DATE_FORMAT ('%s','%s') order by %s desc;
        '''%(config.VehicleData.tablename,

             config.VehicleData.begintime,
             config.time_format,
             beginTime,
             config.time_format,
             config.VehicleData.endtime,
             config.time_format,
             endTime,
             config.time_format,
             config.VehicleData.id,) #倒序查询 保证新数据再最上面
   # print(sql)
    res= cursor.execute(sql)
    #成功取回数据则打印
    if(res):
        temp=cursor.rowcount
        print("ID\t\t\t方向类型\t\t\t车流量\t\t\t起始时间\t\t\t结束时间")
        for i in range(temp):
            cursor.scroll(i, mode="absolute")
            data = cursor.fetchone()
            print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t%s"%(data[0],data[1],data[4],data[2],data[3]))
    cursor.close()

if __name__=='__main__':
    vehicleData_search_all()
    vehicleData_search_by_time('2021-05-20 20:00:00','2021-05-02 20:01:02')