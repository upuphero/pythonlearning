import xlrd
import xlwt



def main():
    # 打开文件
    data = xlrd.open_workbook(r'30180.xlsx')
    # 获取所有sheet的名字
    print(data.sheet_names())
    # sheet1索引从0开始，得到sheet1表的句柄
    sheet1 = data.sheet_by_index(0)
    sheet2 = data.sheet_by_index(1)
    sheet3 = data.sheet_by_index(2)
    sheet4 = data.sheet_by_index(3)
    sheet5 = data.sheet_by_index(4)
    

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
    rowNum4 = sheet4.nrows
    rowNum5 = sheet5.nrows
    #print("rowNum1=",rowNum1)
    #print("rowNum3=",rowNum3)

    # 创建一个workbook 设置编码
    f = xlwt.Workbook(encoding = 'utf-8')
    # 创建sheet
    sheet = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
    row0 = [u'序号',u'学号', u'姓名']
    column0 = [0]*rowNum3     
    # 生成第一行
    for i in range(0, len(row0)):
        sheet.write(0, i, row0[i], set_stlye('Times New Roman', 220, True))
    # 生成第一列
    for i in range(0, len(column0)):
        sheet.write(i+1, 0, column0[i], set_stlye('Times New Roman', 220, True))
        
    for i in range(0,rowNum3):
        a= int(sheet3.cell_value(i, 0))
        print(i+1)
        for j in range(1,rowNum5):
            b= int(sheet5.cell_value(j, 0))
            c= sheet5.cell_value(j, 1)
            if b == a:
                #print(a,c)     
                sheet.write(i+1, 0, i+1,set_stlye('Times New Roman', 220, True))
                sheet.write(i+1, 1, a,set_stlye('Times New Roman', 220, True))
                sheet.write(i+1, 2, c,set_stlye('Times New Roman', 220, True))
                break
            if j== rowNum1-1:
                sheet.write(i+1, 0, i,set_stlye('Times New Roman', 220, True))
                sheet.write(i+1, 1, a,set_stlye('Times New Roman', 220, True))
                print('\n')
    
    for i in range(0,rowNum3):
        a= int(sheet3.cell_value(i, 0))
        print(i+1)
        for j in range(1,rowNum4):
            d= int(sheet4.cell_value(j, 0))
            e= sheet4.cell_value(j, 1)
            if d == a:
                #print(a,c)     
                sheet.write(i+1, 0, i+1,set_stlye('Times New Roman', 220, True))
                sheet.write(i+1, 1, a,set_stlye('Times New Roman', 220, True))
                sheet.write(i+1, 2, e,set_stlye('Times New Roman', 220, True))
                break
                
    f.save('finalfile.xls')

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

if __name__ == '__main__':
    main()