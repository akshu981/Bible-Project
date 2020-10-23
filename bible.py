f=open('kjb','r')
s=f.read()
f.close()

book_list=s.split('\nNext:')
f=open('test_file','w')
f.write(str(book_list))
f.close()

book_list=s.split('\nNext:')
for i in range (0,66):
    f=open('book'+str(i+1),'w')
    s=book_list[i]
    start=s.find('Chapter 1')
    s=s[start:-1]+s[-1]
    f.write(s)
    f.close()



            

    




