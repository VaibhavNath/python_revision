'''for i in range(1,11):
    for j in range(1,i):
        print(j,end="")
    print()'''

##1
##12
##123
##1234
##12345
##123456
##1234567
##12345678
##123456789


'''for i in range(1,11):
    for j in range(1,i+1):
        print(j,end="")
    print()'''

##1
##12
##123
##1234
##12345
##123456
##1234567
##12345678
##123456789
##12345678910


#using placeholder with format
'''for i in range(1,11):
    for j in range(1,i+1):
        print('{:3}'.format(j),end="")
    print()'''

##  1
##  1  2
##  1  2  3
##  1  2  3  4
##  1  2  3  4  5
##  1  2  3  4  5  6
##  1  2  3  4  5  6  7
##  1  2  3  4  5  6  7  8
##  1  2  3  4  5  6  7  8  9
##  1  2  3  4  5  6  7  8  9 10


'''def hello():
    name=input("enter name: ")
    print("Hello {} nice to meet you".format(name))
    
hello()'''

#assignment operators
##>>> i=0
##>>> i=i+1
##>>> i
##1
##>>> i=i+8
##>>> i
##9
##>>> i=i/3
##>>> i
##3.0
##>>> i=i//3
##>>> i
##1.0
##>>> i+=1
##>>> i
##2.0
##>>> i*=2
##>>> i
##4.0
##>>> i/=4
##>>> i
##1.0

#typecasting str to int
'''n=input("enter a number:")
print(n)
print(type(n))
print(type(int(n)))
print(n+1) #can only concatenate str (not "int") to str
print(int(n)+1)'''

#while loop
'''count=int(input("Enter a number: "))
while count>0:
    count -=1
    print(count)'''
    
##Enter a number: 5
##4
##3
##2
##1
##0

'''count=int(input("Enter a number: "))
while count>0:
    print(count)
    count -=1'''

##Enter a number: 5
##5
##4
##3
##2
##1

'''count=int(input("Enter a number: "))
while count>=0:
    print(count)
    count -=1'''

##Enter a number: 5
##5
##4
##3
##2
##1
##0

#list methods
'''num=[1,2,4,0,-5]
pos=[]
neg=[]
for n in num:
    if n>0:
        pos.append(n)  #append=add number to end of list
    else:
        neg.append(n)'''


#list comprehension
'''num=[1,2,4,0,-5,8,10]
pos=[i for i in num if i>0]'''

##>>> pos
##[1, 2, 4, 8, 10]


'''list_numbers=[]
for i in range(3):
    list_numbers.append(list(range(1,6)))'''


##[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

'''for i in list_numbers:
	print(i)'''

##[1, 2, 3, 4, 5]
##[1, 2, 3, 4, 5]
##[1, 2, 3, 4, 5]


'''import random
for i in range(10):
	print(random.randint(1,5))'''


##1
##4
##3
##4
##1
##3
##2
##5
##2
##3


'''import random
number=[random.randint(1,5) for i in range(10)]'''

##>>> number
##[3, 1, 3, 5, 3, 4, 5, 2, 2, 2]


import random
##numbers = [i for i in range(1,26)]

##>>> numbers
##[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
## 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

##random.shuffle(numbers)

##>>> numbers
##[8, 11, 23, 13, 24, 20, 6, 14, 19, 1, 17, 5, 18,
## 22, 7, 10, 2, 21, 9, 15, 16, 4, 12, 25, 3]

shuffled=[8, 11, 23, 13, 24, 20, 6, 14, 19, 1, 17, 5, 18,
          22, 7, 10, 2, 21, 9, 15, 16, 4, 12, 25, 3]

##>>> numbers.pop(5)  #pop and remove item from list
##20

horses=[[],[],[],[],[]]
'''for i in range(5):
    for j in range(5):
        horses[j].append(shuffled.pop())'''

##>>> horses
##[[3, 15, 7, 1, 24], [25, 9, 22, 19, 13], [12, 21, 18, 14, 23], [4, 2, 5, 6, 11], [16, 10, 17, 20, 8]]
##>>> shuffled
##[]

'''for race in horses:
    print(race)'''

##[3, 15, 7, 1, 24]
##[25, 9, 22, 19, 13]
##[12, 21, 18, 14, 23]
##[4, 2, 5, 6, 11]
##[16, 10, 17, 20, 8]

horses=[[3, 15, 7, 1, 24],
        [25, 9, 22, 19, 13],
        [12, 21, 18, 14, 23],
        [4, 2, 5, 6, 11],
        [16, 10, 17, 20, 8]]

for race in horses:
    race.sort()

##>>> horses
##[[1, 3, 7, 15, 24], [9, 13, 19, 22, 25],
## [12, 14, 18, 21, 23], [2, 4, 5, 6, 11], [8, 10, 16, 17, 20]]

'''for race in horses:
    (race.sort(reverse=True))'''  #sort each list in descending order.

##[24, 15, 7, 3, 1]
##[25, 22, 19, 13, 9]
##[23, 21, 18, 14, 12]
##[11, 6, 5, 4, 2]
##[20, 17, 16, 10, 8]

for race in horses:
    print(race)

def last(x):
    return x[-1]


new_horses=sorted(horses,key=last,reverse=True)
print()
for race in new_horses:
    print(race)

##[9, 13, 19, 22, 25]
##[1, 3, 7, 15, 24]
##[12, 14, 18, 21, 23]
##[8, 10, 16, 17, 20]
##[2, 4, 5, 6, 11]  