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
'''st='python narayana'
def string(st):
    st=input('enter any string:')
    a=[]
    for i in st:
        if i in 'aeiou':
            a.append(i)
        else:
            a.append(i)
                 
    print(''.join(a))
string(st)
'''
#12
'''string='narayana'
vowels=['a','e','i','o','u']
s=""
for i in range(len(string)):
    if string[i] not in vowels:
        s=s+string[i]
print('removing vowels:',s)'''
#15
'''st=input('enter a string:')
st=st.split()
if len(st)>5:

   print('lenghty string')
else:
   print('small string') 
'''
#13
'''s=input('enter a string:')
r=len(s)//2
x=s[0:r]
y=s[r:]

print(y+x)'''
#7
'''st=' python narayana tech house'
s=''
for i in st:
   if i in 'aeiou':
      s=s+'*'
   else:
      s=s+i
print(s)'''
       

