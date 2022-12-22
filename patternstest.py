#1
'''n=int(input('enter any number:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print(end='\n')
output
------
enter any number:5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 '''
#2
'''n=int(input('enter any number:'))
for i in range(n):
    for j in range(i):
        print(i,end=" ")
    print(end='\n')
output
------
enter any number:6

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5'''
#3
'''n=int(input('enter any number:'))
for i in range(1,n):
    for j in range(n):
        print(i,end=" ")
    print(end='\n')
    
output
------
enter any number:5
1 1 1 1 1  
2 2 2 2 2  
3 3 3 3 3  
4 4 4 4 4  
5 5 5 5 5  '''
#4
'''n=int(input('enter any number:'))
for i in range(n,0,-1):
    for j in range(n):
        print(i,end=" ")
    print(end='\n')
output
------
enter any number:5
5 5 5 5 5 
4 4 4 4 4 
3 3 3 3 3 
2 2 2 2 2 
1 1 1 1 1 '''
#5
'''n=int(input('enter any number:'))
for i in range(1,n):
    for j in range(n-i):
        print(i,end=" ")
    print(end='\n')
output
------
enter any number:6
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 '''
#6
'''n=int(input('enter any number:'))
for i in range(n):
    for j in range(n-i):
        print(n-i,end=" ")
    print(end='\n')
output
------
enter any number:5
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 '''
#7
'''n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n):
        print(i*2+1 ,end=" ")
    print(end="\n")
output
------
Enter number of rows: 5
1 1 1 1 1 
3 3 3 3 3 
5 5 5 5 5 
7 7 7 7 7 
9 9 9 9 9 '''
#8
'''n = int(input("Enter number of rows: "))
count=1
for i in range(n):
    for j in range(i+1):
        print(count, end=" ")
        count=count+1
    print(end="\n")
output
------
Enter number of rows: 5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 '''
#9
'''n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(i):
        print('*', end=" ")

    print(end='\n')
output
------
Enter number of rows: 6

* 
* * 
* * * 
* * * * 
* * * * * '''
#10
'''n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n):
        print('*', end=" ")
    print(end='\n')
output
------
Enter number of rows: 5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * '''
