### 增加可信度知识
import datetime

import config

cursor=config.connect.cursor()
print("*****增加可信度知识*****")

while(1):
    print("输入#终止")
    precondition_value=input("输入前提：")
    if(precondition_value=='#'):
        break

    conclusion_value=input("输入结论：")
    pre_probablity_value=input("输入前提可信度：")
    con_probablity_value=input("输入结论可信度：")
    use_count_value=0
    last_use_value=datetime.datetime.now().strftime(config.time_format)

    sql = '''insert into %s (%s,%s,%s,%s,%s,%s)  
    values ('%s','%s',%f,%f,%d,'%s');
    '''%(config.TrustworthinessKnowledge.table_name,
         config.TrustworthinessKnowledge.precondition,
         config.TrustworthinessKnowledge.conclusion,
         config.TrustworthinessKnowledge.pre_probability,
         config.TrustworthinessKnowledge.con_probability,
         config.TrustworthinessKnowledge.use_count,
         config.TrustworthinessKnowledge.last_use,
         precondition_value,
         conclusion_value,
         float(pre_probablity_value),
         float(con_probablity_value),
         int(use_count_value),
         last_use_value)
    print(sql)
    res= cursor.execute(sql)
    config.connect.commit()
    print("插入成功！" if res==True else "插入失败")


cursor.close()
config.connect.close()