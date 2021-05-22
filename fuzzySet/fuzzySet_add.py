
import datetime
import config

def fuzzy_set_add(fuzzySetId,elementId,pointOrline,leftBound,rightBound,belong):
    cursor=config.connect.cursor()
    updateTime = datetime.datetime.now().strftime(config.time_format)
    sql = '''insert into %s (%s,%s,%s,%s,%s,%s,%s)
    values ('%d','%d', %d, %d, %d,'%f','%s')
    '''%(config.fuzzySet.table_name,
        config.fuzzySet.fuzzySetId,
        config.fuzzySet.elementId,
        config.fuzzySet.pointOrline,
        config.fuzzySet.leftBound,
        config.fuzzySet.rightBound,
        config.fuzzySet.belong,
        config.fuzzySet.updateTime,

        int(fuzzySetId),
        int(elementId),
        int(pointOrline),
        int(leftBound),
        int(rightBound),
        float(belong),
        updateTime
        )
    print(sql)
    res= cursor.execute(sql)
    config.connect.commit()
    print("插入成功！" if res==True else "插入失败")
    cursor.close()
    config.connect.close()


if __name__ == '__main__':
    cursor=config.connect.cursor()
    print("*****模糊知识库的模糊知识表*****")
    while(1):
        print("输入#终止")
        fuzzySetId=input("输入模糊集id：")
        if(fuzzySetId=='#'):
            break
        elementId=input("输入元素id：")
        pointOrline=input("输入点段标识：")
        leftBound=input("输入左边界：")
        rightBound=input("输入右边界：")
        belong=input("输入隶属度：")
        updateTime=datetime.datetime.now().strftime(config.time_format)

        sql = '''insert into %s (%s,%s,%s,%s,%s,%s,%s)
        values ('%d','%d', %d, %d, %d,'%f','%s')
        '''%(config.fuzzySet.table_name,
            config.fuzzySet.fuzzySetId,
            config.fuzzySet.elementId,
            config.fuzzySet.pointOrline,
            config.fuzzySet.leftBound,
            config.fuzzySet.rightBound,
            config.fuzzySet.belong,
            config.fuzzySet.updateTime,

            int(fuzzySetId),
            int(elementId),
            int(pointOrline),
            int(leftBound),
            int(rightBound),
            float(belong),
            updateTime
            )
        print(sql)
        res= cursor.execute(sql)

        config.connect.commit()
        print("插入成功！" if res==True else "插入失败")
    cursor.close()
    config.connect.close()