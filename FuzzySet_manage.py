import config
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import datetime

#模糊集查询
def fuzzySet_search():
    print('*****模糊知识库的模糊知识表*****')
    cursor=config.connect.cursor()
    sql='''select * from %s order by %s
        '''%(config.fuzzySet.table_name,
             config.fuzzySet.id)
    res= cursor.execute(sql)
    sqldata=[]
    #成功取回数据则打印
    if(res):
        temp=cursor.rowcount
        print("模糊集ID\t\t\t\t元素ID\t\t\t\t点段标识\t\t\t\t左边界\t\t\t\t右边界\t\t\t\t隶属度\t\t\t\t更新时间")
        for i in range(temp):

            cursor.scroll(i, mode="absolute")
            data = cursor.fetchone()
            sqldata.append(list(data))
            print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s"%(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
    cursor.close()
    return sqldata

#根据ID查询
def fuzzySet_search_by_id(id_value):
    print('根据id查询')
    print('*****模糊知识库的模糊知识表*****')
    cursor=config.connect.cursor()
    sql='''select * from %s where %s=%d
        '''%(config.fuzzySet.table_name,
             config.fuzzySet.id,
             int(id_value))
    print(sql)
    res= cursor.execute(sql)
    
    #成功取回数据则打印
    if(res):
        temp=cursor.rowcount
        print("模糊集ID\t\t\t\t元素ID\t\t\t\t点段标识\t\t\t\t左边界\t\t\t\t右边界\t\t\t\t隶属度\t\t\t\t更新时间")
        for i in range(temp):

            cursor.scroll(i, mode="absolute")
            data = cursor.fetchone()
            return list(data)
            print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s"%(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
    cursor.close()
    

#模糊集添加函数
def fuzzy_set_add(fuzzySetId,elementId,pointOrline,leftBound,rightBound,belong):
    cursor=config.connect.cursor()
    updateTime = datetime.datetime.now().strftime(config.time_format)
    sql = '''insert into %s (%s,%s,%s,%s,%s,%s,%s)
    values ('%d','%d', %d, %d, %d,'%f','%s')
    '''%(config.fuzzySet.table_name,
         config.fuzzySet.fuzzySetId,
         config.fuzzySet.elementId,
         config.fuzzySet.pointOrline,
         config.fuzzySet.leftBound,
         config.fuzzySet.rightBound,
         config.fuzzySet.belong,
         config.fuzzySet.updateTime,

         int(fuzzySetId),
         int(elementId),
         int(pointOrline),
         int(leftBound),
         int(rightBound),
         float(belong),
         updateTime
         )
    print(sql)
    res= cursor.execute(sql)
    config.connect.commit()
    print("插入成功！" if res==True else "插入失败")
    cursor.close()
    
    

#删除模糊集
def fuzzySet_delete(id_value):

    cursor=config.connect.cursor()

    sql='''delete from %s where %s=%d
        '''%(config.fuzzySet.table_name,
             config.fuzzySet.id,
             int(id_value))
    print(sql)
    res= cursor.execute(sql)
    connect=config.connect
    connect.commit()
    cursor.close()
    print("删除成功" if res else "删除失败")

#更新模糊集
def fuzzySet_update(id_value,fuzzySetId,elementId,pointOrline,leftBound,rightBound,belong):

    cursor=config.connect.cursor()
    
    updateTime=datetime.datetime.now().strftime(config.time_format)

    print('执行sql前')
    sql='''update %s set %s=%d, %s=%d ,%s=%d, %s=%d,%s=%d,%s=%f,%s='%s' where %s=%d;
            '''%(config.fuzzySet.table_name,
                 config.fuzzySet.fuzzySetId,
                 int(fuzzySetId),
                 config.fuzzySet.elementId,
                 int(elementId),
                 config.fuzzySet.pointOrline,
                 int(pointOrline),
                 config.fuzzySet.leftBound,
                 int(leftBound),
                 config.fuzzySet.rightBound,
                 int(rightBound),
                 config.fuzzySet.belong,
                 float(belong),
                 config.fuzzySet.updateTime,
                 updateTime,
                 config.fuzzySet.id,
                  int(id_value)

                 )
    print(sql)
    print('更新sql函数')
    res= cursor.execute(sql)
    connect=config.connect
    connect.commit()
    cursor.close()
    print("更新成功" if res else "更新失败")



#模糊集根据ID查询的线程
class fuzzySet_search_by_id_thread(QThread):
    sinOut = pyqtSignal(list)

    def __init__(self, id):
        super().__init__()
        self.id = id

    def run(self):

        res= fuzzySet_search_by_id(self.id)
       
        self.sinOut.emit(res)



# 模糊集添加的线程
class fuzzy_set_add_thread(QThread):
    sinOut = pyqtSignal(list)

    def __init__(self, data):
        super().__init__()
        self.data = data

    def run(self):

        fuzzy_set_add(self.data[0], self.data[1],
                           self.data[2], self.data[3],
                           self.data[4], self.data[5])
        res=fuzzySet_search()
        print('增加线程')
        self.sinOut.emit(res)


# 模糊集删除的线程
class fuzzy_set_delete_thread(QThread):
    sinOut = pyqtSignal(list)

    def __init__(self, id):
        super().__init__()
        self.id = id

    def run(self):
        print('删除线程')
        fuzzySet_delete(int(self.id))
        res=fuzzySet_search()
        self.sinOut.emit(res)


#更新数据的线程
class fuzzy_set_update_thread(QThread):
    sinOut = pyqtSignal(list)

    def __init__(self, data):
        super().__init__()
        self.data = data

    def run(self):
        print('更新线程')
        fuzzySet_update( self.data[0],self.data[1],self.data[2],self.data[3],self.data[4],self.data[5],self.data[6])
        res=fuzzySet_search()
        self.sinOut.emit(res)