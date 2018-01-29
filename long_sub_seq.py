
ls=[15,10,8,1,2,9,3,4,5,6,3,7]
temp=[]
ls1=[]
temp1=[]
for i in ls:
    ls1.append(0)


def getmaxseq(j,ls,ls1):
    if j==0:
        return [1]
    for i in range(0,j):
        if (ls[i]<ls[j]):
            temp1.append(ls1[i]+1)
        else:
            temp1.append(ls1[i]+1)



j=0
for i in ls:
    temp=getmaxseq(j,ls,ls1)
    j+=1
    val=max(temp)
    ls1[i]=val

print max(ls1)


