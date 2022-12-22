#method overriding
'''class parentClass:
    def display(self):
        print('it parent method')
class childClass(parentClass):
    def display(self):
        print('it child method')
        super().display()
x=childClass()
x.display()'''
#method overloading
'''class Empdata:
    def display(self,a):
        print('it first method')
    def display(self,a,b):
        print('it second method')
    def display(self,a,b,c):
        print('it third method')
e=Empdata()
e.display(10,20,30)'''
#encapsulation
'''class Empdata:
    name='satya'
    salary=20000
    def working(self):
        print('he works full time')
    def updating(self):
        print('he update knowledge always')
e=Empdata()
print(e.name)
print(e.salary)
e.working()
e.updating()'''
#hierarchical inheritance
'''class A:
    a1=10
    def am1(self):
        print('it am1 method')
class B(A):
    b1=20
    def bm1(self):
        print('it bm1 method')
class C(A):
    c1=30
    def cm1(self):
        print('it cm1 method')
b=B()
print(b.b1)
b.bm1()
print(b.a1)
b.am1()
c=C()
print(c.c1)
c.cm1()
print(c.a1)
c.am1()'''
#mutliple inheritance
'''class A:
    a1=10
    def am1(self):
        print('it am1 method')
class B:
    b1=20
    def bm1(self):
        print('it bm1 method')
class C(A,B):
    c1=30
    def cm1(self):
        print('it cm1 method')
c=C()
print(c.c1)
c.cm1()
print(c.b1)
c.bm1()
print(c.a1)
c.am1()
'''
#multi-level inheritance
'''class A:
    a1=10
    def am1(self):
        print('it am1 method')
class B(A):
    b1=20
    def bm1(self):
        print('it bm1 method')
class C(B):
    c1=30
    def cm1(self):
        print('it cm1 method')
c=C()
print(c.c1)
c.cm1()
print(c.b1)
c.bm1()
print(c.a1)
c.am1()'''
#single inheritance
'''class A:
    a1=10
    def am1(self):
        print('it am1 method')
class B(A):
    b1=20
    def bm1(self):
        print('it bm1 method')
b=B()
print(b.b1)
b.bm1()
print(b.a1)
b.am1()'''
#data abstraction
'''class Empdata:
    name='sai'
    company='tcs'
    __salary=1000
    __age=25
    def display(self):
        print('he is {} yeras old ang getting {} salary'.format(Empdata.__age,Empdata.__salary))
e1=Empdata()
print(e1.name)
print(e1.company)
e1.display()'''
#class and object
'''class studentdata:
    name='ashu'
    marks=90
    iname='nth'
    def learning(self):
        print('student always learn subject')
    def reading(self):
        print('students always read whatsapp msgs')
s1=studentdata()
print(s1.name)
print(s1.marks)
print(s1.iname)
s1.learning()
s1.reading()'''
#reprograms
'''data='iam working in TCS Company near by INFOSYS Company but  my friend is working in WIPRO Company' 
import re
m=re.findall('[A-Z]{1,} Company',data)
print(m)

print([i.replace(' Company','')for i in re.findall('[A-z]{1,} Company',data)])
'''
#local variables
'''def display():
    a=10
    print(a)
display() '''
#global variables
'''a=10
print(a)
def display():
    global a
    a=90+a
    print(a)
display()
print(a)'''
#return statement
'''def display():
    a=10
    b=90
    c=a+b
    return c

x=display()
print(x)
print(x)'''

# pickling
'''import pickle
names=['sai','ashu','python',3000,'computer']
file=open('pickledata.txt','wb')
pickle.dump(names,file)
file.close()'''
#unpickling
'''import pickle
with open('pickledata.txt','rb') as file:
    names1=pickle.load(file)
    print(names1)
'''
