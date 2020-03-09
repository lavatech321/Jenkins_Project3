import re
f1=open('details.txt','r')
l1=[]
for x in f1:
  line=re.split('\s',x)
  l1.append(line[0])
print(l1)
