import config


def fuzzySet_delete():
    while(1):
        cursor=config.connect.cursor()
        id_value=input("要删除的模糊知识库的模糊知识表ID(输入#终止)：")

        if(id_value == '#'):
            break
        sql='''delete from %s where id="%s"
            '''%(config.fuzzySet.table_name,
                id_value)
        res= cursor.execute(sql)
        connect=config.connect
        connect.commit()
        cursor.close()
        print("删除成功" if res else "删除失败")


if __name__=='__main__':
    fuzzySet_delete()
