#shopping list

'''##f = open('test1.txt','w')  #creates a new file in write mode
f = open('test1.txt','a')    #opens file in append mode
f.write('hi how are you')    #overwrite the entite content of file
f.close()
f=open("test1.txt")
print(f.read())
f.close()'''


'''with open('test1.txt')as f:     #here we dont need tO close the file,file get closed automatically
    print(f.read())
with open('test1.txt','w')as f:
    a=f.write('hello dear whats up')
with open('test1.txt')as f:
    print(f.read())'''


'''def my_list():
    while True:
        with open('shoppig_list.txt','a+')as file:
##            print(file.tell())
            item=input('enter items:')            
            if item == 'exit':
                break                
            elif item =='list':
##                print(file.tell())
                file.seek(0)
                print(file.read())
            else:
                file.write(item +'\n')
         

my_list()'''
        
##enter items:list
##egg
##bread
##toast
##egggggs
##peanut
##lo
##loo
##egg
##plo
##
##enter items:chicken
##enter items:exit


#idle shell

##>>> f=open('shoppig_list.txt')
##>>> f.read()
##'egg\nbread\ntoast\negggggs\npeanut\nlo\nloo\negg\nplo\nchicken\n'
##>>> f.tell()
##64
##>>> f.seek(0)
##0
##>>> print(f.read())
##egg
##bread
##toast
##egggggs
##peanut
##lo
##loo
##egg
##plo
##chicken


def my_list():
    while True:
        with open('shopping_list.txt','a+')as file:
##            print(file.tell())
            item=input('enter items:')            
            if item == 'exit':
                break                
            elif item =='list':
##                print(file.tell())
                file.seek(0)
                items=list(enumerate(file.read().split(),1))
                for count, item in items:
                     print(f'{count:3d}) {item}')
            else:
                    file.write(item +'\n')

my_list()


##enter items:list
##  1) egg
##  2) bread
##  3) toast
##  4) egggggs
##  5) peanut
##  6) lo
##  7) loo
##  8) egg
##  9) plo
## 10) chicken