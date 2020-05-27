#-*- coding = utf-8 -*-
#@TIME: 2020/5/26 12:29
#@FILE: test_re.py
#@software: PyCharm

'''
re.search()
re.math()
re.findall()
re.sub()
'''
#正则表达式：字符串模式 判断字符串是否符合一定的标准

import re

#创建模式对象

pat = re.compile("AA")  #此处的AA是正则表达式 用来验证其他字符串
# m = pat.search("CBA")   #search字符串被检验的内容
# m = pat.search("ABCAA")
m = pat.search("ABCAADDCCAA")#search进行比对查找只找到第一个字符，并告诉你位置
print(m)

#没有模式对象
m = re.search("asd","Aasd") #前面的字符串是规则，后面字符串是被校验的对象
print(m)


m = re.findall("a","ASDaDFGAa")#前面的字符串是规则，后面字符串是被校验的对象
print(m)

m = re.findall("[A-Z]","ASDaDFGAa")#前面的字符串是规则，后面字符串是被校验的对象
print(m)

m = re.findall("[A-Z]+","ASDaDFGAa")
print(m)

#sub 分割 替换
print(re.sub("a","A","abcdaa")) #在abcd到a用A替换，

#建议在正则表达式中，被比较的字符串前加r,不用担心转义字符的问题

a = r"asd\na\c"
print(a)



