#recursion , command line , dictionaries

#factorial of one number
'''def factorial(n):
    if n>=0:
        if n==0:
            return 1
        else:
            return n*factorial(n-1)
    else:
        return 'Negative'    '''

##print(factorial(0))    #1
##print(factorial(-2))     #Negative
##print(factorial(5))     #120

#factorial of may numbers at once
'''def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

test=[3,4,1,2,5,100]
for i in test:
    print(factorial(i))'''

##6
##24
##1
##2
##120
##93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000


#lottery powerball
'''def odds(balls,pick,power=False):
    """enter number a regilar balls"""
    from math import factorial as fact
    p_ball=1
    if power:
        p_ball=int(input("enter number of powerballs:"))
    return(fact(balls)/(fact(5)*fact(balls-pick))*p_ball)*p_ball

print(f"{odds(69,6):,}")'''


'''import sys
print(sys.argv)'''

##C:\Users\ACER\Desktop>python 16-09-2021.py how are you
##['16-09-2021.py', 'how', 'are', 'you']


'''import sys
if len(sys.argv)>1:
   print(f"Hello {sys.argv[1]}")
else:
    print(f"Hello world!")'''

'''import sys
if len(sys.argv)==2:
    print(f"Hello {sys.argv[1]}")
    print(sys.argv)
elif len(sys.argv)==3:
    print(f"Hello {sys.argv[1]},I hear you{sys.argv[2]}")
    print(sys.argv)
else:
    print(f"Hello world!")
    print(sys.argv)'''



##C:\Users\ACER\Desktop>16-09-2021.py  Sam
##Hello Sam
##
##C:\Users\ACER\Desktop>16-09-2021.py  46
##Hello 46
##
##C:\Users\ACER\Desktop>16-09-2021.py sam 43
##Hello sam,I hear you43
##
##C:\Users\ACER\Desktop>16-09-2021.py sam  43
##Hello sam,I hear you43
##
##C:\Users\ACER\Desktop>16-09-2021.py sam
##Hello sam
##['C:\\Users\\ACER\\Desktop\\16-09-2021.py', 'sam']
##
##C:\Users\ACER\Desktop>16-09-2021.py sam 42
##Hello sam,I hear you42
##['C:\\Users\\ACER\\Desktop\\16-09-2021.py', 'sam', '42']
##
##C:\Users\ACER\Desktop>16-09-2021.py sam 42 52
##Hello world!
##['C:\\Users\\ACER\\Desktop\\16-09-2021.py', 'sam', '42', '52']


#dictionary
'''fruit={'banana':3,'apple':2}
for i in fruit:
    print(i)'''
    
##banana
##apple

fruit={'banana':3,'apple':2}
for k,v in fruit.items():
    print(f'I have {v} {k}')

##I have 3 banana
##I have 2 apple