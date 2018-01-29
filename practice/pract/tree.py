tree={}

def create(parent,child):
    if parent not in tree:
        tree[parent]=[]
    if child not in tree:
        tree[child]=[]

    tree[parent].append(child)

def immediatechild(parent):
    print "immediate child are ",tree[parent]

def allchildren(parent,list):
    if tree!=0:
        map(lambda x:list.append(x),tree[parent])
        for x in tree[parent]:
            allchildren(x,list)
    return list

def isancestor(ancestor,child):
    list1=[]
    list1=allchildren(ancestor,[])
    if child in list1:
        print 'true'
    else:
        print 'false'


str=raw_input().strip().split()
str=map(lambda x:x.split('-'),str)
for pc in str:
    create(pc[0],pc[1])
print tree
immediatechild('a')
print allchildren('b',[])
isancestor('n','g')
isancestor('n','d')
