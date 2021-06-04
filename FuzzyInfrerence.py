import getDataFromDB
from fuzzyKnowledge import fuzzy_matrix
import numpy as np

# 对车流量进行模糊化处理
def FuzzyVehicalCount(x):
    # 按照三角模糊法，取sigma为7
    result = []
    for i in range(40):
        if(i <= x - 7):
            result.append(0)
        elif(i > x -7 and i < x):
            temp = ((i+7-x) / 7)
            result.append(temp)
        elif(i >= x and i < x+7):
            temp = ((x+7-i) / 7)
            result.append(temp)
        else:
            result.append(0)
    print(result)

    return result

# 计算交集
def jiaoji(num1 , num2):
    if(num1 >= num2 ):
        return num2
    else:
        return num1

# 计算并集
def huoji(num1 , num2):
    if(num1 >= num2):
        return num1
    else:
        return num2

# 得到输入，上两次的车辆数目
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
def CaculateSim(result , fuzzy_num):
    Carnum = fuzzy_matrix.ReturnCarnum()

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

# 寻找匹配度最高的那条知识
# 修改一下计算方法，不用合成证据，因为模糊化效果不好
def SearchKnowledge():

    FuzzyKnowledge = getDataFromDB.getFuzzyKnowledgeData()
    Carnum = fuzzy_matrix.ReturnCarnum()
    count1 , count2 = getCount(4)
    fuzzycar1 = FuzzyVehicalCount(count1)
    fuzzycar2 = FuzzyVehicalCount(count2)
    Evidence = CaculateCompose(fuzzycar1,fuzzycar2)
    print('evidence' , Evidence)

    sims = []
    for i in range(len(FuzzyKnowledge)):
        Aid = FuzzyKnowledge[i][0]
        Bid = FuzzyKnowledge[i][1]
        Acar = Carnum[Aid - 1]
        Bcar = Carnum[Bid - 1]
        premise = CaculateCompose(Acar , Bcar)
        sim1 = CaculateSim(Acar , fuzzycar1)
        sim2 = CaculateSim(Bcar , fuzzycar2)
        sim = sim1+sim2
        sims.append(sim)

    kslice = sims.index(max(sims))
    return Evidence,FuzzyKnowledge[kslice][0],FuzzyKnowledge[kslice][1],FuzzyKnowledge[kslice][2]

# 计算结论，前提与模糊矩阵相乘
def CaculateConclusion():
    evidence, index1 ,index2 ,index3 = SearchKnowledge()
    matrix = fuzzy_matrix.make_fuzzy_matrix(index1, index2 ,index3)

    matrix = np.array(matrix)
    temp = []
    for i in range(0,40,4):
        temp.append(evidence[i])

    evidence = np.array(temp)

    conclusion = evidence @ matrix
    conclusion = conclusion.tolist()

    conclusion = fuzzy_matrix.ReturnLightTime(index3 - 8)

    return conclusion

# 结论去模糊化
def Defuzzification():

    conclusion = CaculateConclusion()
    print(conclusion)
    maxvalue = max(conclusion)
    indexs = []
    for i in range(len(conclusion)):
        if(conclusion[i] == maxvalue):
            indexs.append(i)

    return indexs[0]



if __name__ == '__main__':
    conclusion = Defuzzification()

    print(conclusion)





