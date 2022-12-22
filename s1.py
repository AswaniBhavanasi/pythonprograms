#1
'''lst = [10,20,30,40,50,60,70,80,90,100]
lst1=[]
lst2=[]
for i in range(len(lst)):
    if i%2==0:
        lst1.append(lst[i])
    else:
        lst2.append(lst[i])
print("Even elements: ",lst2)
print("Odd elements: ",lst1)
'''
#2
'''dict={'ename':'aswani','salary':20000,'company':'tcs'}
print(dict)
dict['loc']='hyd'
print(dict)
'''
#3.
'''dict1={'sname':'sai','salary':10000,'location':'hyd'}
print(dict1)
dict1['salary']=30000
print(dict1)
'''
#4
'''st='python narayana tech house'
def string(st):
    st=input('enter any string:')
    a=[]
    for i in st.split():
        a.append(''.join(i[0].upper()+i[1:]))
    print(''.join(a))
string(st)'''
#6
'''st='python narayana tech house HYDERABAD'
def string(st):
    st=input('enter any string:')
    a=[]
    for i in st:
        if i in 'aeiou':
            a.append(i.upper())
        else:
            a.append(i.lower())
            
    print(''.join(a))
string(st)'''
#5
'''st='python narayana tech house hyderabad'
def string(st):
    st=input('enter any string:')
    a=[]
    for i in st.split(' '):
        a.append(''.join(reversed(i)))
    print(' '.join(a))
string(st)
'''
#8
'''st='pythoin narayana'
def string(st):
    st=input('enter any string:')
    a=[]
    for i in st:
        if i in i.upper():
            a.append(i)
        else:
            continue
    for i in st:
        if i in i.lower():
            a.append(i)
        else:
            continue
    print(''.join(a))
string(st)
'''
 
#7
'''st='python narayana'
def string(st):
    st=input('enter any string:')
    a=[]
    b=[]
    for i in st:
        if i in 'aeiou':
            a.append(i)
        else:
            b.append(i)

    print(''.join(a+b))
string(st)
'''
#9
'''st='python narayana'
def string(st):
    st=input('enter any string:')
    a=[]
    b=[]
    for i in st:
        if i in 'aeiou':
            a.append(i)
        else:
            b.append(i)
    print('vowels are:',len(a))
    print('consonants are:',len(b))
string(st)'''
#10
'''lst=[10,45,30,67,23,43]
def list(lst):
    lst=[10,45,30,67,23,43]
    a=sorted(lst)
    print(a[-1])

list(lst)
'''
#11
'''lst=[10,'NTH',True,11,'python',False,12]
newlst=[]
for i in lst:
    if type(i) is int:
        newlst.append(i)
print(newlst)'''

#12
'''lst=[100,200,300,150,'NTH','python']
def index(lst):
    a=eval(input('enter any element from lst:'))
    b=lst.index(a)
    print(format(a),'index position is',format(b))
index(lst)'''
#14
'''n=eval(input('enter any 3 numbers:'))
for i in n:
    if str(i) in str(max(n)):
        print(i)
'''
        
#13
'''st='NARAYANA Tech House'
def string(st):
    st=input('enter any string:')
    a=[]

    for i in st.split(' '):
        a.append(i[0])
    print(' '.join(a))
string(st)
'''
    
#15
'''n=input('enter  your string:')
vowels=0
consonants=0
for i in n:
    if(i=='a' or i=='e' or i=='i'or i=='o'or i=='u' or i=='A' or i=='E' or i=='I' or i=='o' or i=='u'):
        vowels=vowels+1
    elif i!=' ':
        consonants=consonants+1
print('total number of vowels in the  string=',vowels)
print('total number of consonants in  the string=',consonants)
if vowels>consonants:
    print('vowels dominated string')
elif vowels<consonants:
    print('consonants dominated string')
elif vowels==consonants:
    print('raise error ,equal vowels and consonants error')'''

#16
'''def string(s):

    t=[]
    st='abcdefghijklmnopqrstvuwxyzABCDEFGHIJKLMNOPQRSTVUWXYZ'
    for i in s:
        h=st.index(i)
        t.append(st[h+1])
    p=''.join(t)
    print(p)
s=input('enter any string:')    
string(s)'''
