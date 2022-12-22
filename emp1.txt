data=open('empdata1.txt').read()
print(data)

import re
#1 write a program  to fetch all names?
a=open('empdata1.txt').read()
print(a)
b=re.findall('[A-Z][a-z][s]?[.][A-Z]?[a-z]{1,}',a)
print(b)

#2 write a program to fetch  all emails?
a=open('empdata1.txt').read()
b=re.findall('[a-z_0-9.]{1,}[@][a-z]{2,5}[.][a-z]{2,3}',a)
print(b)

#3 write a program to fetch all companys?
a=open('empdata1.txt').read()
b=re.findall('[A-Z]{1,}[a-z]*[ ]?[A-Z]{1,}[a-z]{1,}',a)
lst=[]
for i in b:
    lst.append(i.replace(' Company',''))
print(lst)
#4 write a program to fetch  all moblie numbers?
a=open('empdata1.txt').read()
b=re.findall('[8-9]{1}[0-9]{9}',a)
print(b)
#5 write a program to fetch all date of births?
a=open('empdata1.txt').read()
b=re.findall('[0-9]{1,}[-][0-9]{1,}[-][0-9]{1,}',a)
print(b)
#6 write a program to fetch all pan numbers?
a=open('empdata1.txt').read()
b=re.findall('[A-Z]{5}[0-9]{4}[A-Z]{1}',a)
print(b)
#7
   
