#1
'''import calendar as c
for i in c.day_name:
    print(i)'''
#2
import calendar as c
'''for i in c.day_name :
     if i[0] =='T':
         print(i)'''

#3
'''for i in c.day_name :
    if i.count('e')>=2:
        print(i)'''
#4
'''lst=[]
for i in c.day_name :
    lst.append(len(i))
for i in c.day_name:
    if len(i)==max(lst):
        print(i)'''
#5
'''lst=[]
for i in c.day_name :
    lst.append(len(i))
for i in c.day_name:
    if len(i)==min(lst):
        print(i)'''
#6
lst=[]
import re
for i in c.day_name:
    lst.append(len(re.findall('[aeiou]',i)))
for i in c.day_name:    
    if len(re.findall('[aeiou]',i))==max(lst):
        print(i)
#7
lst=[]
import re
for i in c.day_name:
    lst.append(len(re.findall('[^aeiou]',i)))
for i in c.day_name:    
    if len(re.findall('[^aeiou]',i))==max(lst):
        print(i)       
#8
for i in c.day_name:
    if len(i)==8:
        print(i)
