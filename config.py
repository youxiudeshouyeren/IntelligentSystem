import pymysql.cursors
import datetime

# 连接数据库
connect = pymysql.Connect(
    host='114.55.95.14',
    port=3306,
    user='user',
    passwd='123456',
    db='knowledge',
    charset='utf8'
)


time_format='%Y-%m-%d %H:%M:%S' #日期格式

#可信度知识库
class TrustworthinessKnowledge:
    table_name='TrustworthinessKnowledge'
    id='id'
    precondition='precondition'
    conclusion='conclusion'
    pre_probability='pre_probability'
    con_probability='con_probability'
    use_count='use_count'
    last_use='last_use'


#车流量数据表
class VehicleData:
    tablename='vehicleData'
    type='type'
    begintime='beginTime'
    endtime='endTime'
    vehiclecount='vehicleCount'
