import xml.etree.ElementTree as ET
data = '''
<person>
<name>Chuck</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes" />
</person>'''
tree = ET.fromstring(data)
#print(tree)  <Element 'person' at 0x7fc855c42f50> so this basically extract main element in xml document at its location and made it as xml tree structure format  so that it can able to acess its component inside it
print("phone:",tree.find('phone').text)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))