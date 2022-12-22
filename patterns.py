#1
'''n=eval(input('enter any number:'))
for i in range(n):
    for j in range(i+1):
        print(n-i,end=' ')
    print(end='\n')
output:
------  
enter any number:4
4 
3 3 
2 2 2 
1 1 1 1''' 
#2
'''n=eval(input('enter any number:'))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print(end='\n')
output:
------
enter any number:4
* 
* * 
* * * 
* * * * '''
#3
'''n=eval(input('enter any number:'))
for i in range(n):
    for j in range(i+1):
        print(n-j,end=' ')
    print(end='\n')
output
------
enter any number:5
5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 '''
#4
'''n=eval(input('enter any number:'))
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print(end='\n')
output
------
enter any number:5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * '''
#5
'''n = int(input("Enter any number : "))

for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print(end="\n")
output
------
Enter any number : 5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 '''
#6
'''n = int(input("Enter any  number : "))
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print(end="\n")
output
-------
Enter any  number : 5
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 '''
#7
'''n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n-i):
        print(i, end=" ")
    print(end="\n")
output
------
Enter number of rows: 6
0 0 0 0 0 0 
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 '''
#8
'''n= int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n-i):
        print(i+1, end=" ")
    print(end="\n")
output
------
Enter number of rows: 5
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 '''


#9

'''n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n-i):
        print(i-j, end=" ")
    print(end="\n")
output
-----
Enter number of rows: 6
0 -1 -2 -3 -4 -5 
1 0 -1 -2 -3 
2 1 0 -1 
3 2 1 
4 3 
5 '''
#10
'''n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n-i):
        print(j-i, end=" ")
    print(end="\n")
output
-----
Enter number of rows: 5
0 1 2 3 4 
-1 0 1 2 
-2 -1 0 
-3 -2 
-4 '''
#11
'''n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(i+1):
        print(i*2+1 ,end=" ")
    print(end="\n")
output
-----
Enter number of rows: 4
1 
3 3 
5 5 5 
7 7 7 7'''
#12
'''n = int(input("Enter number of rows: "))
for i in range(n):
    
    for j in range(n-i):
        print(n-i, end=" ")
    print(end="\n")
output
-----
Enter number of rows: 4
4 4 4 4 
3 3 3 
2 2 
1 '''
#13
'''n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(i+1):
        print(i-j+1, end=" ")
    print(end="\n")
output
-----
Enter number of rows: 5
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 '''
#14
'''n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n-i):
        print(n-i-j, end=" ")
    print(end="\n")
output
-----
Enter number of rows: 6
6 5 4 3 2 1 
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 '''
#15
'''n = int(input("Enter number of rows: "))
count=1
for i in range(n):
    for j in range(i+1):
        print(count, end=" ")
        count=count+1
    print(end="\n")
output
-----
Enter number of rows: 5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 '''
#16
'''n = int(input("Enter number of rows: "))
num =n
for i in range(n,0,-1):
    for j in range(0, i):
        print(num, end=' ')
    print(end="\n")
output
------
Enter number of rows: 5
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5 '''
#17
'''n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print(end="\n")
output
------
Enter number of rows: 5
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1 '''
#18
'''n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()    
output
------
Enter number of rows: 6
1 2 3 4 5 6 
2 2 3 4 5 6 
3 3 3 4 5 6 
4 4 4 4 5 6 
5 5 5 5 5 6 
6 6 6 6 6 6 '''
#19
'''n = int(input("Enter the number of rows "))
for i in range(1, n+ 1):
    for j in range(1, i + 1):
        square = i * j
        print(i * j, end='  ')
    print()
output
------
Enter the number of rows 8
1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64  
'''
#20
'''n = int(input("Enter the number of rows "))

for i in range(1, n):
    num = 1
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print(end="\n")
output
-------
Enter the number of rows 6
          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 '''
