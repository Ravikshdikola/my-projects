import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
count = 0
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verifymode = ssl.CERT_NONE

#url = input("Enter -")
url = " http://py4e-data.dr-chuck.net/known_by_Nikolina.html"
html = urllib.request.urlopen(url,context=ctx).read()
#print(html) it reads all the data in html format and also include /r/n for next line so doesnot any proper space to show data
soup = BeautifulSoup(html,'html.parser')
tag = soup('a')
#print(soup) #it reads the data but eliminate all /r/n and provide new line to each html coontent to show how it looks actually
#print(tag)
for ur in tag:
    count = count + 1
    if count ==18:
      print(ur.get('href',None))
      #this will retrieve the contents with the link
      jaco = ur.contents[0]
      print(jaco)



