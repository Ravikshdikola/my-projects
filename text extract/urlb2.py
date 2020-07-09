import urllib.request,urllib.parse,urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
dic = dict()
for lines in fhand:
    line = lines.decode().split()
    for words in line:
        dic[words] = dic.get(words,0)+1
print(dic)