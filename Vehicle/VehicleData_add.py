# 车流量数据的增加
import datetime

import config
import random


type=0
#  0表示东-西方向
#  1表示西-东方向
#   2表示南-北方向
#   3表示北-南方向
vehicle_count=0  #车流量

# 参数分别为 方向类型、车流量、采集日期开始时间、采集日期结束时间
def vehicleData_add(type,vehicle_count,datetime_begin,datetime_end):
    cursor=config.connect.cursor()
    sql='''insert into %s (%s,%s,%s,%s)
    values (%d,'%s','%s',%d);
    '''%(config.VehicleData.tablename,
         config.VehicleData.type,
         config.VehicleData.begintime,
         config.VehicleData.endtime,
         config.VehicleData.vehiclecount,
         int(type),
         datetime_begin,
         datetime_end,
         vehicle_count )

    res=cursor.execute(sql)
    config.connect.commit()
    print("插入成功！" if res==True else "插入失败")



if __name__=='__main__':
    for i in range(10):
        type= (i % 2)
        vehicle_count=random.randint(0,20)

        # 当前时间提前一分钟
        begin_time=(datetime.datetime.now()-datetime.timedelta(minutes=1)).strftime(config.time_format)
        # 当前时间
        end_time=datetime.datetime.now().strftime(config.time_format)

        vehicleData_add(type,vehicle_count,begin_time,end_time)
