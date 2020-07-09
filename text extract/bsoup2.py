import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
count =0
total = 0

ctx = ssl.create_default_context()
ctx.checkhostname = False
ctx.verifymode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_263402.html"
html = urllib.request.urlopen(url,context= ctx)
soup = BeautifulSoup(html,'html.parser')
tags = soup('span')
for tag in tags:
    try:

        total = total + int(tag.contents[0])
        count = count + 1
    except:
        continue

print('count',count)
print('sum',total)