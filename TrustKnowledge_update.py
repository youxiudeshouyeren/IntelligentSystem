import datetime

import config
from TrustKnowledge_search import *

def TrustKnowledge_update():
    cursor=config.connect.cursor()
    id_value=input("要更新的产生式ID：")
    precondition_value=input("输入前提：")
    conclusion_value=input("输入结论：")
    pre_probablity_value=input("输入前提可信度：")
    con_probablity_value=input("输入结论可信度：")
    use_count_value=0
    last_use_value=datetime.datetime.now().strftime(config.time_format)


    sql='''update %s set %s="%s",%s="%s",%s=%f,%s=%f,%s=%d,%s="%s" where %s=%d;
            '''%(config.TrustworthinessKnowledge.table_name,
                 config.TrustworthinessKnowledge.precondition,precondition_value,
                 config.TrustworthinessKnowledge.conclusion,  conclusion_value,
                 config.TrustworthinessKnowledge.pre_probability, float(pre_probablity_value),
                 config.TrustworthinessKnowledge.con_probability,float(con_probablity_value),
                 config.TrustworthinessKnowledge.use_count, int(use_count_value),
                 config.TrustworthinessKnowledge.last_use, last_use_value,
                 config.TrustworthinessKnowledge.id,int(id_value)
                 )
    res= cursor.execute(sql)
    connect=config.connect
    connect.commit()
    cursor.close()
    print("更新成功" if res else "更新失败")


if __name__=="__main__":
    TrustKnowledge_search()
    TrustKnowledge_update()