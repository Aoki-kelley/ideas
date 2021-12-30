import re
html=input('输入:')
p=re.compile('href="[^"]*?[\s\S]*?"')
url=p.findall(html)
if url!=[]:
    for i in url:
        target=i.replace('href=','')
        target=target.replace('"','')
        print(target)
else:
    print('Not Found')