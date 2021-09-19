#Random Password Generator

'''import random , string

def password(length,num=False,strength='weak'):
    """length of password , num if you want a number,and strength (weak,strong,very)"""
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    letter=lower + upper
    dig =string.digits
    punct = string.punctuation
    pwd = ''
    if strength == 'weak':
        if num:
            length -= 2
            for i in range(2):
                  pwd += random.choice(dig)          
        for i in range(length):
            pwd += random.choice(lower)
    elif strength == 'strong':
        if num:
            length -= 2
            for i in range(2):
                  pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(letter)
    elif strength == 'very':
        ran=random.randint(2,4)
        if num:
            length -= ran
            for i in range(ran):
                pwd += random.choice(dig)
        length -= ran
        for i in range(ran):
            pwd += random.choice(punct)
        for i in range(length):
            pwd += random.choice(letter)
    pwd=list(pwd)        
    random.shuffle(pwd)
    return ''.join(pwd)


print(password(6,num=True))

print(password(10,num=True,strength='strong'))

print(password(15,num=True,strength='very'))'''



##lbk6b9
##tWZOkAn14T
##{4z2V&2DIH2}H+S





##>>> name='vaibhav'
##>>> name=list(name)
##>>> name
##['v', 'a', 'i', 'b', 'h', 'a', 'v']
##>>> ''.join(name)
##'vaibhav'
##>>> ' '.join(name)
##'v a i b h a v'
##>>> '*'.join(name)
##'v*a*i*b*h*a*v'



#packing and unpacking

'''student=['john','sam','vaibhav','harry']    #['john', 'sam', 'vaibhav', 'harry']

grade=[6,7,8,8]                                #[6, 7, 8, 8]

classes=list(zip(student,grade)                #zip the lists   # [('john', 6), ('sam', 7), ('vaibhav', 8), ('harry', 8)]

new_student , grade=zip(*classes)              #unzip the list  '''


##>>> new_student
##('john', 'sam', 'vaibhav', 'harry')
##>>> grade
##(6, 7, 8, 8)




'''x='help'    '''

##>>> x
##'help'
##>>> dir(x)
##>>> help(x.center)
##>>> x.center(50,'#')
##'#######################help#######################'




'''x=['sam',42,'vaibhav',78,'john','20']
name=[False if str(i).isnumeric() else True for i in x]'''

##>>> name
##[True, False, True, False, True, False]








































