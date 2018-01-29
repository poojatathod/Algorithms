dict1={}

def addToTree(parent,child):
    if parent not in dict1:
        dict1[parent]=[]
    if child not in dict1:
        dict1[child]=[]
    dict1[parent].append(child)


def immediate_child(parent):
    print dict1[parent]

def all_children(parent,list1):
    if dict1[parent]!=0:
        map((list1.append),dict1[parent])
        for x in dict1[parent]:
            list1=all_children(x,list1)
        return list1
    else:
        return list1

def isAncestor(ancestor,child):
    list1=[]
    list1=all_children(ancestor,[])
    if child in list1:
        print 'TRUE'
    else:
        print 'FALSE'

input=raw_input().strip().split()
li=map((lambda x:x.split('-')),input)
for pc in li:
    addToTree(pc[0],pc[1])
print dict1

immediate_child('a')
print all_children('a',[])

isAncestor('n','f')
