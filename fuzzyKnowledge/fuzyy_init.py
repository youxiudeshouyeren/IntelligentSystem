### 初始化模糊知识
import datetime
import config


#a b-----1：很少 2:较少 3:少  4：正常 5：多 6：较多 7：很多
# c------1：不变 2:增加很小 3:增加较小 4:增加小   5：增加大 6：增加较大 7：增加很大
#               8:减少很小 9:减少较小 10:减少小  11：减少大 12：减少较大 13：减少很大

C=[[1,2,3,4,5,6,7],
   [8,1,2,3,4,5,6],
   [9,8,1,2,3,4,5],
   [10,9,8,1,2,3,4],
   [11,10,9,8,1,2,3],
   [12,11,10,9,8,1,2],
   [13,12,11,10,9,8,1]
   ]
cursor=config.connect.cursor()
fuzzyMatrixId=1 #模糊矩阵id

for precondition_a in range(1,8): #模糊集Aid
    for precondition_b in range(1,8): #模糊集Bid
        conclusion_c=C[precondition_a-1][precondition_b-1]  #模糊矩阵Cid
        pre_probablity_value=0.8 #前提可信度
        con_probablity_value=0.9 #结论可信度
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
        # print(sql)
        res = cursor.execute(sql)
        config.connect.commit()
        print("插入成功！" if res == True else "插入失败")

        fuzzyMatrixId+=1 #自增

cursor.close()
config.connect.close()
