def easy_chapters():
    chapter_number=0
    for i in range(1,67):
        j=1
        done=False
        while not done:
            f=open('book'+str(i)+'Chapter_'+str(j),'r')
            s=f.read()
            f.close()
            f=open('chapter'+str(chapter_number),'w')
            f.write(s)
            f.close()
            j=j+1
            chapter_number=chapter_number +1
            try:
                f=open('book'+str(i)+'Chapter_'+str(j),'r')
                f.close()
            except:
                done=True

f=open('important_words','r')
global iw
iw=eval(f.read())
f.close()

def grab_weight(chapter_a,chapter_b):
    weight=0
    for word in chapter_a:
        if word in iw and word in chapter_b:
            weight=weight+1
    return(weight)

def build_adjacency_matrix():
    AM=[]
    for i in range(0,1193):
        print(i)
        this_row=[]
        for j in range(0,1193):
            if j%100==0:
                print(j)
            if i>j:
                this_row.append(AM[j][i])
            elif i==j:
                this_row.append(1)
            else:
                f=open('chapter'+str(i),'r')
                a=eval(f.read())
                f.close()
                f=open('chapter'+str(j),'r')
                b=eval(f.read())
                f.close()
                this_row.append(grab_weight(a,b))
        AM.append(this_row)
    return(AM)
                
                    
                    
                
    
