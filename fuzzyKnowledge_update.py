import datetime

import config
from fuzzyKnowledge_search import *

def fuzzyKnowledge_update():
    fuzzyKnowledge_search()

    cursor=config.connect.cursor()
    id_value=input("要更新的模糊知识ID：")
    precondition_a=input("输入模糊集Aid：")
    precondition_b=input("输入模糊集Bid：")

    con_c=input("输入模糊集Cid：")
    fuzzyMatrixID=input("输入模糊矩阵id：")
    pre_probablity_value=input("输入前提可信度：")
    con_probablity_value=input("输入结论可信度：")
    use_count_value=0
    last_use_value=datetime.datetime.now().strftime(config.time_format)


    sql='''update %s set %s="%d",%s="%d",%s=%d,%s=%d,%s=%f,%s="%f",%s="%d",%s="%s" where %s=%d;
            '''%(config.fuzzyKnowledge.table_name,
                 config.fuzzyKnowledge.Aid,int(precondition_a),
                 config.fuzzyKnowledge.Bid,int(precondition_b),
                 config.fuzzyKnowledge.Cid, int(con_c),
                 config.fuzzyKnowledge.fuzzyMatrixId,int(fuzzyMatrixID),
                 config.fuzzyKnowledge.pre_probability, float(pre_probablity_value),
                 config.fuzzyKnowledge.con_probability, float(con_probablity_value),
                 config.fuzzyKnowledge.use_count, int(use_count_value),
                 config.fuzzyKnowledge.last_use, last_use_value,
                 config.fuzzyKnowledge.id,int(id_value)
                 )
    res= cursor.execute(sql)
    connect=config.connect
    connect.commit()
    cursor.close()
    print("更新成功" if res else "更新失败")


if __name__=="__main__":
    fuzzyKnowledge_update()
