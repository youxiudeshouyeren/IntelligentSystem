# 车流量数据的删除
# 1.全部删除
# 2.时间段删除

# 删除全部车流量数据 请谨慎操作！！
import config


def vehicleData_delete_all():
    temp=input('删除全部车流量数据，输入 yes 确认')
    if(temp!='yes'):
        return

    cursor=config.connect.cursor()
    sql='''delete from %s 
        '''%(config.VehicleData.tablename
            )
    res= cursor.execute(sql)
    connect=config.connect
    connect.commit()
    cursor.close()
    print("删除成功" if res else "删除失败")

def vehicleData_delete_by_time(beginTime,endTime):
    cursor=config.connect.cursor()
    sql='''delete from %s   where DATE_FORMAT( %s,'%s') >= DATE_FORMAT ('%s','%s') and DATE_FORMAT (%s,'%s') <= DATE_FORMAT ('%s','%s')
            '''%(config.VehicleData.tablename,
                 config.VehicleData.begintime,
                 config.time_format,
                 beginTime,
                 config.time_format,
                 config.VehicleData.endtime,
                 config.time_format,
                 endTime,
                 config.time_format,
                 )
    res= cursor.execute(sql)
    connect=config.connect
    connect.commit()
    cursor.close()
    print("删除成功" if res else "删除失败")


if __name__=='__main__':
    # vehicleData_delete_by_time('2021-05-20 20:00:00','2021-05-02 20:01:02')
    vehicleData_delete_all()
