'''p=eval(input('enter your percentage:'))
if p>=35:
  print('you are passed on the exam')
  print('congratulations')
  print('where is the party?')
'''
#
'''
age=eval(input('enter your age:'))
if age>=18:
         
  print('you are {} years old'.format(age))
  print('you can apply for your vote')
  print('you can use www.nth.com')  

  '''
#
'''
p=eval(input('enter your percentage:'))
if p>=35:
  print('you are passed on the exam')
  print('congratulations')
  print('where is the party?')
else:
  print('you are failed in the exam')
  print('better luck next time')
  print('dont worry we will have party to forget failure')
  
'''
#
'''
course=input('which course you are learning?:')
if course=='python':
    print('ok, its good course')
else:
    print('you have to learn python to get job easily')
'''
#
'''
n1=eval(input('enter first number:'))
n2=eval(input('enter second number:'))
if n1>n2:
    print('{} is highest number between {} and {}'.format(n1,n1,n2))
else:
    print('{} is highest number between {} and {}'.format(n2,n1,n2))

'''
#
'''
n=eval(input('enter any number:'))
if n%2==0:
    print('{} is even number'.format(n))
else:
    print('{} is odd number'.format(n))

 '''
#
'''
p=eval(input('enter your percentage:'))
if p>=0 and p<35:
    print('you are failed')
elif p>=35 and p<50:
    print('3 rd class')
elif p>=50 and p<60:
    print('2 nd class')
elif p>=60 and p<75:
    print('1 st class')
elif p>=75 and p<=100:
    print('distinct')
else:
    print('invalid percentage')
   '''
#
'''
n1=eval(input('enter first number:'))
n2=eval(input('enter second number:'))
if n1>n2:
    print('{} is highest number between {} and {}'.format(n1,n1,n2))
elif n1==n2:
    print('{} and {} are same numbers'.format(n1,n2))
else:
    print('{} is highest number between {} and {}'.format(n2,n1,n2))
'''
#
'''
course=input('which course you are learning?:')
if course=='python':
    print('python is simple and easy language')
elif course=='java':
    print('java is little complex and lengthy language')
elif course=='c':
    print('c isd the oldest language')
else:
    print('python or java is best for freshers')
   '''     
#
'''
p=eval(input('enter any number:'))
if p>0 and p%2==0:
    print('{] is poistive and even number'.format(p))
elif p>0 and p%2!=0:
    print('{] is poistive and odd number'.format(p))
elif p<0 and p%2==0:
    print('{] is negative and even number'.format(p))
elif p<0 and p%2!=0:
    print('{] is negative and odd number'.format(p))
else:
    print('you entered zero')
'''

#
'''
ans1=input('did you write assignments ?(yes/no):').lower()
if ans1=='yes':
    marks=eval(input('how many marks you got?:'))
    if marks>=0 and marks<25:
        print('ok,you need to pratice more')
    elif marks>=25 and marks<45:
        print('good,you need to pratice little more')
    elif marks>=45 and marks<=50:
        print('very good,maintain same')
    else:
        print('{} is invalid marks'.format(marks))
elif ans1=='no':
    print('you should write assignments')
else:
    print('dont say stories ,please say yes or no')
'''
#
'''
ans1=input('what are you doing ?:')
if ans1=='training':
    ans2=input('which course are you training?:')
    if ans2 in['python','java','c','c++']:
       print('{},very good skill'.format(ans2))
    elif ans2 in['aws','sap','deveops']:
       print('{},is not good for freshers'.format(ans2))
    else:
       print('{],is new/old skill  for courses')
elif ans1=='searching':
    ans3=input('where are you searching?:')
    if ans3 in['hyd','bnglr','chennai','pune']:
       print('{},is the best location for job searching'.format(ans3))
    else:
       print('{},is not good location for job searching'.format(ans3))
elif ans1=='working':
    package=eval(input('what is your package?:'))
    if package >1 and package <=2:
      print('{},its very less package')
    elif package>=2 and package<=5:
      print('{},good package')
    elif package>=5 and package<=7:
      print('{},very good package')
    else:
      print('dont tell lies')
else:
      print('dont waste your time')
'''
   #

