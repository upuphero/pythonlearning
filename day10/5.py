import os
import xlrd,sys
import xlwt

def main():
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('入职员工')
    with open('.\名字.txt') as f:
        h = 0
        line = f.readline()
        while line:
            line = line.replace('\r', '').replace('\n', '').replace('\t', '')
            # print(line)
            Meiyitiao = Ex_Find(line)
            print(Meiyitiao)
            i = 0
            for zhi in Meiyitiao:
                # 写入excel
                # 参数对应 行, 列, 值
                worksheet.write(h, i, label=zhi)
                i += 1
            h += 1
            line = f.readline()
        workbook.save('入职员工资料.xls')

def Ex_Find(number):
    workfile = xlrd.open_workbook('excelFile.xls')
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

if name == 'main':
    main()
