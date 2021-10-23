'''def time_table():
    try:
        x=int(input("Enter a number:"))
        for row in range(x):
            for col in range(x):
                print(f'{row*col:2}', end= "  ")
            print()
    except ValueError:
        print("oppps,enter a number")

time_table()'''

##Enter a number:5
## 0   0   0   0   0  
## 0   1   2   3   4  
## 0   2   4   6   8  
## 0   3   6   9  12  
## 0   4   8  12  16  

##Enter a number:m
##oppps,enter a number


'''def time_table():
    while True:
        try:
            x=int(input("Enter a number:"))
            for row in range(x):
                for col in range(x):
                    print(f'{row*col:2}', end= "  ")
                print()
        except ValueError:
            print("oppps,enter a number")        

time_table()'''

##Enter a number:5
## 0   0   0   0   0  
## 0   1   2   3   4  
## 0   2   4   6   8  
## 0   3   6   9  12  
## 0   4   8  12  16  
##Enter a number:6
## 0   0   0   0   0   0  
## 0   1   2   3   4   5  
## 0   2   4   6   8  10  
## 0   3   6   9  12  15  
## 0   4   8  12  16  20  
## 0   5  10  15  20  25
##Enter a number:m
##oppps,enter a number


'''def time_table():
    while True:
        try:
            x=int(input("Enter a number:"))
            for row in range(x):
                for col in range(x):
                    print(f'{row*col:2}', end= "  ")
                print()
        except ValueError:
            print("oppps,enter a number")
        q=input("do you want another table? y/n: ").lower()
        if q=='n':
            break

time_table()'''

##Enter a number:3
## 0   0   0  
## 0   1   2  
## 0   2   4  
##do you want another table? y/n: y
##Enter a number:
##oppps,enter a number
##do you want another table? y/n: n


#prime numbers
'''def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True'''
'''list1=[i for i in range(1,10)]
for num in list1:
    print(f"{num}is a prime number {is_prime(num)}")'''

##1is a prime number True
##2is a prime number True
##3is a prime number True
##4is a prime number False
##5is a prime number True
##6is a prime number False
##7is a prime number True
##8is a prime number False
##9is a prime number False


'''def nth_prime(x):
    num=3
    prime=2
    if x==1:
        return 2
    while prime < x:
        num+=2
        if is_prime(num):
            prime+=1
    return num'''

##>>> nth_prime(10)
##29
##>>> nth_prime(3)
##5
##>>> nth_prime(4)
##7

'''primes=[i for i in range(2,100) if is_prime(i)]'''

##>>> primes
##[2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
## 31, 37, 41, 43, 47, 53, 59, 61, 67,
## 71, 73, 79, 83, 89, 97]

#GUESS GAME
'''import random

while True:
    number=random.randint(1,20)
    print(number)
    try:
        guess=int(input("enter a guess:"))
        while guess !=number:
            if guess > number:
                print("please guess a smaller number")
                guess=int(input("enter a guess:"))
            else:
                print("please guess a larger number:")
                guess=int(input("enter a guess:"))
        else:
            print("guessed correct number")
    except ValueError:
        print("opps,enter a number")
    q=input("do you want to play again ?y/n: ").lower()
    if q=='n':
        break'''


##9
##enter a guess:5
##please guess a larger number:
##enter a guess:9
##guessed correct number
##do you want to play again ?y/n: y
##14
##enter a guess:10
##please guess a larger number:
##enter a guess:124
##please guess a smaller number
##enter a guess:14
##guessed correct number
##do you want to play again ?y/n: n


#leap year
'''def leap_year(year):
    if year % 4 ==0:
        if year % 100==0:
            if year % 400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

years=[1900,2000,1600,2004]
for year in years:
    print(f"{year} is a leap year, {leap_year(year)}")'''
            
##1900 is a leap year False
##2000 is a leap year True
##1600 is a leap year True
##2004 is a leap year True


'''names=['Vaibhav', 'James', 'Hari']
for i in range(len(names)):
    print(i+1, names[i])'''

##1 Vaibhav
##2 James
##3 Hari

##>>> new=enumerate(names)
##>>> new
##<enumerate object at 0x0000020D83726E80>
##>>> new=list(new)
##>>> new
##[(0, 'Vaibhav'), (1, 'James'), (2, 'Hari')]
##>>> new[0]
##(0, 'Vaibhav')
##>>> type(new)
##<class 'list'>
##>>> type(new[0])
##<class 'tuple'>


'''names=['Vaibhav', 'James', 'Hari']
for i in enumerate(names,start=1):
    print(i)'''

##(1, 'Vaibhav')
##(2, 'James')
##(3, 'Hari')


#packing and unpacking
'''>>> i
(3, 'Hari')
>>> num,name=1
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    num,name=1
TypeError: cannot unpack non-iterable int object
>>> num,name=i
>>> num
3
>>> name
'Hari'
'''

'''names=['Vaibhav', 'James', 'Hari']
for num,name in enumerate(names,start=1):
    print(num,name)'''

##1 Vaibhav
##2 James
##3 Hari