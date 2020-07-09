import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
count =0
total = 0

ctx = ssl.create_default_context()
ctx.checkhostname = False
ctx.verifymode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_263402.html"
html = urllib.request.urlopen(url,context= ctx).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('tr')
for tag in tags:
  #  print(tag.contents[0])
    name = soup('td')
    for nam in name:
     try:
         print(nam.contents[0])
     except:
        continue

