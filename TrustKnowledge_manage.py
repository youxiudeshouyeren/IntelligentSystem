import config

def TrustKnowledge_search():


    print('*****可信度知识库*****')
    cursor=config.connect.cursor()
    sql='''select * from %s order by %s
        '''%(config.TrustworthinessKnowledge.table_name,
             config.TrustworthinessKnowledge.id)
    res= cursor.execute(sql)
    sqldata=[]

    #成功取回数据则打印
    if(res):
        temp=cursor.rowcount
        print("产生式ID\t\t\t前提\t\t\t结论\t\t\t前提可信度\t\t\t结论可信度\t\t\t知识使用次数\t\t\t最后一次使用时间")
        for i in range(temp):

            cursor.scroll(i, mode="absolute")
            data = cursor.fetchone()
            #print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s"%(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
            sqldata.append(data)
    cursor.close()
    return sqldata

if __name__=='__main__':
    TrustKnowledge_search()
