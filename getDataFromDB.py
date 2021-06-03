import config
import time
import datetime
#将数据库中数据转化为列表存储
def getTrustKnowledgeData():   #获取可信度知识库数据
    cursor=config.connect.cursor()
    sql='''select %s,%s,%s,%s from %s order by %s desc;
        '''%(config.TrustworthinessKnowledge.precondition,
             config.TrustworthinessKnowledge.conclusion,
             config.TrustworthinessKnowledge.pre_probability,
             config.TrustworthinessKnowledge.con_probability,
             config.TrustworthinessKnowledge.table_name,
             config.TrustworthinessKnowledge.id) #倒序查询 保证新数据再最上面
    cursor.execute(sql)
    result = cursor.fetchall()
    result = list(result)
    return result

def getVehicleData():
    cursor = config.connect.cursor()
    sql = '''select %s,%s,%s,%s from %s order by %s DESC ;
            ''' % (config.VehicleData.type,
                   config.VehicleData.begintime,
                   config.VehicleData.endtime,
                   config.VehicleData.vehiclecount,
                   config.VehicleData.tablename,
                   config.VehicleData.begintime)  # 倒序查询 保证新数据再最上面
    cursor.execute(sql)
    result = cursor.fetchall()
    result = list(result)
    return result

# 获取模糊知识
def getFuzzyKnowledgeData():
    cursor = config.connect.cursor()
    sql = '''select %s,%s,%s,%s,%s,%s from %s order by %s desc;
            ''' % (config.fuzzyKnowledge.Aid,
                   config.fuzzyKnowledge.Bid,
                   config.fuzzyKnowledge.Cid,
                   config.fuzzyKnowledge.fuzzyMatrixId,
                   config.fuzzyKnowledge.pre_probability,
                   config.fuzzyKnowledge.con_probability,
                   config.fuzzyKnowledge.table_name,
                   config.fuzzyKnowledge.id)  # 倒序查询 保证新数据再最上面
    cursor.execute(sql)
    result = cursor.fetchall()
    result = list(result)
    return result

def getFuzzySet():
    pass

if __name__ == '__main__':
    TrustKnowledge = getTrustKnowledgeData()
    print(type(TrustKnowledge[0]))
    print(TrustKnowledge)
    VehicleData = getVehicleData()
    print(type(VehicleData[0][1]))


