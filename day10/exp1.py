import os
import xlrd
import sys
import xlwt

def set_stlye(name, height, bold=False):
    # 初始化样式
    style = xlwt.XFStyle()
    # 创建字体
    font = xlwt.Font()
    font.bold = bold
    font.height = height
    font.name = name
    style.font = font
    return style


# 创建一个workbook 设置编码
f = xlwt.Workbook(encoding='utf-8')
# 创建sheet1
sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
row0 = [u'序号', u'学号', u'姓名']
for i in range(1,10):
    column0 = [i]
# 生成第一行
for i in range(0, len(row0)):
    sheet1.write(0, i, row0[i], set_stlye('Times New Roman', 220, True))
# 生成第一列
for i in range(0, len(column0)):
    sheet1.write(i+1, 0, column0[i],set_stlye('Times New Roman', 220, True))
    f.save('file.xls')
