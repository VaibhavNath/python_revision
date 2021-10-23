#list comprehension
'''x=['sam',20,'vaibhav','5']
name=[False if str(i).isnumeric() else True for i in x]'''

##>>> x
##['sam', 20, 'vaibhav', '5']
##>>> x[-1].isnumeric()     #python recognises the string contains numeric value
##True
##>>> x[0].isnumeric()
##False

##>>> name
##[True, False, True, False]

'''>>> help(any)
Return True if bool(x) is True for any x in the iterable.
    
    If the iterable is empty, return False.

>>> any(name)
True

>>> help(all)
Return True if bool(x) is True for all values x in the iterable.
    
    If the iterable is empty, return True.

>>> all(name)
False                   '''


##>>> help(str.join)
###Concatenate any number of strings.
##>>> hello='hello all'
##>>> hello
##'hello all'
##>>> hello.split()
##['hello', 'all']
##>>> hello_split=hello.split()
##>>> hello_split
##['hello', 'all']
##>>> ' '.join(hello_split)
##'hello all'
##>>> '.'.join(['ab', 'pq', 'rs'])
##'ab.pq.rs'



'''from string import ascii_uppercase as letters
from random import choice
a_f=list(letters[:6])

num=iter(range(1,7))
hidden = [choice(a_f) + str(choice(list(range(1,7))))for i in range(4)]
arr=[['O' for i in range(6)] for i in range(6)]
play=True
while play:
    num=iter(range(1,7))
    print(hidden)
    print(f'Find the {len(hidden)} hidden X"s')
    print('  '+' '.join(a_f))
    for i in arr:
        print(next(num),end = ' ')
        print(' '.join(i))
    move=input('''Q to Quit
enter move (eg A5):''')
    if move.lower()=='q':
        play=False
    else:
        if move in hidden:
            hidden.pop(hidden.index(move))
            move=list(move)
            arr[int(move[1])-1][a_f.index(move[0])]="X"
        else:
            move=list(move)
            arr[int(move[1])-1][a_f.index(move[0])]=" "
'''


##['C6', 'A3', 'D5', 'E6']
##  A B C D E F
##1 O O O O O O
##2 O O O O O O
##3 O O O O O O
##4 O O O O O O
##5 O O O O O O
##6 O O O O O O
##  Q to Quit
##enter move (eg A5):q