#统计单词总字数

import re

with open('Little Prince.txt','r')as f:
    data = f.read()
result = re.split(r"[^a-zA-Z]",data)
print (len([x for x in result if x!= '']))
f.close()
