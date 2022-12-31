import sys


class Edge:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length


class Node:
    def __init__(self, nodeSelf, root, length):
        self.nodeSelf = nodeSelf
        self.root = root
        self.length = length


def getRootNodes(childNode, charlist):
    nodeslist = []
    nodeslist.append(childNode)

    tmpNode = childNode

    while tmpNode.root is not None:
        for i in range(0, len(charlist)):
            if tmpNode.root is charlist[i].nodeSelf:
                nodeslist.append(charlist[i])
                tmpNode = charlist[i]
                break
    return nodeslist


def first_second_third_mst(input_file_path, output_file_path):
    MAX = sys.maxsize

    with open(input_file_path) as infile:
        vertices = int(infile.readline())
        primgraph = [[int(x) for x in line.split(',')] for line in infile]
        infile.close()    
    
    out = open(output_file_path, "w")
    
    if vertices == 0 or vertices == 1:
        out.write(str(0)+"\n")
        out.close()
        sys.exit()
        
        
    for i in range(vertices):
        for j in range(vertices):
            if i == j:
                primgraph[i][j] = MAX
        
    chararray = []
    for i in range(vertices):
        chararray.append(str(i))

    # inital
    charlist = []
    allEdgelist = []
    rootNode = Node(chararray[0], None, 0)
    charlist.append(rootNode)
    mid = []
    lowcost = []
    lowcost.append(-1)
    mid.append(0)
    n = len(chararray)
    for i in range(1, n):
        lowcost.append(primgraph[0][i])
        mid.append(0)
    mst_sum = 0

    # MST
    for i in range(0, n):
        tempList = primgraph[i]
        for j in range(i, n):
            if tempList[j] != MAX:
                edgeData = Edge(chararray[i], chararray[j], tempList[j])
                allEdgelist.append(edgeData)

    mstEdgelist = []
    for _ in range(1, n):
        minid = 0
        mindata = MAX
        for j in range(1, n):
            if lowcost[j] != -1 and lowcost[j] < mindata:
                minid = j
                mindata = lowcost[j]
        inputNode = Node(chararray[minid], chararray[mid[minid]], lowcost[minid])
        charlist.append(inputNode)

        for i in range(0, len(allEdgelist)):
            firstX = allEdgelist[i].x
            firstY = allEdgelist[i].y
            secondX = chararray[mid[minid]]
            secondY = chararray[minid]

            if (firstX is secondX) & (firstY is secondY):
                mstEdgelist.append(i)
            elif (firstX is secondY) & (firstY is secondX):
                mstEdgelist.append(i)

        mst_sum += mindata
        lowcost[minid] = -1
        for j in range(1, n):
            if lowcost[j] != -1 and lowcost[j] > primgraph[minid][j]:
                lowcost[j] = primgraph[minid][j]
                mid[j] = minid

    
    out.write(str(mst_sum)+"\n")
    