employees = {
    'emp1':{'name':'Sai', 'salary':20000, 'company':['TCS','Capgemini','Infosys'], 'hTown':'Hyd'},
    'emp2':{'name':'Nani','salary':30000, 'company':['Wipro','NTH'], 'hTown':'Bangalore'},
    'emp3':{'name':'Satya','salary':40000, 'company':['NTH','Infosys','CTS'],'hTown':'Chennai'},
    'emp4':{'name':'Rohit','salary':25000, 'company':['Infosys','TCS','Defteam'], 'hTown':'Pune'},
    'emp5':{'name':'Mohan','salary':22000, 'company':['NTH','HCL','DeepCompute'], 'hTown':'Hyd'},
    'emp6':{'name':'Sanjay','salary':45000, 'company':['Wipro','Infosys','Defteam'], 'hTown':'Mumbai'}
    }
'''for i in employees:
        if employees[i]['name']=='Satya':
                print(employees[i]['company'])'''
#print(employees['emp1']['salary'])     
'''for i in employees:
   print(employees[i]['name'])'''
'''s=0
for i in employees:
   s=s+employees[i]['salary']
print(s)'''
#print(employees['emp2']['hTown'])
'''for i in employees:
   if employees[i]['name'].endswith(('a','e','i','o','u')):
      print(employees[i]['name'])'''
#print(employees['emp4']['hTown'])    
#print(employees['emp3']['company'])
#print(employees['name'])
#print(employees['emp2']['name']['salary'])
#print(employees['emp4']['salary'])
'''for i in employees:
   if 'Infosys'  not in employees[i]['company']:
        print(employees[i]['name'])'''
#print(employees['emp5']['name']['company'])
'''for i in employees:
   if 'Pune' in employees[i]['hTown']:
       print(employees[i]['name'])'''
'''
for i in employees:
   if 'TCS' in employees[i]['company']:
        print(employees[i]['name'])

'''
'''for i in range(5,26,5):
    
     print(i)
'''
#
'''
for i in range(-1,0,1):
    print(i)
'''
#
'''
for i in range(-5,6):
    print(i)
'''
#
'''
for i in range(-10,11,2):
    print(i)
'''
#
'''
st='python and django are simple skills'
newList=[]
s=st.split(' ')
for i in s:
   if len(i)==6:
       newList.append(i)
print(newList) 
'''
'''team = ['Kohli', 'Dhoni', 'Sachin', 'Surya']
name=input('enter any name:')
if name in team:
	print('{} is avaliable in team'.format(name))
if name not in team:
	team.append(name)
print(team)'''

'''language='python'
course=input('which course  you are learning:')
if course==language:
	print('you are learning updated skill language')
else:
      	print('you have to learn python language')'''

'''n=eval(input('enter any number:'))
if n%10==0:
	print('{} is divisible  by 10'.format(n))
else:
	print('{} is not divisible by 10'.format(n))'''
'''n=eval(input('enter any number:'))
print(type(n))'''
'''st='developer'
s=input('enter any character:')
if s in st:
	print('{} is available in string'.format(s))
else:
	print('{} is  not available in string'.format(s))'''
'''n=['monday','tuesday','wednesday','thursday']
day=input('enter your day:')
if day in n:
	print('you can wear School Uniform')
elif day=='Friday':
	print('You can wear Civil Dress')
elif day=='Saturday':
	print('You can wear white and white')
elif day=='Sunday':
	print('Its your choice')
'''
'''name=input('enter your name:')
gender=input('enter your gender:')
if gender=='male':
	age=eval(input('enter your age:'))
	if age>=30:
	       print('its time to get marraige')
elif gender=='female':
	age=eval(input('enter your age:'))
	if age>=25:
	       print('its time to get marriage')
else:	
	print('please enter your gender')'''

'''name=input('enter your name:')
age=eval(input('enter your age:'))
if age>=0 and age<=5:
	print('you are an infant')
elif age>=6 and age<=16:
	print('you are school going kid')
elif age>=17 and age<=22:
	print('you are college going kid')
elif age>=23 and age<=30:
	print('You need to settle in life and get marry')
elif age>=31 and age<=45:
	print('You need to work and earn money')
elif age>=46 and age<=60:
	print('You need to do business')
elif age>=61:
	print('You need to take rest')
else:
	print('Invalid Age, please check once')'''

'''height=eval(input('enter the height:'))
weight=eval(input('enter the weight:'))
BMI=weight / height*height
if BMI>0 and BMI<=18.5:
	print('Underweight')
elif BMI>18.5 and BMI<=24.9:
	print('Normal Weight')
elif BMI>25.0 and BMI<=29.9:
	print('pre-obesity')
elif BMI>30.0 and BMI<=40.0:
	print('obesity')
elif BMI>40:
	print('extremly obesity')
else:
   print('unfit')'''
