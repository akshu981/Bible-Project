def correlation_problem():
    dependent_var=[]
    independent_var=[]
    for i in range(0,1193):
        f=open('chapter'+str(i),'r')
        L=eval(f.read())
        f.close()
        ofs=L.count('of')
        dependent_var.append(ofs)
        length=len(L)
        independent_var.append(length)
    return(independent_var,dependent_var)

from random import *

def ttest_problem():
    first_sample_books=[]
    while len(first_sample_books)<10:
        r=randint(1,39)
        if r not in first_sample_books:
            first_sample_books.append(r)
    second_sample_books=[]
    while len(second_sample_books)<10:
        r=randint(40,66)
        if r not in second_sample_books:
            second_sample_books.append(r)
    Old_sample=[]
    New_sample=[]
    for number in first_sample_books:
        f=open('book'+str(number),'r')
        s=f.read()
        f.close()
        count=s.count('king')+s.count('King')
        Old_sample.append(count)
    for number in second_sample_books:
        f=open('book'+str(number),'r')
        s=f.read()
        f.close()
        count=s.count('king')+s.count('King')
        New_sample.append(count)    
    return(Old_sample,New_sample)

def ratio_problem():
    Paul_Is=0
    total_length=0
    for i in range(45,58):
        f=open('book'+str(i),'r')
        s=f.read()
        f.close()
        total_length=total_length+len(s.split(' '))
        Paul_Is=Paul_Is+s.count('I ')+s.count(' I.')+s.count('I;')+s.count('I:')+s.count('I,')
    f=open('book40','r')
    s=f.read()
    f.close()
    Mathew_Is=s.count('I ')+s.count(' I.')+s.count('I;')+s.count('I:')+s.count('I,')
    Mathew_length=len(s.split(' '))
    f=open('book41','r')
    s=f.read()
    f.close()
    Mark_Is=s.count('I ')+s.count(' I.')+s.count('I;')+s.count('I:')+s.count('I,')
    Mark_length=len(s.split(' '))
    Paul_ratio=Paul_Is/total_length
    Mathew_ratio=Mathew_Is/Mathew_length
    Mark_ratio=Mark_Is/Mark_length
    return(Paul_ratio,Mathew_ratio,Mark_ratio)

    
    


