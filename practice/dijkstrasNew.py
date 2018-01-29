weights={}
parents={}
graph={}
finalW={}

def relaxEdges(s,d,w):
    if (weights[s]+w)<weights[d]:
        weights[d]=weights[s]+w
        parents[d]=s
        return True


def reverseDict():
    temp={}
    for k in weights:
        temp[weights[k]]=k
    return temp

def dijkstras(edges,s,d):
    vertices=graph.keys()
    marked=[]

    for v in vertices:
        weights[v]=99999999
    weights[s]=0
    del weights[s]
    marked.append(s)
    finalW[s]=0

    while marked!=vertices:
        for e in edges:
            if e[1] not in  marked:
                s=relaxEdges(e[0],e[1],int(e[2]))
        temp=reverseDict()
        minw=min(temp.keys())
        marked.append(temp[minw])
        finalW[temp[minw]]=minw
        del weights[temp[minw]]



edges=map(lambda x:x.split("-"),raw_input("Enter edges: ").strip().split())
for e in edges:
    if e[0] not in graph:
        graph[e[0]]=[]
    if e[1] not in graph:
        graph[e[1]]=[]

    graph[e[0]].append(e[1])
    graph[e[1]].append(e[0])

dijkstras(edges,'A','D')
print weights
print parents
