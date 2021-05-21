import datetime
import config
cursor=config.connect.cursor()
# select CONCAT( 'drop table ', table_name, ';' ) FROM information_schema.tables Where table_name LIKE '%_16%';
while(1):
    tableId = input("请输入希望删除的模糊矩阵表名（#结束）：")
    if(tableId == '#'):
        break
    sql = '''
        drop table matrix%s;
    '''%tableId
    print(sql)
    res = cursor.execute(sql)
    config.connect.commit()
    print("删除成功！")
cursor.close()
config.connect.close()
