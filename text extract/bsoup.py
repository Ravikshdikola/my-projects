import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verifymode = ssl.CERT_NONE

#url = input("Enter -")
url = " https://www.geeksforgeeks.org/"
html = urllib.request.urlopen(url,context=ctx).read()
#print(html) it reads all the data in html format and also include /r/n for next line so doesnot any proper space to show data
soup = BeautifulSoup(html,'html.parser')
tag = soup('a')
#print(soup) it reads the data but eliminate all /r/n and provide new line to each html coontent to show how it looks actually
for tags in tag:
    # this tag is used to pull out the links from the other website
    print(tags.get('href',None))
    # this line shows if we get href tag so print it otherwise ignore other tags given inside it