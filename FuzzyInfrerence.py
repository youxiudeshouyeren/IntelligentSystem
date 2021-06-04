import getDataFromDB
from fuzzyKnowledge import fuzzy_matrix
# import numpy as np

# 对车流量进行模糊化处理
def FuzzyVehicalCount(x):
    # 按照三角模糊法，取sigma为7
    result = []
    for i in range(40):
        if(i <= x - 4):
            result.append(0)
        elif(i > x -4 and i < x):
            temp = (i+4-x / 4)
            result.append(temp)
        elif(i >= x and i < x+4):
            temp = (x+4-i / 4)
            result.append(temp)
        else:
            result.append(0)

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
def SearchKnowledge():

    FuzzyKnowledge = getDataFromDB.getFuzzyKnowledgeData()
    Carnum = fuzzy_matrix.ReturnCarnum()
    count1 , count2 = getCount(4)
    fuzzycar1 = FuzzyVehicalCount(count1)
    fuzzycar2 = FuzzyVehicalCount(count2)
    Evidence = CaculateCompose(fuzzycar1,fuzzycar2)

    sims = []
    for i in range(len(FuzzyKnowledge)):
        Aid = FuzzyKnowledge[i][0]
        Bid = FuzzyKnowledge[i][1]
        Acar = Carnum[Aid - 1]
        Bcar = Carnum[Bid - 1]
        premise = CaculateCompose(Acar , Bcar)
        sim = CaculateSim(Evidence , premise)
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

    return conclusion

# 结论去模糊化
def Defuzzification():

    conclusion = CaculateConclusion()

    return conclusion.index(max(conclusion))


if __name__ == '__main__':
    conclusion = Defuzzification()

    print(conclusion)





