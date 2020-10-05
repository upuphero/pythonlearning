import xlrd
import xlwt


data = xlrd.open_workbook(r'30180.xlsx')


table = data.sheets()[0]          #通过索引顺序获取

table = data.sheet_by_index(sheet_indx)) #通过索引顺序获取

table = data.sheet_by_name(sheet_name)#通过名称获取

#以上三个函数都会返回一个xlrd.sheet.Sheet()对象

names = data.sheet_names()    #返回book中所有工作表的名字

data.sheet_loaded(sheet_name or indx)   # 检查某个sheet是否导入完毕



nrows = table.nrows  #获取该sheet中的有效行数

table.row(rowx)  #返回由该行中所有的单元格对象组成的列表

table.row_slice(rowx)  #返回由该列中所有的单元格对象组成的列表

table.row_types(rowx, start_colx=0, end_colx=None)    #返回由该行中所有单元格的数据类型组成的列表

table.row_values(rowx, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表

table.row_len(rowx) #返回该列的有效单元格长度




ncols = table.ncols   #获取列表的有效列数

table.col(colx, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表

table.col_slice(colx, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表

table.col_types(colx, start_rowx=0, end_rowx=None)    #返回由该列中所有单元格的数据类型组成的列表

table.col_values(colx, start_rowx=0, end_rowx=None)   #返回由该列中所有单元格的数据组成的列表



print (sheet1.col_values(0, 0, 5))    # 取第1列，第0~5行（不含第5行）
print (sheet1.row_slice(2, 0, 2))     # 获取单元格值类型和内容，同sheet1.row(0)
print (sheet1.row_types(1, 0, 2))     # 获取单元格数据类型


import xlrd
import xlwt
from xlutils.copy import copy

dir = os.path.abspath('.').split('src')[0]
'''主要逻辑实现'''
oldWb = xlrd.open_workbook(dir+"/data/考勤系统/考勤系统.xlsx");#先打开已存在的表
newWb = copy(oldWb)#复制
newWs = newWb.get_sheet(2);#取sheet表
newWs.write(2, 4, "pass");#写入 2行4列写入pass
newWb.save(dir+"/result/考勤系统.xls"); #保存至result路径