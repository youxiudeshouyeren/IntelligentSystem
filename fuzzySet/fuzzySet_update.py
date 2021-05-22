import datetime

import config

def fuzzySet_update():

    cursor=config.connect.cursor()
    id_value = input("要更新的模糊知识ID：")
    fuzzySetId = input("输入模糊集id：")
    elementId = input("输入元素id：")
    pointOrline = input("输入点段标识：")
    leftBound = input("输入左边界：")
    rightBound = input("输入右边界：")
    belong = input("输入隶属度：")
    updateTime=datetime.datetime.now().strftime(config.time_format)


    sql='''update %s set %s="%d",%s="%d",%s=%d,%s=%d,%s=%d,%s="%f",%s="%s" where %s=%d;
            '''%(config.fuzzySet.table_name,

                 config.fuzzySet.fuzzySetId, int(fuzzySetId),
                 config.fuzzySet.elementId,int(elementId),
                 config.fuzzySet.pointOrline,int(pointOrline),
                 config.fuzzySet.leftBound,int(leftBound),
                 config.fuzzySet.rightBound,int(rightBound),

                 config.fuzzySet.belong,float(belong),
                 config.fuzzySet.updateTime,updateTime,

                 config.fuzzySet.id, int(id_value)

                 )
    res= cursor.execute(sql)
    connect=config.connect
    connect.commit()
    cursor.close()
    print("更新成功" if res else "更新失败")


if __name__=="__main__":
    fuzzySet_update()
