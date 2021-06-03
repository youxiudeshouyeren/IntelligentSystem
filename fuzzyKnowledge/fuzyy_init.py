### 初始化模糊知识
import datetime
import config


#a b-----1：很少 2:较少 3:少  4：正常 5：多 6：较多 7：很多
# c------8：不变 9:很小 10:较小 11:小   12：大 13：较大 14：很大

C=[[8,9,10,11,12,13,14],
   [9,8,9,10,11,12,13],
   [10,9,8,9,10,11,12],
   [11,10,9,8,9,10,11],
   [12,11,10,9,8,9,10],
   [13,12,11,10,9,8,9],
   [14,13,12,11,10,9,8]
   ]
cursor=config.connect.cursor()
fuzzyMatrixId=8 #模糊矩阵id

for precondition_b in range(1,8): #模糊集Aid
    for precondition_a in range(1,8): #模糊集Bid
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
