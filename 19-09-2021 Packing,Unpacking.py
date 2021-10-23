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