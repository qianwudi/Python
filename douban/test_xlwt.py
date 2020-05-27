#-*- coding = utf-8 -*-
#@TIME: 2020/5/26 16:48
#@FILE: test_xlwt.py
#@software: PyCharm

import xlwt

#9X9乘法表

workbook = xlwt.Workbook(encoding="utf-8")#创建Workbook对象
worksheet = workbook.add_sheet('sheet')#创建工作表

for hang in range(1,10):
    for lie in range(1,hang+1):
        dat = str(hang)+"X"+str(lie)+"=%d"%(hang*lie)
        print(dat,end="\t")
        worksheet.write(hang-1, lie-1, dat)  # 第一个参数为行，第二个参数为列，第三个参数为内容
    print("\n")


workbook.save('test.xls')#保存数据


