#1. Write a program to fetch all data from the file.
'''print(open('nthdata.txt').read())
output:
TCS,Sai,Rohit,Satya,Dhoni,Sarath,Saroj,Venkat,Sas
INFOSYS,Kohli,Santosh,Venkat,Koti,Prabha,Soumya,Mishra
WIPRO,Satya,Kohli,Ram,Chinna,Pop,Amelia,Suresh,Arjuna
CTS,Prabha,Subha,Debha,Rabha,Venkat,Dhoni,Surya,Saroj
NTH,Narayana,Akhil,Arha,Venkat,Sravya,Ananya,Revanth,Aha
ABC,Arha,Chinna,Satya,Dhoni,Venkat,Rohit,Yash,Nikhilesh'''
  
#2. Write a program to read the first line from the file.
'''print(open('nthdata.txt').readline())
output:
TCS,Sai,Rohit,Satya,Dhoni,Sarath,Saroj,Venkat,Sas '''   
#3. Write a program to read the last line from the file.
'''print(open('nthdata.txt').readlines()[-1])
output:
ABC,Arha,Chinna,Satya,Dhoni,Venkat,Rohit,Yash,Nikhilesh'''
#4. Write a program to read the 3rd line from file
'''print(open('nthdata.txt').readlines()[2])

WIPRO,Satya,Kohli,Ram,Chinna,Pop,Amelia,Suresh,Arjuna'''
#5. Write a program to count total number of characters in the file?
'''print(len(open('nthdata.txt').read()))

325'''
#6. Write a program to count total number of commas in the file?
'''print(open('nthdata.txt').read().count(','))

47'''
#7. Write a program to count total number of words in the first line?
'''print(len(open('nthdata.txt').readlines()[0].split(',')))

9'''
#8. Write a program to count total number of lines in the file?
'''print(len(open('nthdata.txt').readlines()))

6'''
#9. Write a program to count total number of 'Sai' name in the file?
'''print(open('nthdata.txt').read().count('Sai'))

1'''
#10. Write a program to fetch the first word from each line in the file?
'''print([i.split(',')[0] for i in(open('nthdata.txt').readlines())])

['TCS', 'INFOSYS', 'WIPRO', 'CTS', 'NTH', 'ABC']'''
#11. Write a program to fetch the last word from each line?
'''print([i.split(',')[-1] for i in(open('nthdata.txt').readlines())])

['Sas\n', 'Mishra\n', 'Arjuna\n', 'Saroj\n', 'Aha\n', 'Nikhiles\n']'''

#12. Write a program to fetch all words which starts with 'a' Character?
'''a=open('nthdata.txt').read()
b=a.replace('\n',',').split(',')
print(b)
for i in b:
        if i[0] in 'Aa':
            print(i)

print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i[0] in 'Aa'])
Amelia
Arjuna
Akhil
Arha
Ananya
Aha
ABC
Arha'''           
#13. Write a program to fetch all words which ends with an vowel?
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i[-1] in 'aeiouAEIOU'])

['Sai', 'Satya', 'Dhoni', 'Kohli', 'Koti', 'Prabha', 'Soumya',
 'Mishra', 'WIPRO', 'Satya', 'Kohli', 'Chinna', 'Amelia', 'Arjuna',
 'Prabha', 'Subha', 'Debha', 'Rabha', 'Dhoni', 'Surya', 'Narayana',
 'Arha', 'Sravya', 'Ananya', 'Aha', 'Arha', 'Chinna', 'Satya', 'Dhoni']'''
#14. Write a program to fetch all words which has either 'a' or 'i' characters in the file?
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if 'a' in i or 'i' in i])

['Sai', 'Rohit', 'Satya', 'Dhoni', 'Sarath', 'Saroj', 'Venkat',
 'Sas', 'Kohli', 'Santosh', 'Venkat', 'Koti', 'Prabha', 'Soumya',
 'Mishra', 'Satya', 'Kohli', 'Ram', 'Chinna', 'Amelia', 'Arjuna',
 'Prabha', 'Subha', 'Debha', 'Rabha', 'Venkat', 'Dhoni', 'Surya',
 'Saroj', 'Narayana', 'Akhil', 'Arha', 'Venkat', 'Sravya', 'Ananya',
 'Revanth', 'Aha', 'Arha', 'Chinna', 'Satya', 'Dhoni', 'Venkat',
 'Rohit', 'Yash', 'Nikhiles']'''
