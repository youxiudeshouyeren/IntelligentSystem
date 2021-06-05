# 控制信息数据的增加
import datetime

import config
import random




# 参数分别为 东-西方向灯类型 西-东方向 南北方向 北南方向 起始时间 结束时间
def ControlData_add(light_1,light_2,light_3,light_4,datetime_begin,datetime_end):
    cursor=config.connect.cursor()
    sql='''insert into %s (%s,%s,%s,%s,%s,%s)
    values (%d,%d,%d,%d,'%s','%s');
    '''%(config.ControlData.tablename,
         config.ControlData.light_1,
         config.ControlData.light_2,
         config.ControlData.light_3,
         config.ControlData.light_4,
         config.ControlData.begintime,
         config.ControlData.endtime,
         int(light_1),
         int(light_2),
         int(light_3) ,
         int(light_4),
         datetime_begin,
         datetime_end)

    res=cursor.execute(sql)
    config.connect.commit()
    print("插入成功！" if res==True else "插入失败")



if __name__=='__main__':
    
    #10条随机数据测试
    for i in range(10):
        light_1=random.randint(0,2)
        light_2=light_1
        light_3 = random.randint(0, 2)
        light_4 = light_3
        
        seconds=random.randint(10,60) #模拟秒数
        minutes=random.randint(10,60)#随机分钟数
        # 当前时间提前一分钟
        begin_time=(datetime.datetime.now()-datetime.timedelta(minutes=minutes)).strftime(config.time_format)
        # 当前时间
        end_time=(datetime.datetime.now()+datetime.timedelta(seconds=seconds)).strftime(config.time_format)

        ControlData_add(light_1,light_2,light_3,light_4,begin_time,end_time)
