import re
file=open('regrex.txt')
li = list()
sum=0
for line in file:
 line = line.rstrip()
 flt = re.findall('[0-9]+',line)
 li.append(flt)
for x in li:
    for y in x:
        fy = int(y)
        sum = sum + fy

print(sum)