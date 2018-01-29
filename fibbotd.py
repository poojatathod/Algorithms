def fibbotd(n,x,list1):
    if x>n :
        return list1[n]
    else:
            list1[x]=list1[x-1]+list1[x-2]
            return fibbotd(n,x+1,list1)



n=int(input( "enter a value n: "))
list1=range(0,n)
x=2
for i in range(0,n):
    list1[i]=-1

list1[0]=0
list1[1]=1

output=fibbotd(n-1,x,list1)
print "fibbonaci no at ",n ,"position is: ",output
