tree= { }

def addToTree(parent,child):
    if parent not in tree:
        tree[parent]=[]
    if child not in tree:
        tree[child]=[]

    tree[parent].append(child)

def immediateChildren(parent):
    print "Immediate children of ",parent," are ",tree[parent]

def allChildren(parent,res):
    if len(tree[parent])!=0:
        map(res.append,tree[parent])
        for c in tree[parent]:
            res=allChildren(c,res)
            return res
    else:
        return res

def isAncestor(ancestor,child):
    children=allChildren(ancestor,[])
    if child in children:
        return True
    else:
        return False

ip=raw_input().strip().split()
pcNodes=map(lambda x:x.split('-'),ip)
for pc in pcNodes:
    addToTree(pc[0],pc[1])
print tree
immediateChildren('a')
immediateChildren('n')
print "All children of 'a' are ",allChildren('a',[])
print "All children of 'n' are ",allChildren('n',[])
print " 'a' is ancestor of 'e' ",isAncestor('a','e')
print " 'f' is ancestor of 'e' ",isAncestor('f','e')
