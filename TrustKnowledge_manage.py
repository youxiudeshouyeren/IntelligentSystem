import config
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import datetime


# 查询所有数据
def TrustKnowledge_search():
    print('*****可信度知识库*****')
    cursor = config.connect.cursor()
    sql = '''select * from %s order by %s
        ''' % (config.TrustworthinessKnowledge.table_name,
               config.TrustworthinessKnowledge.id)
    res = cursor.execute(sql)

    sqldata = []
    # 成功取回数据则打印
    if (res):
        temp = cursor.rowcount
        print("产生式ID\t\t\t前提\t\t\t结论\t\t\t前提可信度\t\t\t结论可信度\t\t\t知识使用次数\t\t\t最后一次使用时间")
        for i in range(temp):
            cursor.scroll(i, mode="absolute")
            data = cursor.fetchone()
            sqldata.append(data)
            # print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s"%(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
    cursor.close()
    return sqldata


def TrustKnowledge_search_by_id(id_value):
    print('*****可信度知识库根据id*****')
    cursor = config.connect.cursor()
    print('连接')
    sql = 'a'
    print(sql)

    sql = '''select * from %s  where %s=%d''' % (config.TrustworthinessKnowledge.table_name,
                                                 config.TrustworthinessKnowledge.id,
                                                 int(id_value))

    res = cursor.execute(sql)
    # 成功取回数据则打印
    if (res):
        temp = cursor.rowcount
        print("产生式ID\t\t\t前提\t\t\t结论\t\t\t前提可信度\t\t\t结论可信度\t\t\t知识使用次数\t\t\t最后一次使用时间")
        for i in range(temp):
            cursor.scroll(i, mode="absolute")
            data = cursor.fetchone()

            # print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s"%(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
            return list(data)
    cursor.close()

#新增
def TrustKnowledge_add(precondition_value, conclusion_value, pre_probablity_value,
                       con_probablity_value, use_count_value, last_use_value):
    cursor = config.connect.cursor()
    print("*****增加可信度知识*****")

    sql = '''insert into %s (%s,%s,%s,%s,%s,%s)  
    values ('%s','%s',%f,%f,%d,'%s');
    ''' % (config.TrustworthinessKnowledge.table_name,
           config.TrustworthinessKnowledge.precondition,
           config.TrustworthinessKnowledge.conclusion,
           config.TrustworthinessKnowledge.pre_probability,
           config.TrustworthinessKnowledge.con_probability,
           config.TrustworthinessKnowledge.use_count,
           config.TrustworthinessKnowledge.last_use,
           precondition_value,
           conclusion_value,
           float(pre_probablity_value),
           float(con_probablity_value),
           int(use_count_value),
           last_use_value)
    print(sql)
    res = cursor.execute(sql)
    config.connect.commit()
    print("插入成功！" if res == True else "插入失败")
    cursor.close()
    return '1' if res == True else "0"

#删除数据
def TrustKnowledge_delete(id_value):


    cursor=config.connect.cursor()

    sql='''delete from %s where id="%s"
        '''%(config.TrustworthinessKnowledge.table_name,
             id_value)
    res= cursor.execute(sql)
    connect=config.connect
    connect.commit()
    cursor.close()

def TrustKnowledge_update(id_value,precondition_value, conclusion_value, pre_probablity_value,
                          con_probablity_value, use_count_value, last_use_value):
    cursor=config.connect.cursor()
  


    sql='''update %s set %s="%s",%s="%s",%s=%f,%s=%f,%s=%d,%s="%s" where %s=%d;
            '''%(config.TrustworthinessKnowledge.table_name,
                 config.TrustworthinessKnowledge.precondition,precondition_value,
                 config.TrustworthinessKnowledge.conclusion,  conclusion_value,
                 config.TrustworthinessKnowledge.pre_probability, float(pre_probablity_value),
                 config.TrustworthinessKnowledge.con_probability,float(con_probablity_value),
                 config.TrustworthinessKnowledge.use_count, int(use_count_value),
                 config.TrustworthinessKnowledge.last_use, last_use_value,
                 config.TrustworthinessKnowledge.id,int(id_value)
                 )
    res= cursor.execute(sql)
    connect=config.connect
    connect.commit()
    cursor.close()
    print("更新成功" if res else "更新失败")

# 通过id搜索的线程
class TrustKnowledge_search_by_id_thread(QThread):
    sinOut = pyqtSignal(list)

    def __init__(self, id):
        super().__init__()
        self.id = id
        print('初始化')

    def run(self):
        print('线程运行')
        data = TrustKnowledge_search_by_id(self.id)
        print(data)
        self.sinOut.emit(data)


# 新增数据的线程
class TrustKnowledge_add_thread(QThread):
    sinOut = pyqtSignal(list)

    def __init__(self, data):
        super().__init__()
        self.data = data
        print('初始化')

    def run(self):
        print('线程运行')
        TrustKnowledge_add(self.data[0], self.data[1],
                                 self.data[2], self.data[3], 
                                 self.data[4], self.data[5])
        res=TrustKnowledge_search()

        self.sinOut.emit(res)


# 删除数据的线程
class TrustKnowledge_delete_thread(QThread):
    sinOut = pyqtSignal(list)

    def __init__(self, id):
        super().__init__()
        self.id= id
        print('初始化')

    def run(self):
        print('线程运行')
        TrustKnowledge_delete(self.id)
        res=TrustKnowledge_search()

        self.sinOut.emit(res)


# 更新数据的线程
class TrustKnowledge_update_thread(QThread):
    sinOut = pyqtSignal(list)

    def __init__(self, data):
        super().__init__()
        self.data = data
        print('初始化')

    def run(self):
        print('线程运行')
        TrustKnowledge_update(self.data[0], self.data[1],
                           self.data[2], self.data[3],
                           self.data[4], self.data[5],
                           self.data[6])
        res=TrustKnowledge_search()

        self.sinOut.emit(res)