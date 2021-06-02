import getDataFromDB

inferenceChain = {}   #推理链
factData = []  #事实库

def getVehicalCountFact(x):   #获取上次车流量产生的事实
    cf1 = 0.0
    cf2 = 0.0
    cf3 = 0.0
    if (x < 5):
        cf1 = 1
    elif(x >= 5 and x < 10):
        cf1 = (-1/5) * x + 2
        cf2 = (1/7.5) * x - (2/3)
    elif(x >= 10 and x < 15):
        cf2 = 0.8
    elif(x >= 15):
        cf2 = (-1/7.5) * x + 8/3
        cf3 = x / 5 - 3
    countLow = '上一轮绿灯通过车辆少'
    countMiddle = '上一轮绿灯通过车辆适中'
    countHigh = '上一轮绿灯通过车辆多'
    factData.append([countLow,cf1])
    factData.append([countMiddle,cf2])
    factData.append([countHigh,cf3])

def getGapCountFact(x):   #待完成
    cf1 = 0.0
    cf2 = 0.0
    cf3 = 0.0
    if (x < 5):
        cf1 = 1
    elif (x >= 5 and x < 10):
        cf1 = (-1 / 5) * x + 2
        cf2 = (1 / 7.5) * x - (2 / 3)
    elif (x >= 10 and x < 15):
        cf2 = 0.8
    elif (x >= 15):
        cf2 = (-1 / 7.5) * x + 8 / 3
        cf3 = x / 5 - 3
    countLow = '上一轮绿灯通过车辆少'
    countMiddle = '上一轮绿灯通过车辆适中'
    countHigh = '上一轮绿灯通过车辆多'
    factData.append([countLow, cf1])
    factData.append([countMiddle, cf2])
    factData.append([countHigh, cf3])

def getCount(type):
    VehicleData = getDataFromDB.getVehicleData()
    count = 0 #上一轮车辆通过数
    gapCount = 0  #两轮车辆变化情况
    gap = 0
    for i in range(len(VehicleData)):
        if(VehicleData[i][0] == type):
            gap += 1
            if(gap == 1):
                count = VehicleData[i][3]
            elif(gap == 2):
                gapCount = VehicleData[i][3] - count
                break

    return count,gapCount

def TrustKnowledgeMatch():
    TrustKnowledge = getDataFromDB.getTrustKnowledgeData()
    conclusion = []
    for i in range(len(factData)):
        for j in range(len(TrustKnowledge)):
            if(factData[i][0] == TrustKnowledge[j][0]):
                if(factData[i][1] >= TrustKnowledge[j][3]):
                    print('知识：',factData[i][0],'匹配成功')
                    cfH = factData[i][1] * TrustKnowledge[j][2]
                    conclusion = [TrustKnowledge[j][1],cfH]
    factData.append(conclusion)

if __name__ == '__main__':
    # fact = []
    # fact = getFact(3)
    # print('获取的事实及其可信度为：')
    # print(fact)
    # print(type(fact))
    getVehicalCountFact(6)
    print(factData)
    TrustKnowledgeMatch()
    print(factData)
