# 工具函数库


from PyQt5.QtGui import QStandardItem, QColor

# 从sql查询结果中读取数据显示到表格上
def load_data_to_table(header,data,row,column,model):
    #print(data)
    model.clear()#先清空
    model.setHorizontalHeaderLabels(header)
    row=min(row, len(data))
    for i in range(row):
        for j in range(column):
            item=QStandardItem(str(data[i][j]))
            item.setBackground(QColor('#DDDDDD') if i%2 else QColor('#C0EFFA'))

            model.setItem(i,j,item)
