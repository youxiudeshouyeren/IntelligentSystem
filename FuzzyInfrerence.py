import getDataFromDB
from fuzzyKnowledge import fuzzy_matrix
import numpy as np

#解释器，记录推理过程
fuzzy_train=[]
#车辆数据  1：很少 2:较少 3:少  4：正常 5：多 6：较多 7：很多
# 时间变化幅度  8：不变 9:很小 10:较小 11:小   12：大 13：较大 14：很大
car_time=['','很少','较少','少','正常','多','较多','很多',
          '不变','很小','较小','小','大','较大','很大']

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
    # print(result)

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
    Count2 = 0  #上上轮车辆通过数
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
def SearchKnowledge(derection):

    FuzzyKnowledge = getDataFromDB.getFuzzyKnowledgeData()
    Carnum = fuzzy_matrix.ReturnCarnum()
    count1 , count2 = getCount(derection)
    fuzzycar1 = FuzzyVehicalCount(count1)
    fuzzycar2 = FuzzyVehicalCount(count2)
    Evidence = CaculateCompose(fuzzycar1,fuzzycar2)
    # print('evidence' , Evidence)

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
    fuzzy_train.append('南北方向，使用模糊推理机 本轮车辆数：' + str(count1)+',上轮车辆数：' + str(count2))
    fuzzy_train.append('使用三角法对车辆数据进行模糊化：\n'+str(fuzzycar1)+'\n'+str(fuzzycar2))
    fuzzy_train.append('求出的最大匹配度为' + str(max(sims)))
    fuzzy_train.append('计算出合成证据：'+ str(Evidence))
    if (count1 == count2):
        fuzzy_train.append('使用第'+str(kslice)+'条知识：' + 'IF x is 当前车辆(x1) '\
                       +str(car_time[FuzzyKnowledge[kslice][0]])+' &上次车辆(x2)'
                        +str(car_time[FuzzyKnowledge[kslice][1]])+' THEN y is 绿灯时间不变')
    elif (count1 < count2):
        fuzzy_train.append('使用第' + str(kslice) + '条知识：' + 'IF x is 当前车辆(x1) ' \
                           + str(car_time[FuzzyKnowledge[kslice][0]]) + ' &上次车辆(x2)'
                           + str(car_time[FuzzyKnowledge[kslice][1]]) + ' THEN y is 绿灯时间减少'
                           +str(car_time[FuzzyKnowledge[kslice][2]]))
    elif (count1 > count2):
        fuzzy_train.append('使用第' + str(kslice) + '条知识：' + 'IF x is 当前车辆(x1) ' \
                           + str(car_time[FuzzyKnowledge[kslice][0]]) + ' &上次车辆(x2)'
                           + str(car_time[FuzzyKnowledge[kslice][1]]) + ' THEN y is 绿灯时间增加'
                           + str(car_time[FuzzyKnowledge[kslice][2]]))
    return Evidence,FuzzyKnowledge[kslice][0],FuzzyKnowledge[kslice][1],FuzzyKnowledge[kslice][2]

# 计算结论，前提与模糊矩阵相乘
def CaculateConclusion(derection):
    evidence, index1 ,index2 ,index3 = SearchKnowledge(derection)
    matrix = fuzzy_matrix.make_fuzzy_matrix(index1-1, index2-1 ,index3-8)
    # print(index1-1 , index2-1 ,index3-8)


    matrix = np.array(matrix)
    temp = []
    for i in range(0,40,4):
        temp.append(evidence[i])

    evidence = np.array(temp)

    conclusion = evidence @ matrix
    conclusion = conclusion.tolist()

    conclusion = fuzzy_matrix.ReturnLightTime(index3 - 8)
    fuzzy_train.append('计算出结论：时间变化幅度为 '+str(conclusion))
    # print('conclusion',conclusion)
    return conclusion


# 结论去模糊化
def Defuzzification(derection):

    conclusion = CaculateConclusion(derection)
    # print(conclusion)
    maxvalue = max(conclusion)
    indexs = []
    for i in range(len(conclusion)):
        if(conclusion[i] == maxvalue):
            indexs.append(i)
    fuzzy_train.append('使用最大隶属度法对结论进行去模糊化，时间变化： '+str(indexs[0])+'秒')
    return indexs[0],fuzzy_train



if __name__ == '__main__':

    count1 , count2 = getCount(1)
    print(count1, count2)
    conclusion,fuzzy_train = Defuzzification(1)
    if(count1 == count2 or conclusion==0):
        print('不变')
    elif(count1 < count2):
        print('绿灯时长减少{}秒'.format(conclusion))
    elif (count1 > count2):
        # conclusion = Defuzzification()
        print('绿灯时长增加{}秒'.format(conclusion))

    # print(fuzzy_train)
    for th in fuzzy_train:
        print(th)
    # CaculateConclusion()





