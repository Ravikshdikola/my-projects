# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Nikolina.html'
count = input("enter the count")
pos = input("enter the position")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')
#print(tags) this will print all the tag inside the given url
for i in range(int(count)): # input symbol used for outside looping to count number of times we switches inside the web pages containning links
    links = []
    for tag in tags:
        jac = (str(tag.get('href',None)))
        links.append(jac)
    html = urllib.request.urlopen(links[int(pos) - 1], context=ctx).read() # this statement will grap the link  according to the position demanded by the user
    soup = BeautifulSoup(html, 'html.parser')
    print("Retrieving", links[int(pos) - 1])
    tags = soup('a')