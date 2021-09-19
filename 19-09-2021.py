#class creation, method of class, object initialisation


'''class rect():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        print(f'your rectangle is {length} by {breadth}')
    def perim(self):
        print(2*self.length*self.breadth)

    def area(self):
        print(self.length*self.breadth)


a=rect(4,5)     #object initialisation
a.perim()       #call of function from class
a.area()        #call of function from class'''


##your rectangle is 4 by 5
##40
##20



'''class rect():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def __repr__(self):
        return "rect({self.length},{self.breadth})".format(self=self)

    def __str__(self):
        return f"your rect is {self.length} by {self.breadth}"
        

    def perim(self):
        print(2*self.length*self.breadth)

    def area(self):
        print(self.length*self.breadth)


a=rect(4,5)   #object initialisation'''



## >>> a
## rect(4,5)
## >>> repr(a)
## 'rect(4,5)'
## >>> str(a)
## 'your rect is 4 by 5'



'''class Dog:
    species='canine'
    voice='bark'

class poodle(Dog):
    pass


rusty=poodle()
print('voice:',rusty.voice)
print('species:',rusty.species)'''


##voice: bark
##species: canine



#iterator

'''name='Vaibhav'
name=iter(name)'''


##>>> next(name)
##'V'
##>>> next(name)
##'a'
##>>> next(name)
##'i'
##>>> next(name)
##'b'
##>>> next(name)
##'h'
##>>> next(name)
##'a'
##>>> next(name)
##'v'


#generators

'''def series(num):
    n=0
    while n<num:
        yield n     #Any function that contains a yield keyword is termed a generator.
                    #Hence, yield is what makes a generator.
                    #yield in Python can be used like the return statement in a function. When done so,
                    #the function instead of returning the output, it returns a generator that can
                    #be iterated upon.
        n +=1
    
five=series(5)'''


##>>> five
##<generator object series at 0x000001B822A48B30>
##>>> next(five)
##0
##>>> next(five)
##1
##>>> next(five)
##2
##>>> next(five)
##3
##>>> next(five)
##4


#round off number to nearest multiple of 5 if difference between number
#and multiple of 5 is <= 2
'''
78-->80
77-->77
94-->95
72-->72
74-->75

'''


'''def fives(x):
    if x%5==4 or x%5==3:
        x +=(5-x%5)
    print(x)

grades=[74,86,92,73,84,100]
for grade in grades:
    print(grade,end=' '),fives(grade)'''


##74 75
##86 86
##92 92
##73 75
##84 85
##100 100




