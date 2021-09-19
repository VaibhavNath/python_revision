'''fruit={
    'banana':3,
    'apple':2,
    'orange':1
    }
for k , v in fruit.items():
    print(f'I have {v} {k} ')'''


##I have 3 banana 
##I have 2 apple 
##I have 1 orange  


'''from string import ascii_lowercase as lower
key= {}
for i in range(len(lower)):
    key[lower[i]]=1+i
    print(key)'''

##>>> key
##{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
## 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
## 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}


'''>>> for k,v in key.items():
	print(k,v)'''

	
##a 1
##b 2
##c 3
##d 4
##e 5
##f 6
##g 7
##h 8
##i 9
##j 10
##k 11
##l 12
##m 13
##n 14
##o 15
##p 16
##q 17
##r 18
##s 19
##t 20
##u 21
##v 22
##w 23
##x 24
##y 25
##z 26


'''from string import ascii_lowercase as lower
letters=lower
num=list(range(1,27))
key=dict(zip(letters,num))'''


##>>> key
##{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
## 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
## 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
## 'z': 26}

file='''1845
Everyone will agree with this, especially college students or freshers,
that to get connected with the recruiters and grab worthwhile job
opportunities for getting into your dream job is quite a tedious task.  

For instance – firstly, you need to look out if the particular company
is hiring for a candidate as per your skillset & qualifications or not
through various online or offline platforms. Then you’re required to
apply for it and wait till your resume gets shortlisted. Furthermore,
you need to clear their screening round
to get selected for further technical or managerial interview rounds'''


'''file=file.split()
book={}
for word in file:
    if word not in book:
        book[word]=1
    else:
        book[word] += 1'''

##>>> book
##{'1845': 1, 'Everyone': 1, 'will': 1, 'agree': 1, 'with': 2, 'this,': 1, 'especially': 1, 'college':
## 1, 'students': 1, 'or': 4, 'freshers,': 1, 'that': 1, 'to': 5, 'get': 2, 'connected': 1, 'the': 2,
## 'recruiters': 1, 'and': 2, 'grab': 1, 'worthwhile': 1, 'job': 2, 'opportunities': 1,
## 'for': 4, 'getting': 1, 'into': 1, 'your': 3, 'dream': 1, 'is': 2, 'quite': 1, 'a': 2,
## 'tedious': 1, 'task.': 1, 'For': 1, 'instance': 1, '–': 1, 'firstly,': 1, 'you': 2, 'need': 2,
## 'look': 1, 'out': 1, 'if': 1, 'particular': 1, 'company': 1, 'hiring': 1, 'candidate': 1,
## 'as': 1, 'per': 1, 'skillset': 1, '&': 1, 'qualifications': 1, 'not': 1, 'through': 1, 'various': 1,
## 'online': 1, 'offline': 1, 'platforms.': 1, 'Then': 1, 'you’re': 1, 'required': 1, 'apply': 1,
## 'it': 1, 'wait': 1, 'till': 1, 'resume': 1, 'gets': 1, 'shortlisted.': 1,
## 'Furthermore,': 1, 'clear': 1, 'their': 1, 'screening': 1, 'round': 1, 'selected': 1, 'further': 1,
## 'technical': 1, 'managerial': 1, 'interview': 1, 'rounds': 1}


'''def phone_number():
    x=input("enter the number:")
    print(f'({x[:3]}){x[3:6]}-{x[6:]}')'''

##>>> phone_number()
##enter the number:6386147580
##(638)614-7580


'''students=[
    'steve','john','tam','harry'
    ]
s_dict={student[0].upper(): student for student in students}
print(s_dict)'''


##{'S': 'steve', 'J': 'john', 'T': 'tam', 'H': 'harry'}


'''from random import shuffle, choice
def game(x,change=False):
    doors = ['goat','goat','cat']
    shuffle(doors)
##    print(doors)
    wins , loses = 0,0
    def no_switch():
        nonlocal wins , loses
        if 'cat'==choice(doors):
            wins +=1
        else:
            loses += 1
    def switch():
        door=['goat','goat','cat']
        nonlocal wins , loses
        door.pop(choice(range(3)))
        door.remove('goat')
        second_choice=door[0]
        if second_choice=='cat':
            wins +=1
        else:
            loses += 1

    for i in range(x):
        if change:
            switch()
        else:
            no_switch()
    print(f'wins: {wins} present wins: {(wins/x)}')
    print(f'loses:{loses} present loses:{(loses/x)}')
                
game(10000)
print()
game(10000,True)'''


##wins: 3310 present wins: 0.331
##loses:6690 present loses:0.669
##
##wins: 6680 present wins: 0.668
##loses:3320 present loses:0.332


#urlib
'''import urllib.request as url
page=url.urlopen('http://textfiles.com/etext/AUTHORS/POE/poe-raven-702.txt')

text=page.read()
text=text.decode()
page.close()

file=open('raven.txt','w')
file.write(text)

file.close()'''




'''file=file.split()
book={}
for word in file:
    if word not in book:
        book[word]=1
    else:
        book[word] += 1


def last(x):
    return x[-1]

book=book.items()
sort_book=sorted(book,key=last,reverse=True)
for i in sort_book[:10]:
    print(i[0],':',i[1])'''



##to : 5
##or : 4
##for : 4
##your : 3
##with : 2
##get : 2
##the : 2
##and : 2
##job : 2
##is : 2