#15. Write a program to fetch all words which contains only 5 characters in the file?
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if len(i) is 5])

['Rohit', 'Satya', 'Dhoni', 'Saroj', 'Kohli', 'WIPRO', 'Satya',
 'Kohli', 'Subha', 'Debha', 'Rabha', 'Dhoni', 'Surya', 'Saroj',
 'Akhil', 'Satya', 'Dhoni', 'Rohit']'''
#16. Write a program to fetch all words which does not contains vowels except i in the file?
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',')
       if 'i' in i.lower() and 'a' not in i.lower() and 'e' not in i.lower()
       and 'o' not in i.lower() and'u'  not in i.lower()])'''
#17. Write a program to fetch all words which ends with uppercase character in the file?
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i[-1].isupper()])
['TCS', 'INFOSYS', 'WIPRO', 'CTS', 'NTH', 'ABC']'''
#18. Write a program to count total number of characters in the file excluding commas and \ns?
'''print(len([i for i in open('nthdata.txt').read().replace('\n',',').split(',') for j in i]))

273'''
#19. Write a program to count total number of words in the entire file?
'''print(len(open('nthdata.txt').read().replace('\n',',').split(',')))
53'''
#20. Write a program to fetch all even number words from from every line the file?
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if len(i)%2==0])
['Sarath', 'Venkat', 'Venkat', 'Koti', 'Prabha', 'Soumya',
 'Mishra', 'Chinna', 'Amelia', 'Suresh', 'Arjuna', 'Prabha',
 'Venkat', 'Narayana', 'Arha', 'Venkat', 'Sravya', 'Ananya',
 'Arha', 'Chinna', 'Venkat', 'Yash', 'Nikhiles']'''
#21. Write a program to fetch all words which ends with 'bha' in the file?
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',')  if i.endswith( 'bha')])
['Prabha', 'Prabha', 'Subha', 'Debha', 'Rabha']'''
#22. Write a program to display all TCS employees?
'''print([i for i in open('nthdata.txt').readline().replace('\n',',').split(',') if 'TCS' not in i ])

['Sai', 'Rohit', 'Satya', 'Dhoni', 'Sarath', 'Saroj', 'Venkat', 'Sas', '']'''
#23. Write a program to display the company name of Chinna Employee?
'''print([i.split(',')[0] for i in open('nthdata.txt').readlines()if 'Chinna'in i.split(',') ])
['WIPRO', 'ABC']'''

#24. Write a program to fetch the 2nd from 3rd line in the file?
'''print(open('nthdata.txt').readlines()[2].split(',')[1])
Satya'''
#25. Write a program to fetch the first character from each word in the 3rd line?
'''print([i[0] for i in  open('nthdata.txt').readlines()[2].split(',')])
['W', 'S', 'K', 'R', 'C', 'P', 'A', 'S', 'A']'''
#26. Write a program to fetch first and last character of each word in the last line?
'''print([i[0]+i[-1] for i in  open('nthdata.txt').readlines()[-1].split(',')])
['AC', 'Aa', 'Ca', 'Sa', 'Di', 'Vt', 'Rt', 'Yh', 'Ns']'''
#27. Write a program to fetch all characters(except 1st and last chars) of each word in the 2nd line?
'''print([i[1:-1] for i in open('nthdata.txt').readlines()[1].split(',')])
['NFOSY', 'ohl', 'antos', 'enka', 'ot', 'rabh', 'oumy', 'ishra']'''
#28. Write a program to count total number of words which starts with 'S' character?
'''print(len([i for i in open('nthdata.txt').read().replace('\n',',').split(',')  if i.startswith( 'S')]))
14'''
#29. Write a program to fetch all duplicate names in the file?
'''print(set([i for i in open('nthdata.txt').read().replace('\n',',').split(',') for j in i if i .count(j)>1]))
{'Sravya', 'Satya', 'Rabha', 'Chinna', 'INFOSYS', 'Ananya', 'Nikhiles', 'Sarath', 'Prabha', 'Narayana'}'''
#30. Write a program to count all vowels in the file? (Note: output must be in dict)
'''lst=['a','e','i','o','u','A','E','I','O','U']
d={}.fromkeys(lst,0)
for i in open('nthdata.txt').read().replace('\n',',').split(','):
    for j in i:
        if j in d:
            d[j]=d[j]+1
