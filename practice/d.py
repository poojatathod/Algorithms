list=[]
graphAdjacencyList={}
verticesDistances={}
verticesParents={}
FinalVertices={}

def adjacencyMatrix(edges):
    for i in range(n):
        list1=[]
        for j in range(n):
            list1.append(0)
        list.append(list1)

    for i in edges:
        list[int(i[0])][int(i[1])]=int(i[2])
        list[int(i[1])][int(i[0])]=int(i[2])
    return list



def adjacencyList(edges):
    for i in edges:
        if i[0] not in graphAdjacencyList:
            graphAdjacencyList[i[0]]=[]
        if i[1] not in graphAdjacencyList:
            graphAdjacencyList[i[1]]=[]

        graphAdjacencyList[i[0]].append([i[1],int(i[2])])
        graphAdjacencyList[i[1]].append([i[0],int(i[2])])

    return graphAdjacencyList


def toGetKey(value):
    for key in verticesDistances:
        if verticesDistances[key]==value:
            return key


def FindMinDistances(source):
    verticesDistances[source]=0
    calMinDistances()

def calMinDistances():
    p=0
    minval=min(verticesDistances.values())
    key=toGetKey(minval)
    FinalVertices[key]=minval
    del(verticesDistances[key])
    list=graphAdjacencyList[key]
    for val in list:
        if val[0] not in verticesDistances:
            p+=1
        else:
            if(minval+val[1])<verticesDistances[val[0]]:
                verticesDistances[val[0]]=(minval+val[1])
                verticesParents[val[0]]=key
    if ((len(verticesDistances))!=0):
        calMinDistances()
        return
    else:
        return


def toFindPath(source,dest,list2):
    list=verticesParents.keys()
    if dest in list:
        list2.append(dest)
        return toFindPath(source,verticesParents[dest],list2)
    elif dest==source:
        list2.append(source)
        return list2

def dijkastrasAlgo(source,dest):
    for key in graphAdjacencyList:
        verticesDistances[key]=9999

    FindMinDistances(source)
    for v in FinalVertices:
        print source,"to" ,v,"minimum distance is: ",FinalVertices[v]
    print "\n"

    path=toFindPath(source,dest,[])
    path.reverse()
    print path


print "Enter input String: "
edges=raw_input().strip().split()
edges=map(lambda x:x.split('-'),edges)
print edges
adjacencyList(edges)
for v in graphAdjacencyList:
    print v,graphAdjacencyList[v]
print "\n"
print "Enter source and destination:\n"
source,dest=raw_input().strip().split('-')
dijkastrasAlgo(source,dest)