'''n=eval(input('enter any number:'))
if n>=1 and n<=10:
	if n%2==0:
		print('You have entered even number')
	else:
		print('You have entered odd number')
else:
	print('Please enter any number between 1 and 10')
'''
'''i=1
n=eval(input('enter any number:'))

while i<=10:
        m=n*i
        print('{}*{}={}'.format(n,i,m))
        i=i+1
'''
'''1.for i in range(10,50):
        if i%5==0:
          print(i)'''
'''for i in range(100,10,-1):
        
        if i%10==0:
            print(i)
for i in range(11,25,2):
        print(i)'''
'''for i in range(-2,-22,-2):
        print(i)'''
'''for i in range(-3,5):
        print(i)''' 
'''for i in  range(-21,22,7):
        
         print(i)'''
'''for i in range(15,-16,-3):
        if i %2==0:
                continue
        print(i)'''

players = { 
'player1':{'name':'Sachin', 'matches':{'test':200,'odi':463},'scores':{'test':248,'odi':200}, 
'wickets':{'test':46, 'odi':154}, 'age':49, 'shirt':10, 'role':'top-order','location':'Bombay'}, 
'player2':{'name':'Kohli', 'matches':{'test':102, 'odi':262}, 'scores':{'test':254, 'odi':183}, 
'wickets':{'test':0, 'odi':4}, 'age':33, 'shirt':18, 'role':'top-order','location':'Delhi'}, 
'player3':{'name':'Rohit', 'matches':{'test':44, 'odi':231}, 'scores':{'test':212, 'odi':264}, 
'wickets':{'test':2, 'odi':8}, 'age':35, 'shirt':45, 'role':'opening','location':'Nagpur'}, 
'player4':{'name':'Sehwag','matches':{'test':104,'odi':251}, 'scores':{'test':319, 'odi':219}, 
'wickets':{'test':40, 'odi':96}, 'age':43, 'shirt':44, 'role':'opening', 'location':'Delhi'}, 
'player5':{'name':'Zaheer Khan', 'matches':{'test':92, 'odi':200}, 'scores':{'test':75, 'odi':34}, 
'wickets':{'test':311, 'odi':282}, 'age':43, 'shirt':41, 'role':'Bowler','location':'Bombay'} ,
'player6':{'name':'Dhoni', 'matches':{'test':90, 'odi':350}, 'scores':{'test':224, 'odi':183}, 
'wickets':{'test':0, 'odi':1}, 'age':41,'shirt':7, 'role':'keeper','location':'Ranchi'} }
 
#print(players)

'''1.for i in players:
         print(players[i]['name'])'''

'''2.for i in players:
         print(players[i]['age'])'''
'''3.lst=[]
for i in players:
         n=players[i]['age']
         lst.append(n)
for i in players:
        if min(lst)==players[i]['age']:
                print(players[i]['name'])'''
'''4.lst=[]
for i in players:
        n=players[i]['matches']['test']
        lst.append(n)
print(lst)
for i in players:
        if max(lst)==players[i]['matches']['test']:
                print(players[i]['name'])'''
        

'''5.for i in players:
        if  players[i]['wickets']['test']==0:
                print(players[i]['name'],players[i]['matches']['test'])'''

'''6.lst=[]
for i in players:
        
         n=players[i]['wickets']['odi']
         lst.append(n)
for i in players:
        if max(lst)==players[i]['wickets']['odi']:
                print(players[i]['name'])'''

        
'''7.lst=[]
for i in players:
        
         n=players[i]['matches']['odi']
         lst.append(n)
for i in players:
        if max(lst)==players[i]['matches']['odi']:
                print(players[i]['name'])'''
'''8.lst=[]
for i in players:
        
         n=players[i]['scores']['test']+players[i]['scores']['odi']
         lst.append(n)
for i in players:
        if str(max(lst))==str(players[i]['scores']['test']+players[i]['scores']['odi']):     
                print(players[i]['name'])'''


'''9.s=0
for i in players:
        if players[i]['name']=='Kohli':
                s=s+players[i]['matches']['test']
        if players[i]['name']=='Kohli':
                s=s+players[i]['matches']['odi']       
                print(s)'''
'''10.for i in players:
        if players[i]['name']=='Rohit':
                print(players[i]['age'])'''
'''11.s=0
for i in players:
        s=s+players[i]['scores']['odi']
print(s)
''12.s=0
for  i in players:
        if players[i]['name']=='Zaheer Khan':
                s=s+players[i]['wickets']['test']
        if players[i]['name']=='Zaheer Khan':
                s=s+players[i]['wickets']['odi']       
                print(s)'''
'''13.for i in players:
        if players[i]['role']=='opening':
                print(players[i]['name'])'''


