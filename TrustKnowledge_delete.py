import config
from TrustKnowledge_search import *

def TrustKnowledge_delete():
    cursor=config.connect.cursor()
    id_value=input("要删除的产生式ID：")
    sql='''delete from %s where id="%s"
        '''%(config.TrustworthinessKnowledge.table_name,
            id_value)
    res= cursor.execute(sql)
    connect=config.connect
    connect.commit()
    cursor.close()
    print("删除成功" if res else "删除失败")


if __name__=='__main__':
    TrustKnowledge_search()
    TrustKnowledge_delete()