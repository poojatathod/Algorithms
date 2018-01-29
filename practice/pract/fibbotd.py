def fibbo(n,x,list1):
    if x>n:
        return list1[n]
    else:
        list1[x]=list1[x-1]+list1[x-2]
        return fibbo(n,x+1,list1)




print "Eneter a no n:"
n=input()
list1=[]
for i in range(0,n):
    list1.append(-1)
list1[0]=0
list1[1]=1
x=2
output=fibbo(n-1,x,list1)
print output
