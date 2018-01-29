def fibbodt(n,list1):
    if list1[n]==-1:
        list1[n]=fibbodt(n-1,list1)+fibbodt(n-2,list1)
        return list1[n]
    else:
        return list1[n]

print "Enter a value of n: "
n=input()
list1=[]
for i in range(0,n):
    list1.append(-1)
list1[0]=0
list1[1]=1

output=fibbodt(n-1,list1)
print output

