# -*- coding: utf-8 -*-
import urllib2
import urllib
import cookielib
import time

a=['14061206']
#for i in range(14061001,14061004):a.append(str(i))
#for i in range(14231001,14231100):a.append(str(i))
#for i in range(13061052,13061233):a.append(str(i))
#for i in range(13231001,13231100):a.append(str(i))
#for i in range(12061001,12061233):a.append(str(i))
#for i in range(12231001,12231100):a.append(str(i))

	

def dididi():
    login_page = "http://10.254.25.5/course/login/index.php"
    url = "http://10.254.25.5/course/blog/index.php?entryid=2494"
    url2 = "http://10.254.25.5/course/comment/comment_ajax.php"
    url3="http://10.254.25.5/course/blog/edit.php?action=reward&entryid=2494&blogpage"
    for i in range(len(a)):
        try:
            cj = cookielib.CookieJar()
            opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
            data = urllib.urlencode({"username":a[i],"password":"12345678"})
            opener.open(login_page,data)
            op=opener.open(url)
            content = op.read()
            sese = content.find("\"client_id\":\"")
            skey = content[sese+13:sese+26]
            sss2 = content.find("\"sesskey\":\"")
            skey2 = content[sss2+11:sss2+21]
            data2 = urllib.urlencode({
                "action":"add",
                "area":"format_blog",
                "client_id":skey,
                "content":"666",
                "component":"blog",
                "contextid":"1391",
                "courseid":"1",
                "itemid":"2494",
                "sesskey":skey2
                })
            print("1\n")
            op=opener.open(url2,data2)
            print("2\n")
            op=opener.open(url3)
            print("3\n")
            '''
            for j in range(515,525):
                data3 = urllib.urlencode({
                "action":"delete",
                "area":"format_blog",
                "client_id":skey,
                "component":"blog",
                "commentid":str(j),
                "contextid":"1391",
                "courseid":"1",
                "itemid":"2494",
                "sesskey":skey2
                })
                op=opener.open(url2,data3)
            '''
            print(a[i]+"\n")
            print op.read()
        except:
            print "error"

dididi()





