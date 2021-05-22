import datetime
import config
#from fuzzySet import fuzzySet_add

cursor=config.connect.cursor()

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
    #config.connect.close()


"""
每次运行不可能都填补一次表格的内容，
此处作者提供一个初始化隶属函数的方法。
"""
def initial_fuzzy_set_table():

    try:
        cursor=config.connect.cursor()
        sql="drop table fuzzySet"
        res= cursor.execute(sql)
        connect=config.connect
        connect.commit()
    except:
        print("fuzzySet数据表不存在,即将创建")

    sql="CREATE TABLE IF NOT EXISTS `fuzzySet` ( \
        `id` int(10) unsigned NOT NULL auto_increment,\
        `fuzzySetId` int(10) NOT NULL,\
        `elementId` int(10) NOT NULL,\
        `pointOrline` int(4) NOT NULL,\
        `leftBound` int(10) NOT NULL,\
        `rightBound` int(10) NOT NULL,\
        `belong` float NOT NULL,\
        `updateTime` datetime DEFAULT NULL,\
        `whoUpdate` varchar(20) DEFAULT NULL,\
        primary key(id)\
        ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;"
    res= cursor.execute(sql)
    connect=config.connect
    connect.commit()

    cursor.close()
    

    #初始化前应该删除表中所有内容 to do
    # fuzzy_set_add(fuzzySetId,elementId,pointOrline,leftBound,rightBound,belong)
    #很少
    fuzzy_set_add(1,    1,     1,      0,      3,        1    )
    fuzzy_set_add(1,    2,     1,      3,      7,        0.8  )
    fuzzy_set_add(1,    3,     1,      7,      10,       0.4  )
    fuzzy_set_add(1,    4,     1,      10,     14,       0.1  )
    fuzzy_set_add(1,    5,     1,      14,     40,       0    )

    #较少
    fuzzy_set_add(2,    1,     1,      0,      3,        0.2    )
    fuzzy_set_add(2,    2,     1,      3,      7,        0.7  )
    fuzzy_set_add(2,    3,     1,      7,      10,       1  )
    fuzzy_set_add(2,    4,     1,      10,     14,       0.7  )
    fuzzy_set_add(2,    5,     1,      14,     40,       0    )

    #少
    fuzzy_set_add(3,    1,     1,      0,      3,        0    )
    fuzzy_set_add(3,    2,     1,      3,      7,        0.2  )
    fuzzy_set_add(3,    3,     1,      7,      10,       0.7  )
    fuzzy_set_add(3,    4,     1,      10,     14,       1  )
    fuzzy_set_add(3,    5,     1,      14,     18,       0.5    )
    fuzzy_set_add(3,    6,     1,      18,     40,       0    )

#正常
    fuzzy_set_add(4,    1,     1,      0,      14,        0    )
    fuzzy_set_add(4,    2,     1,      14,      18,        0.5  )
    fuzzy_set_add(4,    3,     1,      18,      24,       1  )
    fuzzy_set_add(4,    4,     1,      24,     27,       0.5  )
    fuzzy_set_add(4,    5,     1,      27,     40,       0    )


#多
    fuzzy_set_add(5,    1,     1,      0,     24,        0    )
    fuzzy_set_add(5,    2,     1,      24,      27,        0.5  )
    fuzzy_set_add(5,    3,     1,      27,      30,       1  )
    fuzzy_set_add(5,    4,     1,      30,     33,       0.7  )
    fuzzy_set_add(5,    5,     1,      33,     36,       0.2    )
    fuzzy_set_add(5,    6,     1,      36,     40,       0    )

#较多
    fuzzy_set_add(6,    1,     1,      0,      27,        0    )
    fuzzy_set_add(6,    2,     1,      27,      30,        0.7  )
    fuzzy_set_add(6,    3,     1,      30,      33,       1  )
    fuzzy_set_add(6,    4,     1,      33,     36,       0.7  )
    fuzzy_set_add(6,    5,     1,      36,     40,       0.2    )

#很多
    fuzzy_set_add(7,    1,     1,      0,      27,        0    )
    fuzzy_set_add(7,    2,     1,      27,      30,        0.1  )
    fuzzy_set_add(7,    3,     1,      30,      33,       0.4  )
    fuzzy_set_add(7,    4,     1,      33,     36,       0.8  )
    fuzzy_set_add(7,    5,     1,      36,     40,       1    )


#很小
    fuzzy_set_add(8,    1,     1,      0,      5,        1    )
    fuzzy_set_add(8,    2,     1,      5,      10,        0.8  )
    fuzzy_set_add(8,    3,     1,      10,      15,       0.4  )
    fuzzy_set_add(8,    4,     1,      15,     20,       0.1  )
    fuzzy_set_add(8,    5,     1,      20,     60,       0    )

#较小
    fuzzy_set_add(9,    1,     1,      0,      5,        0    )
    fuzzy_set_add(9,    2,     1,      5,      10,        0.2  )
    fuzzy_set_add(9,    3,     1,      10,      15,       0.7  )
    fuzzy_set_add(9,    4,     1,      15,     20,       1  )
    fuzzy_set_add(9,    5,     1,      20,     25,       0.7    )
    fuzzy_set_add(9,    6,     1,      25,     30,       0.2  )
    fuzzy_set_add(9,    7,     1,      30,     60,       0    )

#小
    fuzzy_set_add(10,    1,     1,      0,      20,        0    )
    fuzzy_set_add(10,    2,     1,      20,      25,        0.5  )
    fuzzy_set_add(10,    3,     1,      25,      30,       1  )
    fuzzy_set_add(10,    4,     1,      30,     35,       0.5  )
    fuzzy_set_add(10,    5,     1,      35,     60,       0    )

#大
    fuzzy_set_add(11,    1,     1,      0,      25,        0    )
    fuzzy_set_add(11,    2,     1,      25,      30,        0.5  )
    fuzzy_set_add(11,    3,     1,      30,      35,       1  )
    fuzzy_set_add(11,    4,     1,      35,     40,       0.5  )
    fuzzy_set_add(11,    5,     1,      40,     60,       0    )

#较大
    fuzzy_set_add(12,    1,     1,      0,      30,        0    )
    fuzzy_set_add(12,    2,     1,      30,      35,        0.2  )
    fuzzy_set_add(12,    3,     1,      35,      40,       0.7  )
    fuzzy_set_add(12,    4,     1,      40,     45,       1  )
    fuzzy_set_add(12,    5,     1,      45,     50,       0.7    )
    fuzzy_set_add(12,    6,     1,      50,     55,       0.2  )
    fuzzy_set_add(12,    7,     1,      55,     60,       0    )

#很大

    fuzzy_set_add(13,    1,     1,      0,      40,        0    )
    fuzzy_set_add(13,    2,     1,      40,      45,        0.1  )
    fuzzy_set_add(13,    3,     1,      45,      50,       0.4  )
    fuzzy_set_add(13,    4,     1,      50,     55,       0.8  )
    fuzzy_set_add(13,    5,     1,      55,     60,       1    )

if __name__=='__main__':
    initial_fuzzy_set_table()