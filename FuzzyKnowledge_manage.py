import config
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import datetime


# 查询所有数据
def FuzzyKnowledge_search():
    print('*****模糊知识库search*****')
    cursor = config.connect.cursor()
    sql = '''select * from %s order by %s
            ''' % (config.fuzzyKnowledge.table_name,
                   config.fuzzyKnowledge.id)
    print(sql)
    try:
        res = cursor.execute(sql)
    except :
        s = sys.exc_info()
        print("Error: ")
        print(s )
    sqldata = []
    # 成功取回数据则打印

    if (res):
        print("res")
        temp = cursor.rowcount
        print("模糊知识ID\t\t\t模糊集Aid\t\t\t模糊集Aid\t\t\t模糊集Cid\t\t\t模糊矩阵id\t\t\t前提可信度\t\t\t结论可信度\t\t\t更新时间\t\t\t使用次数")
        for i in range(temp):
            cursor.scroll(i, mode="absolute")
            data = cursor.fetchone()
            print("%s\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t%s\t\t%s" % (
            data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[9]))
            sqldata.append([data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[9]])
    cursor.close()
    print("模糊知识库search完成")
    return sqldata


def FuzzyKnowledge_search_by_id(id_value):
    print('*****模糊知识库*****')
    cursor = config.connect.cursor()

    sql = '''select * from %s  where %s=%d''' % (config.fuzzyKnowledge.table_name,
                                                 config.fuzzyKnowledge.id,
                                                 int(id_value))
    data=[]
    res = cursor.execute(sql)
    # 成功取回数据则打印
    if (res):
        temp = cursor.rowcount
        print("模糊知识ID\t\t\t模糊集Aid\t\t\t模糊集Aid\t\t\t模糊集Cid\t\t\t模糊矩阵id\t\t\t前提可信度\t\t\t结论可信度\t\t\t更新时间\t\t\t使用次数")
        for i in range(temp):
            cursor.scroll(i, mode="absolute")
            data = cursor.fetchone()
            print("%s\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t%s\t\t%s" % (
                data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[9]))
            return list(data)
    cursor.close()
    return list(data)

# 新增
def FuzzyKnowledge_add(precondition_a, precondition_b, conclusion_c,fuzzyMatrixId,pre_probablity_value,con_probablity_value):
    cursor = config.connect.cursor()
    print("*****增加模糊知识库*****")

    use_count_value = 0
    updateTime = datetime.datetime.now().strftime(config.time_format)

    sql = '''insert into %s (%s,%s,%s,%s,%s,%s,%s,%s)  
        values ('%d','%d',%d,%d,%f,'%f','%d','%s')
        ''' % (config.fuzzyKnowledge.table_name,
               config.fuzzyKnowledge.Aid,
               config.fuzzyKnowledge.Bid,
               config.fuzzyKnowledge.Cid,
               config.fuzzyKnowledge.fuzzyMatrixId,
               config.fuzzyKnowledge.pre_probability,
               config.fuzzyKnowledge.con_probability,
               config.fuzzyKnowledge.use_count,
               config.fuzzyKnowledge.updateTime,
               int(precondition_a),
               int(precondition_b),
               int(conclusion_c),
               int(fuzzyMatrixId),
               float(pre_probablity_value),
               float(con_probablity_value),
               int(use_count_value),
               updateTime
               )
    print(sql)
    res = cursor.execute(sql)
    config.connect.commit()
    print("插入成功！" if res == True else "插入失败")
    cursor.close()
    # config.connect.close()


# 删除数据
def FuzzyKnowledge_delete(id_value):
    FuzzyKnowledge_search()
    cursor = config.connect.cursor()
    sql = '''delete from %s where id="%s"
               ''' % (config.fuzzyKnowledge.table_name,
                      id_value)
    res = cursor.execute(sql)
    connect = config.connect
    connect.commit()
    cursor.close()
    print("删除成功" if res else "删除失败")


def FuzzyKnowledge_update(id_value, precondition_a, precondition_b, conclusion_c,fuzzyMatrixId,pre_probablity_value,con_probablity_value):
    cursor = config.connect.cursor()
    use_count_value = 0
    last_use_value = datetime.datetime.now().strftime(config.time_format)

    sql = '''update %s set %s="%d",%s="%d",%s=%d,%s=%d,%s=%f,%s="%f",%s="%d",%s="%s" where %s=%d;
                ''' % (config.fuzzyKnowledge.table_name,
                       config.fuzzyKnowledge.Aid, int(precondition_a),
                       config.fuzzyKnowledge.Bid, int(precondition_b),
                       config.fuzzyKnowledge.Cid, int(conclusion_c),
                       config.fuzzyKnowledge.fuzzyMatrixId, int(fuzzyMatrixId),
                       config.fuzzyKnowledge.pre_probability, float(pre_probablity_value),
                       config.fuzzyKnowledge.con_probability, float(con_probablity_value),
                       config.fuzzyKnowledge.use_count, int(use_count_value),
                       config.fuzzyKnowledge.last_use, last_use_value,
                       config.fuzzyKnowledge.id, int(id_value)
                       )
    res = cursor.execute(sql)
    connect = config.connect
    connect.commit()
    cursor.close()
    print("更新成功" if res else "更新失败")


# 通过id搜索的线程
class FuzzyKnowledge_search_by_id_thread(QThread):
    sinOut = pyqtSignal(list)

    def __init__(self, id):
        super().__init__()
        self.id = id
        print('初始化')

    def run(self):
        print('线程运行')
        data = FuzzyKnowledge_search_by_id(self.id)
        print(data)
        self.sinOut.emit(data)


# 新增数据的线程
class FuzzyKnowledge_add_thread(QThread):
    sinOut = pyqtSignal(list)

    def __init__(self, data):
        super().__init__()
        self.data = data
        print('初始化')

    def run(self):
        print('线程运行')
        FuzzyKnowledge_add(self.data[0], self.data[1],
                           self.data[2], self.data[3],
                           self.data[4], self.data[5])
        res = FuzzyKnowledge_search()
        print("FuzzyKnowledge_search() 结束")
        self.sinOut.emit(res)


# 删除数据的线程
class FuzzyKnowledge_delete_thread(QThread):
    sinOut = pyqtSignal(list)

    def __init__(self, id):
        super().__init__()
        self.id = id
        print('初始化')

    def run(self):
        print('线程运行')
        FuzzyKnowledge_delete(self.id)
        res = FuzzyKnowledge_search()

        self.sinOut.emit(res)


# 更新数据的线程
class FuzzyKnowledge_update_thread(QThread):
    sinOut = pyqtSignal(list)

    def __init__(self, data):
        super().__init__()
        self.data = data
        print('初始化')

    def run(self):
        print('线程运行')
        FuzzyKnowledge_update(self.data[0], self.data[1],
                              self.data[2], self.data[3],
                              self.data[4], self.data[5],
                              self.data[6])
        res = FuzzyKnowledge_search()

        self.sinOut.emit(res)