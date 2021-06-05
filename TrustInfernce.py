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
    cf1 = round(cf1,2)
    cf2 = round(cf2,2)
    cf3 = round(cf3,2)

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
    if (x < -10):
        cf1 = 1
    elif (x >= -10 and x < 0):
        cf1 = (-1 / 10) * x
        cf2 = 1 / 10 * x + 1
    elif (x >= 0 and x < 10):
        cf2 = (-1 / 10) * x + 1
        cf3 = 1 / 10 * x
    elif (x >= 10):
        cf3 = 1
    cf1 = round(cf1, 2)
    cf2 = round(cf2, 2)
    cf3 = round(cf3, 2)
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
Knowledge = []
def TrustKnowledgeMatch():
    TrustKnowledge = getDataFromDB.getTrustKnowledgeData()
    conclusion = []
    for i in range(len(factData)):
        for j in range(len(TrustKnowledge)):
            if(factData[i][0] == TrustKnowledge[j][0]):
                if(factData[i][1] >= TrustKnowledge[j][3]):
                    # print('知识：',factData[i][0],'匹配成功')
                    print(TrustKnowledge[j])
                    Knowledge.append(TrustKnowledge[j])
                    cfH = factData[i][1] * TrustKnowledge[j][2]
                    cfH = round(cfH, 2)
                    conclusion = [TrustKnowledge[j][1],cfH]
                    factData.append(conclusion)

def getConclusion(direction):
    count,gapCount = getCount(direction)
    print("count: %d , gapCount: %d " %(count,gapCount))
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
        if(factCount[0] == factGap[0]):
            cfH = factCount[1]
        else:
            cfH = factCount[1] - factGap[1]
        result = factCount[0]
    else:
        if (factCount[0] == factGap[0]):
            cfH = factGap[1]
        else:
            cfH = factGap[1] - factCount[1]
        result = factGap[0]
    cfH = round(cfH,2)
    if(cfH != 0.0):
        conclusion.append(result)
        conclusion.append(cfH)
    else:
        conclusion.append('本轮绿灯时间不变')
        conclusion.append(1)
    factData.append(conclusion)
    return conclusion

def getInferenceChain():
    InfernceChain = '获取到的事实为：' + '\n'
    if len(factData) != 9:
        return '本轮知识未匹配，绿灯时间不变'
    FactLeft = ''
    FactRight = ''
    conLeft = ''
    conRight = ''
    conHinge = ''
    for i in range(len(factData)):
        if(i<3):
            FactLeft += '('+ str(i) +')' + factData[i][0] + ' 可信度为： ' + str(factData[i][1]) + '\n'
        elif(i<6):
            FactRight += '('+ str(i) +')' + factData[i][0] + ' 可信度为： ' + str(factData[i][1]) + '\n'
        elif(i == 6):
            conLeft = '将(0)(1)(2)同可信度知识库进行匹配,匹配到的知识为：'
            for j in Knowledge[0]:
                conLeft += str(j) + ' '
            conLeft += '\n      将事实可信度和知识可信度相乘，产生新的事实为：' + '('+ str(i) +')' + factData[i][0] + ' 可信度为： ' + str(factData[i][1]) + '\n'
        elif(i==7):
            conRight = '将(3)(4)(5)同可信度知识库进行匹配,匹配到的知识为：'
            for j in Knowledge[1]:
                conRight += str(j) + ' '
            conRight += '\n      将事实可信度和知识可信度相乘，产生新的事实为：' + '(' + str(i) + ')' + factData[i][0] + ' 可信度为： ' + str(factData[i][1]) + '\n'
        elif(i==8):
            conHinge = '将(6)(7)结论进行合成，取可信度高者，若前提不同，可信度最后需要相减：\n\n   生成的结论为：'+factData[i][0] + ' 可信度为： ' + str(factData[i][1]) + '\n'

    InfernceChain += FactLeft + FactRight + conLeft + conRight + conHinge

    return InfernceChain



if __name__ == '__main__':
    conclusion = getConclusion(0)
    print(factData)
    print(conclusion)
    InfernceChain = getInferenceChain()
    print(InfernceChain)
