#-*- coding = utf-8 -*-
#@TIME: 2020/5/26 12:29
#@FILE: main.py
#@software: PyCharm


import urllib.request,urllib.error
#import urllib.parse
from bs4 import BeautifulSoup
import re
import parser
import xlwt

#获取一个网页内容，模拟电脑爬取网址
def askURL(url):

    header = {  #字典
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"

    }
    #1.获取网络信息
    request = urllib.request.Request(url=url,headers=header)#将头文件打包编码，伪装爬虫模拟浏览器访问网站
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")#将爬取的内容进行解析编码utf-8
        print(type(html))
    except urllib.error.URLError  as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e, "reson"):
            print(e.reason)
    return html
#response = urllib.request.urlopen("https://movie.douban.com/top250?start=")
#HTTP Error 418:网页已识别为爬虫，禁止访问，要模拟浏览器访问，伪装爬虫

#获取250条数据,爬取网页，分析数据
def GetData(url):
    print("开始获取网页内容并分析数据")
    baseData = []
    for i in range(0,10):
        html = askURL(url + str(i * 25))  #访问10页，每页25条网站
#        f.writelines(baseData)

    #2.逐一进行解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):#查找符合要求的字符串
            #print(item)#测试全部信息
            dat = []            #保持一部电影的全部信息
            item = str(item)    #item是<class 'bs4.element.Tag'>
            link = re.findall(findLink,item)[0] #re库通过正则表达式查找指定字符串,查找链接
            dat.append(link)
            img = re.findall(findImgSrc,item)[0]
            dat.append(img)
            title = re.findall(findTitle,item)
            if len(title) == 2:
                ctitle = title[0]
                dat.append(title)#添加中文名
                otitle = title[1].replace("/","")#去掉无关的符合
                dat.append(otitle)#添加外国名
            else:
                dat.append(title[0])
                dat.append(' ')

            rating = re.findall(findRating, item)[0]
            dat.append(rating)

            Judge = re.findall(findJudge, item)[0]
            dat.append(Judge)

            Inq = re.findall(findInq, item) #添加概述，可能没有概述
            if len(Inq) != 0:
                inq = Inq[0].replace('。',",")#去掉句号
                dat.append(Inq)
            else:
                dat.append(' ')

            Bd = re.findall(findBd, item)[0]
            Bd = re.sub('<br(\s+)?/>(\s+)?'," ",Bd)#<br>换成空格
            Bd = re.sub("/"," ",Bd)#/换成空格
            dat.append(Bd.strip())#去掉空格
            baseData.append(dat)
    return baseData

#保存数据到表格中
def SaveData(datalist,path):
    print("开始保存数据！")
    print("save....")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建Workbook对象
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)  # 创建工作表
    col = ("电影链接","图片链接","影片中文名","影片英文名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        dat = datalist[i]
        for j in range(0,8):
            sheet.write(i+1, j, dat[j])
    book.save(path)


def main():

    datalist = GetData(url)
    SaveData(datalist,savepath)


#定义网址
url = "https://movie.douban.com/top250?start="

#影片链接的规则
findLink = re.compile(r'<a href=(.*?)">')#创建对象，表示规则(字符串的模式)
#影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)#re.S让换行符包括在内
#影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片的评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#影片评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#影片概括
findInq = re.compile(r'<span class="inq">(.*)</span>')
#影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)#忽视换行符

#f = open("豆瓣TOP250.html","w",encoding="utf-8")


savepath = "豆瓣电影Top250.xls"
if __name__ == "__main__":
    print("begin....！")

    main()
    print("爬虫爬取完毕")











