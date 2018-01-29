ipStrArr=[50,51,52,53,54,55,10,20,30,40]
list1=[]
list2=[]

for i in range(0,len(ipStrArr)):
    list1.append(1)

for i in range(0,len(ipStrArr)):
    if i==0:
        list2.append(0)
    else:
        if(ipStrArr[i-1])<ipStrArr[i]:
            list2.append(list1[i-1])
        else:
            list2.append(0)
    m=0
    m=1+max(list2)
    list2=[]
    list1[i]=m

print max(list1)





