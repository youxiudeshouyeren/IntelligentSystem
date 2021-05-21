import config

def fuzzyKnowledge_search():


    print('*****模糊知识库*****')
    cursor=config.connect.cursor()
    sql='''select * from %s order by %s
        '''%(config.fuzzyKnowledge.table_name,
             config.fuzzyKnowledge.id)
    res= cursor.execute(sql)

    #成功取回数据则打印
    if(res):
        temp=cursor.rowcount
        print("模糊知识ID\t\t\t模糊集Aid\t\t\t模糊集Aid\t\t\t模糊集Cid\t\t\t模糊矩阵id\t\t\t前提可信度\t\t\t结论可信度\t\t\t更新时间\t\t\t使用次数")
        for i in range(temp):

            cursor.scroll(i, mode="absolute")
            data = cursor.fetchone()
            print("%s\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t%s\t\t%s"%(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[9]))
    cursor.close()

if __name__=='__main__':
    fuzzyKnowledge_search()
