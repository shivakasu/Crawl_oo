# -*- coding: utf-8 -*-
import urllib2
import urllib
import cookielib
from bs4 import BeautifulSoup as BS



def dididi(id):
        login_page = "https://www.so.com/s?ie=utf-8&src=hao_search&shb=1&hsid=930a7fe755704a97&q=python"
        for i in range(1):
                cj = cookielib.CookieJar()
                opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
                opener.addheaders = [('User-agent','Mozilla/6.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
                op=opener.open(login_page)
                content=op.read()
                soup = BS(content,"html.parser")
                a = soup.find_all('input',attrs={'name':"psid"})[0]
                for aaa in a:
                    print(str(aaa)+"\n")
                data = urllib.urlencode({"q":"python","src":"srp","fr":"hao_search","psid":a})
                op=opener.open(login_page,data)
                content=op.read()
                soup2 = BS(content,"html.parser")
                qqq=soup2.prettify()
                print qqq

dididi("595")



