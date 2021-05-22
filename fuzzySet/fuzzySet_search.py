import config

def fuzzySet_search():
    print('*****模糊知识库的模糊知识表*****')
    cursor=config.connect.cursor()
    sql='''select * from %s order by %s
        '''%(config.fuzzySet.table_name,
             config.fuzzySet.id)
    res= cursor.execute(sql)

    #成功取回数据则打印
    if(res):
        temp=cursor.rowcount
        print("模糊集ID\t\t\t\t元素ID\t\t\t\t点段标识\t\t\t\t左边界\t\t\t\t右边界\t\t\t\t隶属度\t\t\t\t更新时间")
        for i in range(temp):

            cursor.scroll(i, mode="absolute")
            data = cursor.fetchone()
            print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s"%(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
    cursor.close()

if __name__=='__main__':
    fuzzySet_search()
