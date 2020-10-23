#lonely_words=[]
#gigantic_list=[]
#for i in range(1,67):
 #   j=1
  #  done= False
   # while not done:
    #    f=open('book'+ str(i)+'Chapter_'+ str(j),'r')
     #   try:
      #      L=eval(f.read())
       # except:
        #    print('the bad chapter is book '+str(i)+' chapter '+str(j))
         #   x=1/0
        #f.close()
        #L= list(set(L))
        #gigantic_list.extend(L)
        #j=j+1
        #try:
         #   f= open('book' +str(i) + 'Chapter_' +str(j), 'r')
          #  f.close()
        #except:
         #   done= True



#print('Gigantic list has been formed, start finding lonely words')


#already_checked=[]
#for i in range(0,len(gigantic_list)):
 #   if i%1000==0:
  #      print(i)
   # word= gigantic_list[i]
    #if word not in already_checked:
     #   lonely_words.append(word)
    #else:
     #   try:
      #      lonely_words.remove(word)
       # except:
        #    pass
    #already_checked.append(word)


##Finding overused words##

def grab_top_5(chapter):
    freqs=[]
    chapterset=set(chapter)
    for word in chapter:
        freqs.append([word,chapter.count(word)])
    freqs.sort(key=lambda x:x[1],reverse=True)
    to_return=[]
    for touple in freqs[0:5]:
        to_return.append(touple[0])
    return(to_return)

def build_all_top5():
    list_of_fives=[]
    for i in range(1,67):
        print(i)
        j=1
        done= False
        while not done:
            f=open('book'+ str(i)+'Chapter_'+ str(j),'r')
            L=eval(f.read())
            f.close()
            list_of_fives.append(grab_top_5(L))
            j=j+1
            try:
                f= open('book' +str(i) + 'Chapter_' +str(j), 'r')
                f.close()
            except:
                done= True
        return(list_of_fives)


def construct_important_words():
    gigantic_list=[]
    for i in range(1,67):
        print(i)
        j=1
        done= False
        while not done:
            f=open('book'+ str(i)+'Chapter_'+ str(j),'r')
            L=eval(f.read())
            f.close()
            L= list(set(L))
            gigantic_list.extend(L)
            j=j+1
            try:
                f= open('book' +str(i) + 'Chapter_' +str(j), 'r')
                f.close()
            except:
                done= True
    gigantic_list=list(set(gigantic_list))
    f=open('lonely_words','r')
    lw=eval(f.read())
    f.close()
    for word in lw:
        gigantic_list.remove(word)
    overused_words=[]
    list_of_fives= build_all_top5()
    for word in gigantic_list:
        count=0
        for common_5 in list_of_fives:
            if word in common_5:
                count=count+1
        if count>3:
            overused_words.append(word)
    for word in overused_words:
        gigantic_list.remove(word)
    return(gigantic_list)


    
    
        
