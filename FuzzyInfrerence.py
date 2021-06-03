import getDataFromDB
from fuzzyKnowledge import fuzzy_matrix

# 对车流量进行模糊化处理
def FuzzyVehicalCount(x):
    # 按照三角模糊法，取sigma为7
    result = []
    for i in range(40):
        if(i <= x - 7):
            result.append(0)
        elif(i > x -7 and i < x):
            temp = (i+7-x / 7)
            result.append(temp)
        elif(i >= x and i < x+7):
            temp = (x+7-i / 7)
            result.append(temp)
        else:
            result.append(0)

    return result

def jiaoji(num1 , num2):
    if(num1 >= num2 ):
        return num2
    else:
        return num1

def huoji(num1 , num2):
    if(num1 >= num2):
        return num1
    else:
        return num2

def getCount(type):
    VehicleData = getDataFromDB.getVehicleData()
    count = 0 #上一轮车辆通过数
    Count2 = 0  #这轮车辆通过数
    gap = 0
    for i in range(len(VehicleData)):
        if(VehicleData[i][0] == type):
            gap += 1
            if(gap == 1):
                count = VehicleData[i][3]
            elif(gap == 2):
                Count2 =VehicleData[i][3]
                break

    return count,Count2

# 计算合成证据/前提
def CaculateCompose(fk1 , fk2):
    result = []
    for i in range(len(fk1)):
        result.append(jiaoji(fk1[i],fk2[i]))

    return result

# 计算事实模糊化结果和前提的匹配度
# 有点混乱，暂定
def CaculateSim(result , id):
    Carnum = fuzzy_matrix.ReturnCarnum()
    i = id - 1
    fuzzy_num = Carnum[i]
    temp1 = []
    temp2 = []
    for i in range(len(fuzzy_num)):
        #计算两两之间的交集
        temp1.append(jiaoji(fuzzy_num[i] , result[i]))
        temp2.append(huoji(fuzzy_num[i] , result[i]))
    maxone = max(temp1)
    minone = min(temp2)

    sim = (maxone + 1 - minone) / 2

    return sim

def SearchKnowledge():

    FuzzyKnowledge = getDataFromDB.getFuzzyKnowledgeData()
    count1 , count2 = getCount(4)
    fuzzycar1 = FuzzyVehicalCount(count1)
    fuzzycar2 = FuzzyVehicalCount(count2)
    Evidence = CaculateCompose(fuzzycar1,fuzzycar2)