'''14.lst=[]
for i in players:
                        
         n=players[i]['shirt']
         lst.append(n)
for i in players:
        if max(lst)==players[i]['shirt']:
                print(players[i]['name'])'''


'''15.for i in players:
        if players[i]['location']=='Bombay':
                print(players[i]['name'])'''

'''16.for i in players:
        if players[i]['name']=='Sachin':
        print(players[i]['shirt'])
''17.for i in players:
        if players[i]['name']=='Rohit':
                print(players[i]['role'])'''
'''18.for i in players:
        if players[i]['shirt']==45:
                print(players[i]['location'])''' 

'''19.for i in players:
        if players[i]['role']=='Bowler':
                print(players[i]['wickets'])'''
'''20.c=0
for i in players:
        
        if players[i]['role']=='opening':
              c+=1
              
print(c)'''
'''21.for i in players:
        if players[i]['location']=='Bombay' and players[i]['role']=='opening':
             print(players[i]['name'])
        else:
             print('no  one is there')'''
'''22.for i in players:
        if players[i]['location']=='Delhi':
                print(players[i]['role'])'''
'''23.for i in players:
        if players[i]['name']=='Rohit':
                print(players[i]['role'])
        if players[i]['name']=='Rohit':
                print(players[i]['location'])'''
'''24.s=0
for i in players:
         if players[i]['location']=='Bombay':
                 if players[i]['role']=='top-order':
                         s=s+players[i]['scores']['odi']
                         s=s+players[i]['scores']['test']
                         
print(s)'''
'''25.st=set()
for i in players:
    j=players[i]['role']
    if j in players[i]['role']:
        st.add(j)
print(st)'''
'''26.for i in players:
        if players[i]['location']=='Delhi':
                if players[i]['role']=='top-order':
                        print(players[i]['shirt'])'''
'''27.for i in players:
        if players[i]['role']=='keeper':
                print(players[i]['name'])'''
'''28.for i in players:
        if players[i]['name']=='Dhoni':
                print(players[i]['shirt'])'''
'''29.for i in players:
        if players[i]['matches']['test']<100:
                print(players[i]['name'])'''
'''30.s=0
for i in players:
        if players[i]['location']=='Ranchi':
                s=s+players[i]['wickets']['test']
                s=s+players[i]['wickets']['odi']
print(s)'''
                


#1
'''lst=[10, 11,13,14,9,8]
newList=[]
for i in lst:
    if i%2==0:
        newList.append(i)
print(newList)'''

#2
'''lst=[10,'a',True,'b',False]
newList=[]
for i in lst:
    if type(i) is str:
        newList.append(i)
print(newList)'''

#3
'''lst=[12,15,27,20,5]
newList=[]
for i in lst:
    if i%5==0:
        newList.append(i)
print(newList)'''
#4
'''lst=[10,'a',20,True,30,'b',40]
c=0
for i in lst:
    if type(i) is int:
        c=c+1
    
print(c)'''

#5
'''st='python language'
c=0
for i in st:
    if type(i) is str:
        c=c+1
    
print(c)'''
#6
'''st='python narayana tech house hyd'

st=st.split(' ')
print(len(st))'''
#7
'''st='python language'
newList=[]
for i in st:
    if i  in 'aeiouAEIOU':
        newList.append(i)
print(newList)'''
#8
'''st='python narayana'
c=0
for i in st:
    if i in 'aeiouAEIOU':
        c=c+1

print(c)'''
#9
'''st='python is a simple language'
c=0
st=st.split()
for i in st:
    for j in i:
        
     c=c+1
print(c)'''
#10
'''st='python language'

c=0
st=st.split()
for i in st:
    for j in i:
        if j not in 'aeiouAEIOU':
            c=c+1
print(c)'''
        
#11
'''st='python is simple and easy language'
newList=[]
for i in st.split():
     if i[0] in 'aeiouAeIOU':
         newList.append(i)
print(newList)'''

#12
'''st='python is simple and easy language'
newList=[]
for i in st.split():
    if i[-1] not in 'aeiouAEIOU':
        newList.append(i)
print(newList)'''
#13
'''st='python is simple and easy language'

newList=[]
for i in st.split():
    if 'a' in i:
        if i.count('a')==2:
            newList.append(i)
print(newList)'''

#14
'''st='python is simple and easy language'

newList=[]
for i in st.split():
    newList.append(len(i))        
print(newList)'''

#15
'''st='python is simple and easy language'
newList=[]
for i in st.split():
    
    newList.append(i[0]+i[-1])        
print(newList)'''

