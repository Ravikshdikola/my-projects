import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ' http://py4e-data.dr-chuck.net/comments_263404.xml'
html = urllib.request.urlopen(url,context=ctx).read()
tion = ET.fromstring(html)
list = tion.findall('comments/comment')
sum =0
for item in list:

    sum = sum + (int(item.find('count').text))
   ## print(sum)
    print('name',item.find('name').text)
    print('count',item.find('count').text)
print(sum)