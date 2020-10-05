 
 
import os
import xlrd
import xlwt
# 打开文件
data = xlrd.open_workbook(r'30180.xlsx')
# 获取所有sheet的名字
print(data.sheet_names())
# 获取sheet的表明

# sheet1索引从0开始，得到sheet1表的句柄
sheet1 = data.sheet_by_index(0)
sheet3 = data.sheet_by_index(2)
#sheet1 = data.sheet_by_name("name")
#sheet2 = data.sheet_by_name("number")
#print ('sheet_names:', data.sheet_names()) # 获取所有sheet名字
print ('sheet_number:', data.nsheets)        # 获取sheet数量

# 第一列数据
cols3_1 = sheet3.col_values(0)
#第七列数据
cols1_7 = sheet1.col_values(6)
rowNum1 = sheet1.nrows
rowNum3 = sheet3.nrows

for i in range(rowNum3):
    for j in range(rowNum1):
        if sheet3.cell_value(i, 0) == sheet1.cell_value(j, 6):
                print(sheet1.cell_value(j, 1))
                print('\n')