#16
'''st='python is simple and easy language'

newList=[]
for i in st.split():
    if 'a' in i:
            newList.append(i)
print(newList)'''

#17
'''st='python is simple and easy language'

newList=[]
for i in st.split():
    if 'e'  not in i:
        newLis t.append(i)
print(newList)'''

#18
'''st='python is simple and easy language'

newList=[]
for i in st.split():
    if len(i)<=4:
        newList.append(i)
print(newList)'''

#19
'''st='python is simple and easy language'

newList=[]
for i in st.split():
    if len(i)%2!=0:
        newList.append(i)        
print(newList)''' 

#20
'''st='python is number one language'
newList=[]
for i in st.split():
     if i[0] in 'aeiouAeIOU' and i[-1] in 'aeiou':
         newList.append(i)
print(newList)'''

#21
'''names=['madam','python','dad','language','eye','malayalam']
newList=[]
for i in names:
    if i[-1::-1] in names:
        newList.append(i)
print(newList)'''

#22
'''names=['madam','python','dad','language','eye','malayalam']
newList=[]
for i in names:
    if i[-1::-1]  not in names:
        newList.append(i)
print(newList)  '''

#23
'''names=['madam','python','dad','language','eye','malayalam']
newList=[]
for i in names:
    if i[-1::-1]  in names and i.startswith('m'):
        newList.append(i)
print(newList)'''

#24
'''names=['madam','python','dad','language','eye','malayalam']
newList=[]
for i in names:
    if i[-1::-1]  in names and len(i)>3:
      newList.append(i)
print(newList)'''
 
#25
'''names=['madam','python','dad','language','eye','malayalam']
lst=[]
lst1=[]
lst2=[]
for i in names:
    if i[-1::-1]==i:
        lst.append(i)
        lst1.append(len(i))
for i in lst:
    if len(i)==max(lst1):
        lst2.append(i)
print(lst2)'''

#1
'''lst=[10,11,13,14,9,8]
print([i for i in lst if i%2==0])'''

#2
'''lst=[10,'a',True,'b',False]
print([i for i in lst if type(i) is str])'''

#3
'''lst=[12,15,27,20,5]
print([i for i in lst if i%5==0])'''

#4
'''lst=[10,'a',20,True,30,'b',40]
print( len([i for i in lst if type(i)==int]))'''
#5
'''st='python language'
print(len(st))'''
#6
'''st='python narayana tech house hyd'
st= st.split()
print(len(st))'''
#7
'''st='python language'
print([i for i in st if i in 'aeiou'])'''
#8
'''st='python language'
print(len([i for i in st if i in 'aeiou']))'''
#9
'''st='python is a simple  language'
print(len([j for i in st.split() for j in i]))'''
#10
'''st='python language'
print(len([j for i in st.split() for j in i if  j not in 'aeiou']))'''

#11
'''st='python is simple and easy language'
print([i for i in st.split() if i[0] in 'aeiou'])'''
#12
'''st='python is simple and easy language'
print([i for i in st.split() if i[-1] not in 'aeiou'])'''
#13
'''st='python is simple and easy language'
print([i for i in st.split() if 'a'in i if i.count('a')==2])'''

#14
'''st='python is simple and easy language'
print([len(i) for i in st.split()]) '''

#15
'''st='python is simple and easy language'
print([i[0]+i[-1] for i in st.split()])'''

#16
'''st='python is simple and easy language'
print([i for i in st.split() if 'a' in i])'''

#17
'''st='python is simple and easy language'
print([i for i in st.split() if 'e' not in i])'''

#18
'''st='python is simple and easy language'
print([i for i in st.split() if len(i)<=4])'''

#19
'''st='python is simple and easy language'
print([i for i in st.split() if len(i)%2!=0])'''

#20
'''st='python is number one language'
print([i for i in st.split() if i[0] in 'aeiouAeIOU' and i[-1] in 'aeiou'])'''

#21
'''names=['madam','python','dad','language','eye','malayalam']
print([i for i in names if i[-1::-1] in names])'''

#22
'''names=['madam','python','dad','language','eye','malayalam']
print([i for i in names if i[-1::-1] not  in names])'''

#23
  '''names=['madam','python','dad','language','eye','malayalam']
print([i for i in names if i[-1::-1] in names and i.startswith('m')])'''

#24
'''names=['madam','python','dad','language','eye','malayalam']
print([i for i in names if i[-1::-1] in names and len(i)>3])'''

#25
'''names=['madam','python','dad','language','eye','malayalam']
print([max(names,key=len)])'''

