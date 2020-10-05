import os
import xlrd,sys
import xlwt
from xlutils.copy import copy

def main():
    data = xlrd.open_workbook(r'30180.xlsx')
    sheet1 = data.sheet_by_name("name")
    sheet2 = data.sheet_by_name("number")
    print ('sheet_names:', data.sheet_names()) # 获取所有sheet名字
    print ('sheet_number:', data.nsheets)        # 获取sheet数量


def find():
    data = xlrd.open_workbook(r'30180.xlsx')
    sheet1 = data.sheet_by_name("name")
    sheet2 = data.sheet_by_name("number")
    print (sheet1.col_values(6))   # 取第7列

    
    table = workfile.sheets()[0]
    nrows = table.nrows#nrows有效行数
    for i in range(0,nrows):
        Ndangqian_List = table.row_values(i)#当前行资料 list list[1]为名字
        z = 0
        for c in range(0,len(Ndangqian_List)):
            if Name == Ndangqian_List[z]:#Ndangqian_List[] z += 1 每一格的资料，遍历列表每个元素
                return table.row_values(i)
            z += 1
    return [Name]


def match():


def write():
    newWb = copy(oldWb)#复制
    newWs = newWb.get_sheet(2);#取sheet表
    newWs.write(2, 4, "pass");#写入 2行4列写入pass
    newWb.save(dir+"/result/考勤系统.xls"); #保存至result路径   





print (sheet1.row_values(0))  # 获取第一行所有内容，合并单元格，首行显示值，其它为空。


print ("sheet2 row num:", sheet2.nrows)  # get sheet all rows number
print ("sheet2 col num:", sheet2.ncols)  # get sheet all columns number
print (sheet2.col_values(1))   # 取第2列

