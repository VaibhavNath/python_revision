#second conversion , automate file naming , finding specific files.

'''def sec(x):
    d=x//86400
    h=(x%86400)//3600
    m=(x%3600)//60
    s=(x%60)
    print(f'{d:02}:{h:02}:{m:02}:{s:02}')
    ##or
##    print('{:02}:{:02}:{:02}:{:02}'.format(d,h,m,s))


print('d:h:m:s')
sec(86400)
sec(14008)
sec(90000)
sec(91000)
sec(91121)  '''


##d:h:m:s
##01:00:00:00
##00:03:53:28
##01:01:00:00
##01:01:16:40
##01:01:18:41


#automate file naming


'''import time
f_name=time.asctime().replace(' ','_').replace(':','_')+'.pkl'
##f_name_2=f_name.replace(' ','_')


print(f_name)
##print(f_name_2)
'''


##Mon_Sep_20_14_10_20_2021.pkl


'''import glob
files=glob.glob('*.pkl')
print(files)'''


##[]


'''x=[1,43,5,27,19]
x=sorted(x)
print(max(x))
print(min(x))
print('second largest',x[-2])
print('second smallest',x[1])'''


##43
##1
##second largest 27
##second smallest 5