print(d)

{'a': 47, 'e': 10, 'i': 16, 'o': 13, 'u': 5, 'A': 8, 'E': 0, 'I': 2, 'O': 2, 'U': 0}'''
        
#31. Write a program to reverse all words in the file?
'''print([i[-1::-1] for i in open('nthdata.txt').read().replace('\n',',').split(',')])
['SCT', 'iaS', 'tihoR', 'aytaS', 'inohD',
 'htaraS', 'joraS', 'takneV', 'saS', 'SYSOFNI',
 'ilhoK', 'hsotnaS', 'takneV', 'itoK', 'ahbarP',
 'aymuoS', 'arhsiM', 'ORPIW', 'aytaS', 'ilhoK',
 'maR', 'annihC', 'poP', 'ailemA', 'hseruS',
 'anujrA', 'STC', 'ahbarP', 'ahbuS', 'ahbeD',
 'ahbaR', 'takneV', 'inohD', 'ayruS',
 'joraS', 'HTN', 'anayaraN', 'lihkA', 'ahrA',
 'takneV', 'ayvarS', 'aynanA', 'htnaveR', 'ahA',
 'CBA', 'ahrA', 'annihC', 'aytaS', 'inohD', 'takneV',
 'tihoR', 'hsaY', 'selihkiN']'''

#32. Write a program to fetch all words which contains two or more then 'a' characters?
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i.count('a')>=2])
['Satya', 'Sarath', 'Prabha', 'Satya', 'Prabha', 'Rabha', 'Narayana', 'Sravya', 'Ananya', 'Satya']'''

