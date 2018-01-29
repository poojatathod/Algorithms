tree={}


def createTree(parent,child):
    if parent not in tree:
        tree[parent]=[]
    if child not in tree:
        tree[child]=[]

    tree[parent].append(child)

def immediatechild(parent):
    print "immediate child of ",parent, "are", tree[parent]


def allchild(parent,list):
    if tree!=0:
        map((lambda x:list.append(x)),tree[parent])
        for x in tree[parent]:
            allchild(x,list)
    return list

def isancestor(ancestor,child):
    list1=[]
    list1=allchild(ancestor,[])
    if child in list1:
        print 'TRUE'
    else:
        print 'FALSE'

ip=raw_input().strip().split()
ip=map(lambda x:x.split('-'),ip)
for pc in ip:
    createTree(pc[0],pc[1])
print tree
immediatechild('a')
print allchild('a',[])
isancestor('a','d')

