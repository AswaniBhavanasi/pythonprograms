'''def display(i):
    if i <= 100:
        print(i)
        i=i+1
        display(i)

i=1
display(i)
'''
'''
for i in range(1,20):
    count = 0
    for j in range(2,(i//2+1)):
        if (i%j == 0):
            count = count+1
            break
    if (count == 0 and i != 1):
        print(i)
  '''

'''import calendar as c
m = int(input('Month Number: '))

if m >= 1 and m <= 12:
    print(c.month_name[m])
else:
    print('Invlid Month Number ')
'''
'''import re
mobile = input('Mobile Number: ')

m = re.fullmatch('[6-9][0-9]{9}',mobile)

if m != None:
    print('Valid Mobile Number')
'''
''''
data = open('matches.txt').read().split(' ')
d = {}.fromkeys(data,0)

for i in data:
    if i in d:
        d[i] = d[i]+1

print(d)
'''
# Write a program to print fibonacci series upto n terms in python
'''n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2,14):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()'''
# write a program to reverse of a number
'''num = 1234
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print(reverse)

or
num = 1234
print(str(num)[::-1])'''

# write a program to check palindrome or not
'''num = 1231
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")

or
num = 1234
reverse = int(str(num)[::-1])

if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")'''

# write a program to check armstrong number
number = 371
num = number
digit, sum = 0, 0
length = len(str(num))
for i in range(length):
  digit = int(num%10)
  num = num/10
  sum += pow(digit,length)
if sum==number:
  print("Armstrong")
else:
  print("Not Armstrong")

#write a program factorial number
num=eval(input('enter a number:'))
n=1
for i in range(1,num+1):
  n=n*i
print ('factorial of', num, '=',n)

# write a program to check prime or not
num=5
n = 0
for i in range(2,num):
  if num%i==0:
    n = 1
    break
if n == 1:
  print('Not Prime')
else:
  print("Prime")















