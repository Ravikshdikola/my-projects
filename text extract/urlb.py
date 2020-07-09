import urllib.request,urllib.parse,urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    print(line.decode().strip())

## its better approach to exterct data as compare to socket because it doesnot include any header file so we can directly access the content of the file