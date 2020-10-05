import os
import xlrd
import sys
import xlwt

data = xlrd.open_workbook(r'30180.xlsx')
sheet1 = data.sheet_by_name("name")
sheet2 = data.sheet_by_name("number")
print('sheet_names:', data.sheet_names())  # 获取所有sheet名字
print('sheet_number:', data.nsheets)        # 获取sheet数量


def read_excel():

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

    print("获取第1列内容:", sheet3.col_values(0))
    # 第一列数据
    cols3_1 = sheet3.col_values(0)
    #第七列数据
    cols1_7 = sheet1.col_values(6)
    rowNum1 = sheet1.nrows
    rowNum3 = sheet3.nrows

    for i in range(rowNum3):
        for j in range(rowNum1):
            a= int(sheet3.cell_value(i, 0))
            b= int(sheet1.cell_value(j, 6))
            if a == b:
                print(a)
                print('\n')



def set_stlye(name, height, bold=False):
    # 初始化样式
    style = xlwt.XFStyle()
    # 创建字体
    font = xlwt.Font()
    font.bold = bold
    font.colour_index = 4
    font.height = height
    font.name = name
    style.font = font
    return style


def write():
    f = xlwt.Workbook()
# 创建sheet1
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
    column0 = [u'学号', u'姓名']
    row0 = []

    # 生成第一行
    for i in range(0, len(row0)):
        sheet2.write(0, i, row0[i], set_stlye('Times New Roman', 220, True))

    # 生成第一列
    for i in range(0, len(column0)):
        sheet2.write(i+1, 0, column0[i],
                     set_stlye('Times New Roman', 220, True))
        f.save('file.xls')


if __name__ == '__main__':
    write()




import xlwt
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')

# 写入excel
# 参数对应 行, 列, 值
worksheet.write(1,0, label = 'this is test')

# 保存
workbook.save('Excel_test.xls')