def fibbo(n,list1):
    if list1[n] == -1:
        list1[n]=fibbo(n-1,list1)+fibbo(n-2,list1)
        return list1[n]
    else:
        return list1[n]



n=int(input("enter a value of n: "))

list1=range(0,n)
for i in range(0,n):
    list1[i]=-1

list1[0]=0
list1[1]=1

output=fibbo(n-1,list1)
print "fibbonaci element at ",n ,"possition is: ", output



