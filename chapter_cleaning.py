def strip_empties(L):
    while '' in L:
        L.remove('')

for i in range(1,67):
    j=1
    done=False
    while not done:
        f=open('book'+ str(i)+'Chapter_'+ str(j),'r')
        L=eval(f.read())
        f.close()
        strip_empties(L)
        f=open('book' +str(i)+'Chapter_'+ str(j),'w')
        f.write(str(L))
        f.close()
        j=j+1
        try:
            f=open('book'+ str(i)+'Chapter_'+str(j),'r')
        except:
            done=True
