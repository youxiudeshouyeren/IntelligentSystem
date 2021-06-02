### 增加可信度知识
import datetime
import config

cursor=config.connect.cursor()
print("*****增加模糊知识*****")

while(1):
    print("输入#终止")
    precondition_a=input("输入模糊集Aid：")
    if(precondition_a=='#'):
        break
    precondition_b=input("输入模糊集Bid：")

    conclusion_c=input("输入模糊矩阵Cid：")
    fuzzyMatrixId = input("输入模糊矩阵id：")
    pre_probablity_value=input("输入前提可信度：")
    con_probablity_value=input("输入结论可信度：")
    # whoUpdate = input("输入更新人：")
    use_count_value=0
    updateTime=datetime.datetime.now().strftime(config.time_format)

    sql = '''insert into %s (%s,%s,%s,%s,%s,%s,%s,%s)  
    values ('%d','%d',%d,%d,%f,'%f','%d','%s')
    '''%(config.fuzzyKnowledge.table_name,
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
    print(sql)
    res= cursor.execute(sql)

    config.connect.commit()
    print("插入成功！" if res==True else "插入失败")


cursor.close()
config.connect.close()
