#-*- coding = utf-8 -*-
#@TIME: 2020/5/26 12:29
#@FILE: test_bs4.py
#@software: PyCharm

#文档解析
from bs4 import BeautifulSoup
'''

- 1.Tag
- 2.NacigableString
- 3.BeautifulSoup
- 4.Comment

'''

file = open("baidu.html","rb")#二进制读取

html = file.read()
bs = BeautifulSoup(html,"html.parser")  #"html.parser"解析器,解析网页的标签

'''
print(bs.title)
print(bs.a)
print(type(bs.head))                    #1.Tag  标签及其内容：只能拿到第一个标签

print(bs.title.string)                  #2.NacigableString 标签里的内容（字符串）

print(bs.a.attrs)                       #标签里的属性

print(type(bs))                          #3.BeautifulSoup表示整个文档
print(bs)

print(bs.a.string)
print(type(bs.a.string))                 #4.Comment 是一个特殊的NacigableString 输出内容不包括注释符号

'''

#文档的遍历文档树

#print(bs.head.contents)
# print(bs.head.contents[1])               #列表


#文档的搜索
#1.直接查找"a"标签 字符串过滤：会查找与字符完全一样的内容
# t_list = bs.find_all("a")
# print(t_list)

import re

'''
#2 正则表达式搜索 使用search()方法匹配内容
t_list = bs.find_all(re.compile("a"))
#标签里包含”a“全部被搜索
print(t_list)

#方法 传入一个函数，根据函数要求来搜索
#了解
def name_is_exists(tag):
    return tag.has_attr("name")
t_list = bs.find_all(name_is_exists)

for item in t_list:
    print(item)

'''

#kwargs   参数
# t_list = bs.find_all(id = "head")
#
# for item in t_list:
#     print(item)

#text 参数
#t_list = bs.find_all(text = ["hao123","新闻","地图"])
# t_list = bs.find_all(text= re.compile(("\d")))#应用正则表达式查找特定文本里的内容（标签里的字符串）
# for item in t_list:
#     print(item)
#limit 参数
# t_list = bs.find_all("a",limit=3)#指定搜索3个
# for item in t_list:
#     print(item)

#css 选择器

t_list = bs.select("title")#通过标签查找
#
# t_list = bs.select(".mnav")#通过类名查找
#
# t_list = bs.select("#u1") #按id查找
#
# t_list = bs.select("a[class='s-bri']") #通过属性查找

#t_list = bs.select("head > noscript") #通过子标签查找

for item in t_list:
    print(item)






