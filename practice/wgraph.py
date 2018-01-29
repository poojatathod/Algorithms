list=[]
n=input()
ip=raw_input().strip().split()
ip=map(lambda x:x.split('-'),ip)

for i in range(n):
    list1=[]
    for j in range(n):
        list1.append(0)
    list.append(list1)

for i in ip:
    list[int(i[0])][int(i[1])]=int(i[2])
    list[int(i[1])][int(i[0])]=int(i[2])

print list
