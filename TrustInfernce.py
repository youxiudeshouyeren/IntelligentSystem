import getDataFromDB

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
    elif(x >= 15 and x < 20):
        cf2 = (-1/7.5) * x + 8/3
        cf3 = x / 5 - 3
    else:
        cf3 = 1
    countLow = '上一轮绿灯通过车辆少'
    countMiddle = '上一轮绿灯通过车辆适中'
    countHigh = '上一轮绿灯通过车辆多'
    factData.append([countLow,cf1])
    factData.append([countMiddle,cf2])
    factData.append([countHigh,cf3])

def getGapCountFact(x):   #获取上上次和上次车流量变化情况事实
    cf1 = 0.0
    cf2 = 0.0
    cf3 = 0.0
    if (x < -5):
        cf1 = 1
    elif (x >= -5 and x < 0):
        cf1 = (-1 / 5) * x
        cf2 = 1 / 5 * x + 1
    elif (x >= 0 and x < 5):
        cf2 = (-1 / 5) * x + 1
        cf3 = 1 / 5 * x
    elif (x >= 5):
        cf3 = 1
    countLow = '上次通过车辆较上上次减少较多'
    countMiddle = '前两轮通过车辆数目变化不大'
    countHigh = '上次通过车辆较上上次增加较多'
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
                gapCount = count - VehicleData[i][3]
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

def getConclusion(direction):
    count,gapCount = getCount(direction)
    print(count,gapCount)
    getVehicalCountFact(count)
    getGapCountFact(gapCount)
    TrustKnowledgeMatch()
    conFact = ['本轮绿灯时间减少','本轮绿灯时间不变','本轮绿灯时间增加']
    factCount = factData[len(factData) - 2]
    factGap = factData[len(factData) - 1]
    #结论合成
    conclusion = []
    result = ''
    cfH = 0.0
    if(factCount[1] >= factGap[1]):
        cfH = factCount[1] - factGap[1]
        result = factCount[0]
    else:
        cfH = factGap[1] - factCount[1]
        result = factGap[0]
    if(cfH != 0.0):
        conclusion.append(result)
        conclusion.append(cfH)
    else:
        conclusion.append('本轮绿灯时间不变')
        conclusion.append(1)
    factData.append(conclusion)
    return conclusion


if __name__ == '__main__':
    conclusion = getConclusion(4)
    print(factData)
    print(conclusion)