#33. Write a program to fetch all words which starts and ends with 'a' character?
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i[0] in 'Aa' and i[-1] in 'Aa'])
['Amelia', 'Arjuna', 'Arha', 'Ananya', 'Aha', 'Arha']'''
#34. Write a program to fetch word which has more number of 'a' characters?
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',')
       if max([i.lower().count('a') for i in open('nthdata.txt').read().replace('\n',',').split(',')
               if 'a'in i.lower()])==i.lower().count('a')])
['Narayana']

#35. Write a program to fetch all company names which starts with vowel?
print([i.split(',')[0] for i in open('nthdata.txt').readlines() if i.split(',')[0][0] in 'aeiouAEIOU'])
['INFOSYS', 'ABC']'''
#36. Write a program to display company name which contains Saroj Employee?
'''print([i.split(',')[0] for i in open('nthdata.txt').readlines()if 'Saroj' in i.replace('\n',',').split(',') ])

['TCS', 'CTS']'''
#37. Write a program to count all words which starts and ends with consonants?
'''print(len([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i[0] not in 'aeiouAEIOU' and i[-1] not in 'aeiouAEIOU']))
21'''
#38. Write a program to fetch all company names which does not contain Venkat employee?
'''print([i.split(',')[0] for i in open('nthdata.txt').readlines() if 'Venkat' not in i.split(',')])
['WIPRO']'''
#39. Write a program to display company name where Narayana is working?
'''print([i.split(',')[0] for i in open('nthdata.txt').readlines() if 'Narayana' in i.replace('\n',',').split(',')])
['NTH']'''       
#40. Write a program to display the first word and last word from each line in dict format?
'''lst=[]
for i in open('nthdata.txt').read().split('\n'):
    lst.append(i.split(',')[0]+i.split(',')[-1])
d={}.fromkeys(lst)
print(d)

{'TCSSas': None, 'INFOSYSMishra': None, 'WIPROArjuna': None, 'CTSSaroj': None, 'NTHAha': None, 'ABCNikhiles': None}'''
#41. Write a program to fetch all names whose name starts with 'a' in NTH company?
'''print([j for i in open('nthdata.txt').read().split('\n') if 'NTH' in i for j in i.split(',') if j[0] in 'Aa'])
['Akhil', 'Arha', 'Ananya', 'Aha']
'''
#42. Write a program to count total number of employees in CTS company?
'''print([len(i.split(',')[1:]) for i in open('nthdata.txt').readlines() if 'CTS' in i])

[8]'''
#43. Write a program to fetch all companies where Venkat employee is working?
'''print([i.split(',')[0] for i in open('nthdata.txt').readlines() if 'Venkat' in i])
['TCS', 'INFOSYS', 'CTS', 'NTH', 'ABC']
'''
#44. Write a program to fetch all companies names which name starts with Vowel?
'''print([i.split(',')[0] for i in open('nthdata.txt').readlines() if i.split(',')[0][0] in 'aeiouAEIOU'])
['INFOSYS', 'ABC']'''
#45. Write a program to fetch all palindrome names from the file?
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i.lower()==i.lower()[-1::-1]])
['Sas', 'Pop', 'Aha']
'''
#46. Write a program to fetch all companies names where palindrome named employees working?
'''print([i.split(',')[0] for i in open('nthdata.txt').read().split('\n') for j in i.split(',') if j.lower()==j.lower()[-1::-1]])
['TCS', 'WIPRO', 'NTH']'''
#47. Write a program to fetch the lengthiest company name?
'''lst=[]
for i in open('nthdata.txt').read().split('\n'):
    lst.append(len(i.split(',')[0]))
for i in open('nthdata.txt').read().split('\n'):
               if str(max(lst)) in str(len(i.split(',')[0])):
                   print(i.split(',')[0])
INFOSYS'''
#48. Write a program to fetch the lengthiest employee name in ABC company?
'''lst=[]
for i in open('nthdata.txt').read().split('\n'):
    if 'ABC'in i.split(','):
        for j in i.split(',')[1:]:
            lst.append(len(j))
for i in open('nthdata.txt').read().split('\n'):
    if 'ABC'in i.split(','):
        for j in i.split(',')[1:]:
            if str(max(lst)) in str(len(j)):
                print(j)
Nikhiles'''
#49. Write a program to fetch shortest employee name in the WIPRO company?
'''lst=[]
for i in open('nthdata.txt').read().split('\n'):
    if 'WIPRO'in i.split(','):
        for j in i.split(',')[1:]:
            lst.append(len(j))
for i in open('nthdata.txt').read().split('\n'):
    if 'WIPRO'in i.split(','):
        for j in i.split(',')[1:]:
            if str(min(lst)) in str(len(j)):
                print(j)
Ram
Pop'''
#50. Write a program count total number of employees in each company(in dict format)?
lst=[]
for i in open('nthdata.txt').read().split('\n'):
    lst.append(i.split(',')[0])
d={}.fromkeys(lst,0)
for i in open('nthdata.txt').read().split('\n'):
    for j in i.split(','):
        if j in d:
            d[j]=len(i.split(',')[1:])
print(d)

{'TCS': 8, 'INFOSYS': 7, 'WIPRO': 8, 'CTS': 8, 'NTH': 8, 'ABC': 8}
 
