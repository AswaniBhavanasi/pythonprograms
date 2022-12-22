a=open('empdata.txt','w')
a.write('Mr.Sai,9090909090,sai@gmail.com,AB 12 XY 1234,04/12/2000,TCS Company,ABCDE1234D\n8789878987Mr.Nani,BNBVG2345D,BN12MN2345,Wipro Company,nani123@gmail.com,8/11/1999\nInfosys Company,satya_i@gmail.com,OD 34 x 9876,31/01/1998,PERAN12,Mrs.Satya,9988998899\nMNBFD1234R,rojan@gmail.com,TS23 AX 1234,1/1/1990,CTS Company,Mr.Rohan,8179817681')
a.close()
a=open('empdata.txt').read()
print(a)

import re
#1.write a program to fetch all emplyoees names
a=open('empdata.txt').read()
b=re.findall('[A-Z]{1}[a-z]{1,2}[.][A-Z]{1}[a-z]{1,}',a)
print(b)

#2.write a program to fetch all mobile numbers in the file

a=open('empdata.txt').read()
b=re.findall('[6-9]{1}[0-9]{9}',a)
print(b)

#3.write a progrma to fetch all pan numbers from file

a=open('empdata.txt').read()
b=re.findall('[A-Z]{5}[0-9]{4}[A-Z]{1}',a)
print(b)

#4.write a program to fetch all mail ids from files

a=open('empdata.txt').read()
b=re.findall('[a-z]{1,}[_]*[a-z]*[0-9]*[@][a-z]{1,}[.][a-z]{1,}',a)
print(b)

#5.write a program to fetch all registration numbers from the file

b=open('empdata.txt').read()
a=re.findall('[A-Z]{1,2}[ ]?[0-9]{1,2}[ ]?[a-zA-Z]{1,2}[ ]?[0-9]{1,4}',b)
print(a)

#6.write a program to fetch all company names

a=open('empdata.txt').read()
b=re.findall('[A-Z]{1,}[a-z]*[ ]?[A-Z]{1,}[a-z]{1,}',a)
print(b)

#7.write a program to fetch all date of births

a=open('empdata.txt').read()
b=re.findall('[0-9]{1,}[/.][0-9]{1,}[/.][0-9]{1,}',a)
print(b)

#8.write a program to fetch company name mr.sai

a=[i for i in open('empdata.txt').readlines() if 'Mr.Sai' in i]
for i in a:
    x=re.findall('[A-Z]{3}[ ]?[A-Z]{1}[a-z]{1,}',i)
    print(x)

#9.write a program to fetch emild id of mr.rohan

a=[i for i in open('empdata.txt').readlines() if 'Mr.Rohan' in i]
for i in a:
    x=re.findall('[a-z]{1,}[_]*[a-z]*[0-9]*[@][a-z]{1,}[.][a-z]{1,}',i)
    print(x)

#10.write a program to fetch employee name who is using 9090909090

a=[i for i in open('empdata.txt').readlines() if '9090909090' in i]
for i in a:
    x=re.findall('[A-Z]{1}[a-z]{1,2}[.][A-Z]{1}[a-z]{1,}',i)
    print(x)

#11.write a program to fetch  pan number of mr.satya

a=[i for i in open('empdata.txt').readlines() if 'Mrs.Satya' in i]
for i in a:
    x=re.findall('[A-Z]{5}[0-9]{4}[A-Z]{1,}',i)
    print(x)

#12.write a program to fetch contact number of both nani and satya

a=[i for i in open('empdata.txt').readlines() if 'Mrs.Satya' in i or 'Mr.Nani' in i]
for i in a:
    x=re.findall('[6-9]{1}[0-9]{9}',i)
    print(x)

#13.write a program to fetch emp names of infosys and tcs companies

a=[i for i in open('empdata.txt').readlines() if 'Infosys Company' in i or 'TCS Company' in i]
for i in a:
    x=re.findall('[A-Z]{1}[a-z]{1,2}[.][A-Z]{1}[a-z]{1,}',i)
    print(x)

#14.write a program to fetch dob of tcs employee

a=[i for i in open('empdata.txt').readlines() if 'TCS Company' in i]
for i in a:
    b=re.findall('[0-9]{1,}[/.][0-9]{1,}[/.][0-9]{1,}',i)
    print(b)

#15.write a program to fetch birth year of mr.nani

a=[i for i in open('empdata.txt').readlines() if 'Mr.Nani' in i]
for i in a:
    b=re.findall('[/][0-9]{4}',i)
for i in b:
    print(i.replace('/',''))

#16.write a program to fetch the empname whose mobile number starts with 8
a=[i for i in open('empdata.txt').readlines() if i.startswith('8')]
for i in a:
    b=re.findall('[A-Z]{1}[a-z]{1,2}[.][A-Z]{1}[a-z]{1,}',i)
    print(b)

#17.write a program to fetch odisha emp name

a=[i for i in open('empdata.txt').readlines() if 'OD 34 x 9876' in i]
for i in a:
    x=re.findall('[A-Z]{1}[a-z]{1,2}[.][A-Z]{1}[a-z]{1,}',i)
    print(x)

#18.write a program to fetch youngest employee name
a=open('empdata.txt').read()
b=re.findall('[0-9]{1,}[/.][0-9]{1,}[/.][0-9]{1,}',a)
print(b)
for i in b:
    if min(b) in i:
        print(i)
        x=re.findall('[A-Z]{1}[a-z]{1}[.][A-Z]{1}[a-z]{2}',i)
        print(x)
#19.write a program to fetch all male employees

a=[i for i in open('empdata.txt').readlines() if 'Mr.' in i]
l=[]
for i in a:
    b=re.findall('[A-Z]{1}[a-z]{1}[.][A-Z]{1}[a-z]{1,}',i)
    l.append(b)
print(l)

#20.write a program to fetch total count of female employees

a=[i for i in open('empdata.txt').readlines() if 'Mrs.' in i]
l=[]
for i in a:
    b=re.findall('[A-Z]{1}[a-z]{2}[.][A-Z]{1}[a-z]{1,}',i)
    l.append(b)
print(len(l))

#21.write a program to fetch all employees names who born in january

a=[i for i in open('empdata.txt').readlines() if '/1/' in i or '/01/' in i]
for i in a:
    b=re.findall('[A-Z]{1}[a-z]{1,}[.][A-Z]{1}[a-z]{1,}',i)
    print(b)

#22.write a program to fetch contact number of telangana employee

a=[i for i in open('empdata.txt').readlines() if 'TS23 AX 1234' in i]
for i in a:
    x=re.findall('[6-9]{1}[0-9]{9}',i)
    print(x)

#23.write a program to fetch company name and mobile number of wipro employee'''
a=[i for i in open('empdata.txt').readlines() if 'Wipro' in i]
for i in a:
    b=re.findall('[A-Z]{1,}[a-z]*[ ]?[A-Z]{1,}[a-z]{1,}',i)
    c=re.findall('[6-9]{1}[0-9]{9}',i)
    print(b+c)

#24.write a program to fecth emp name who born in leaf year
a=[i for i in open('empdata.txt').readlines() if year%4==0 ]
for i in a:
    b=re.findall('[A-Z]{1}[a-z]{1,}[.][A-Z]{1}[a-z]{1,}',i)
    print(b)
#25.write a program to fetch all details of emp whose name not ends with vowel,
    
a=[ i for i in open('empdata.txt').readlines() if i[-1] not in'aeiouAEIOU']
for i in a:
    b=re.findall('[A-Z]{1}[a-z]{1,}[.][A-Z]{1}[a-z]{1,}',i)
    print(b)
