import pymysql.cursors
import datetime
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# 连接数据库
connect = pymysql.Connect(
    # host='114.55.95.14',
    # port=3306,
    # user='user',
    # passwd='123456',
    # db='knowledge',
    # charset='utf8'
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='intelligent',
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


#车流量数据表 存储下位机的信息
class VehicleData:
    id='id'
    tablename='vehicleData'
    type='type'
    begintime='beginTime'
    endtime='endTime'
    vehiclecount='vehicleCount'

#控制信息表 存储上位机发送的信息
class ControlData:
    id='id'
    tablename='controlData'
    #东-西方向灯类型 西-东方向 南北方向 北南方向
    # 0 1 2分别代表红黄绿
    light_1='light_1'
    light_2='light_2'
    light_3='light_3'
    light_4='light_4'
    begintime='beginTime'
    endtime='endTime'

class fuzzyKnowledge:
    table_name = 'fuzzyKnowledge'
    id = 'id'
    Aid = 'Aid'
    Bid = 'Bid'
    Cid = 'Cid'
    fuzzyMatrixId = 'fuzzyMatrixId'
    pre_probability = 'pre_probability'
    con_probability = 'con_probability'
    updateTime = 'updateTime'
    whoUpdate = 'whoUpdate'
    use_count = 'use_count'
    last_use = 'last_use'

class allFuzzyMatrix:
    table_name = 'allFuzzyMatrix'
    matrixID = 'fuzzyMatrixID'
    row = 'row'
    col = 'col'
    value = 'value'

class fuzzySet:
    table_name = 'fuzzySet'
    id="id"
    fuzzySetId="fuzzySetId"
    elementId="elementId"
    pointOrline="pointOrline"
    leftBound="leftBound"
    rightBound="rightBound"
    belong="belong"
    updateTime="updateTime"
    whoUpdate="whoUpdate"










