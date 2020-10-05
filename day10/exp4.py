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
    # sheet1索引从0开始，得到sheet1表的句柄
    sheet1 = data.sheet_by_index(0)
    sheet2 = data.sheet_by_index(1)
    sheet3 = data.sheet_by_index(2)
    #sheet1 = data.sheet_by_name("name")
    #sheet2 = data.sheet_by_name("number")
    #print ('sheet_names:', data.sheet_names()) # 获取所有sheet名字
    print ('sheet_number:', data.nsheets)        # 获取sheet数量

    #print("获取第1列内容:", sheet3.col_values(0))
    # 第一列数据
    cols3_1 = sheet3.col_values(0)
    #第七列数据
    cols1_7 = sheet1.col_values(6)
    rowNum1 = sheet1.nrows
    rowNum2 = sheet2.nrows
    rowNum3 = sheet3.nrows
    #print("rowNum1=",rowNum1)
    #print("rowNum3=",rowNum3)

    for i in range(0,rowNum3):
        a= int(sheet3.cell_value(i, 0))
        print(i+1)
        for j in range(1,rowNum1):
            b= int(sheet1.cell_value(j, 6))
            c= sheet1.cell_value(j, 1)
            if b == a:
                
                print(a,c)
                print('\n')
                break
            if j== rowNum1-1:
                print(a)
                print('\n')

            



if __name__ == '__main__':
    read_excel()