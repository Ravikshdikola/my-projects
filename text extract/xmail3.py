import urllib.request
import xml.etree.ElementTree as ET

result = 0

url ='http://py4e-data.dr-chuck.net/comments_263404.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read() # so it will read all the contents in the link
#print(data)
print('Retrieved', len(data), 'characters') # so this line basically retrived the length of the data
tree = ET.fromstring(data)

counts = tree.findall('.//count') # so the tag count is inside the comments and comment so that's why it uses double slash  to find count
print("Count:",len(counts)) # so number of count tag
for count in counts:   # this loop select the count value inside the count
    value = count.text   # it takes the value inside the count
    result = result + int(value) # it adds the value of the count
print("Sum: ",result)
