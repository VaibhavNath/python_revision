'''##sen='hi vaibhav'
##coma='sam, tom, harry'

name=input("please enter names use commas:").split(',')
print(name)'''
##please enter names use commas:sam , harry , tom
##['sam ', ' harry ', ' tom']

'''name=input("please enter names use commas:").split(',')
names=[i.strip() for i in name]
print(names)'''
##please enter names use commas:sam, tom, pete,harry
##['sam', 'tom', 'pete', 'harry']


#ord returns the ascii value of alphabets
##>>> ord('a')
##97
##>>> ord('b')
##98


'''x='abcaafahbaabdfgz'
sub=x[0]
long, length = sub ,1
for letter in x[1:]:
    if ord(sub[-1])<= ord(letter):
        sub += letter
        if len(sub) > length:
            length = len(sub)
            long = sub
            print(long)
    else:
            sub = letter
print(long)'''

##ab
##abc
##aabd
##aabdf
##aabdfg
##aabdfgz
##aabdfgz

#count number of substring in a string.
'''dad='dadaddadaadada'
count , place=0,0
while dad.find('dad',place)>=0:
    place=dad.find('dad',place) + 1
    count+=1
print(count)'''

##4


##>>> import re
##>>> help(re)
##
##>>> import string
##>>> dir(string)
##>>> letters=string.ascii_lowercase
##>>> letters
##'abcdefghijklmnopqrstuvwxyz'
##>>> letter=string.ascii_letters
##>>> letter
##'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
##>>> al=string.ascii_uppercase
##>>> al
##'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

'''>>> from math import pi
>>> pi
3.141592653589793

>>> import math
>>> o=math.pi
>>> o
3.141592653589793'''


'''from string import ascii_lowercase as lower   #lower stores value of ascii_lowercase i.e abcdefghijklmnopqrstuvwxyz
abc=' '
for letter in lower:
    abc += letter +'*'
    print(abc)'''

## a*
## a*b*
## a*b*c*
## a*b*c*d*
## a*b*c*d*e*
## a*b*c*d*e*f*
## a*b*c*d*e*f*g*
## a*b*c*d*e*f*g*h*
## a*b*c*d*e*f*g*h*i*
## a*b*c*d*e*f*g*h*i*j*
## a*b*c*d*e*f*g*h*i*j*k*
## a*b*c*d*e*f*g*h*i*j*k*l*
## a*b*c*d*e*f*g*h*i*j*k*l*m*
## a*b*c*d*e*f*g*h*i*j*k*l*m*n*
## a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*
## a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*
## a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*
## a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*
## a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*
## a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*
## a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*
## a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*
## a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*
## a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*
## a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*
## a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*


##x='abcaafahbaabdfgz'
'''from string import ascii_lowercase as lower
abc =''
abc='*'.join(lower)
abc +='*'''

##>>> abc
##'a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*'

import re
dad='dadaddadaadada'
##found=re.findall(r'(?=(\w+))',dad)
found=re.findall(r'(?=(\w\w\w))',dad)
dads=[dad for dad in found if dad == 'dad']
print(len(dads))    #4


##['dadaddadaadada', 'adaddadaadada', 'daddadaadada', 'addadaadada', 'ddadaadada', 'dadaadada',
## 'adaadada', 'daadada', 'aadada', 'adada', 'dada', 'ada', 'da', 'a']

##['dad', 'ada', 'dad', 'add',
## 'dda', 'dad', 'ada', 'daa', 'aad', 'ada', 'dad', 'ada']




