# Second-MST

    # Find the MST unused edges
    unUsedlist = []
    for i in range(0, len(allEdgelist)):
        if i not in mstEdgelist:
            unUsedlist.append(allEdgelist[i])

    mstTreelist = []
    
    # Traverse

    maxEdgelist = []
    getNodelists = []
    fatherNodes = []
    for i in range(0, len(unUsedlist)):
        unUsedEdge = unUsedlist[i]
        # Let two vertices back to root, and get list for each one
        nodelistA = []
        nodelistB = []

        isOtherFind = False
        for i in range(0, len(charlist)):
            if unUsedEdge.x is charlist[i].nodeSelf:
                nodelistA = getRootNodes(charlist[i], charlist)
                if isOtherFind:
                    break
                else:
                    isOtherFind = True
            elif unUsedEdge.y is charlist[i].nodeSelf:
                nodelistB = getRootNodes(charlist[i], charlist)
                if isOtherFind:
                    break
                else:
                    isOtherFind = True
        # Find parents of two vertices
        fatherNode = None
        fatherNodeIndex = 0
        index = abs(len(nodelistA) - len(nodelistB))
        if len(nodelistA) > len(nodelistB):
            tmplist = nodelistA[index:len(nodelistA)]

            for i in range(0, len(nodelistB)):
                nodeA = tmplist[i]
                nodeB = nodelistB[i]
                if nodeA.nodeSelf is nodeB.nodeSelf:
                    fatherNode = nodeA
                    fatherNodeIndex = len(nodelistB) - i
                    break
        else:
            tmplist = nodelistB[index:len(nodelistB)]

            for i in range(0, len(nodelistA)):
                nodeA = nodelistA[i]
                nodeB = tmplist[i]
                if nodeA.nodeSelf is nodeB.nodeSelf:
                    fatherNode = nodeA
                    fatherNodeIndex = len(nodelistA) - i
                    break
        fatherNodes.append(fatherNode)
        
        # 
        findMax = 0
        findMaxNode = None
        tmpNodelists = []
        for i in range(0, len(nodelistA) - fatherNodeIndex):
            if nodelistA[i].length > findMax:
                findMax = nodelistA[i].length
                findMaxNode = nodelistA[i]
                tmpNodelists = nodelistA

        for i in range(0, len(nodelistB) - fatherNodeIndex):
            if nodelistB[i].length > findMax:
                findMax = nodelistB[i].length
                findMaxNode = nodelistB[i]
                tmpNodelists =nodelistB

        getNodelists.append(tmpNodelists)

        maxEdgelist.append(findMaxNode)
        # Compute the MST on the list
        addSum = mst_sum + unUsedEdge.length - findMaxNode.length
        mstTreelist.append(addSum)
    
    sec_sum = min(mstTreelist)
    out.write(str(sec_sum)+"\n")
    


    edgeIndex = mstTreelist.index(min(mstTreelist))

    # Break and Connect
    for i in  range(0,len(charlist)):
        node = charlist[i]
        if node.nodeSelf is unUsedlist[edgeIndex].y:
            node.root = unUsedlist[edgeIndex].x
            node.length = unUsedlist[edgeIndex].length

    fathernode = fatherNodes[edgeIndex]

    changeNodes = []
    add = False
    findNodes = getNodelists[edgeIndex]
    for i in range(0, len(findNodes)):
        nodeA = findNodes[i]
        if nodeA.nodeSelf is unUsedlist[edgeIndex].y:
            add = True
        if nodeA.nodeSelf is fathernode.nodeSelf:
            add = False
        if add:
            changeNodes.append(nodeA.nodeSelf)

    tmpNodes = changeNodes[1:]
    revlist = tmpNodes[::-1]
    changeNodes = revlist

    if len(changeNodes)>0:
        for i in range(0, len(charlist)):
            node = charlist[i]
            index = 0
            for j in changeNodes:
                if node.nodeSelf is j:
                    if (i+1)>len(changeNodes):
                        node.root = unUsedlist[index].y
                    else:
                        node.root = changeNodes[i+1]
                index += 1


    thirdmstEdgelist = []
    for i in range(0, len(charlist)):
        node = charlist[i]
        
        for i in range(0, len(allEdgelist)):
            firstX = allEdgelist[i].x
            firstY = allEdgelist[i].y
            secondX = node.nodeSelf
            secondY = node.root

            if (firstX is secondX) & (firstY is secondY):
                thirdmstEdgelist.append(i)
            elif (firstX is secondY) & (firstY is secondX):
                thirdmstEdgelist.append(i)



    # Third-MST
    # Find those unused edged in second-MST
    thirdUnUsedlist = []
    for i in range(0, len(allEdgelist)):
        if i not in thirdmstEdgelist:
            thirdUnUsedlist.append(allEdgelist[i])


    thirdmstTreelist = []

    # Traverse
    for i in range(0, len(thirdUnUsedlist)):
        unUsedEdge = thirdUnUsedlist[i]
        # print(unUsedEdge.x,unUsedEdge.y)
        edgelength = unUsedEdge.length
        # Two vertices back to root and get two list splited
        nodelistA = []
        nodelistB = []

        isOtherFind = False
        for i in range(0, len(charlist)):
            if (unUsedEdge.x is charlist[i].nodeSelf):
                nodelistA = getRootNodes(charlist[i], charlist)
                if (isOtherFind):
                    break
                else:
                    isOtherFind = True
            elif (unUsedEdge.y is charlist[i].nodeSelf):
                nodelistB = getRootNodes(charlist[i], charlist)
                if (isOtherFind):
                    break
                else:
                    isOtherFind = True
        
        # Find two parents of two vertices
        fatherNode = None
        fatherNodeIndex = 0
        index = abs(len(nodelistA) - len(nodelistB))
        if (len(nodelistA) > len(nodelistB)):
            tmplist = nodelistA[index:len(nodelistA)]

            for i in range(0, len(nodelistB)):
                nodeA = tmplist[i]
                nodeB = nodelistB[i]
                if (nodeA.nodeSelf is nodeB.nodeSelf):
                    fatherNode = nodeA
                    fatherNodeIndex = len(nodelistB) - i
                    break
        else:
            tmplist = nodelistB[index:len(nodelistB)]

            for i in range(0, len(nodelistA)):
                nodeA = nodelistA[i]
                nodeB = tmplist[i]
                if (nodeA.nodeSelf is nodeB.nodeSelf):
                    fatherNode = nodeA
                    fatherNodeIndex = len(nodelistA) - i
                    break

        # Find smallest value between two lists
        findMaxA = 0
        for i in range(0, len(nodelistA) - fatherNodeIndex):
            if (nodelistA[i].length > findMaxA)&(nodelistA[i].length <= edgelength):
                findMaxA = nodelistA[i].length

        findMaxB = 0
        for i in range(0, len(nodelistB) - fatherNodeIndex):

            if (nodelistB[i].length > findMaxB)&(nodelistB[i].length <= edgelength):
                findMaxB = nodelistB[i].length

        # Computer the mst in the list
        findMax = 0
        if findMaxB>findMaxA:
            findMax = findMaxB
        else:
            findMax = findMaxA

        addSum = sec_sum + unUsedEdge.length - findMax
        thirdmstTreelist.append(addSum)
    
    third_sum = min(thirdmstTreelist)
    
    out.write(str(third_sum)+"\n")
    out.close()
    
    
    pass

#first_second_third_mst('input0.in', 'input0.out')
