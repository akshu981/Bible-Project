for i in range(1,67):
    f=open('book_'+str(i),'r')
    s=f.read()
    f.close()
    for j in range(1,151):
        s=s.replace('Chapter '+str(j)+'\n','*****')
    this_book=s.split('*****')
    j=1
    done=False
    while not done:
        f=open('book'+str(i)+'Chapter_'+str(j),'w')
        this_chapter=this_book[j]
        this_chapter=this_chapter.lower()
        bad_chars='0123456789?.\',:;!-()\n\t'
        for bc in bad_chars:
            this_chapter=this_chapter.replace(bc,'')
        chapter_as_list=this_chapter.split(' ')
        f.write(str(chapter_as_list))
        f.close()
        j=j+1
        try:
            test=this_book[j]
        except:
            done=True
            

    




