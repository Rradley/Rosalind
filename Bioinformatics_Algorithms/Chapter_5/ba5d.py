# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:51:35 2021

@author: rob
"""
from ba5n import TopologicalOrdering,topological_ordering


def ReadFile (fileName):    
    with open(fileName, "r") as file:
        source = file.readline()
        sink = file.readline()

        graph = []
        
        for line in file:
            row,weight = line.strip().split(':')
            node1,node2 = row.strip().split('->')
            
            graph.append((int(node1),int(node2),int(weight)))
            
    return source,sink,graph

def BuildDict(graph):
    dictGraph = {}
    nodes = set()
    
    
    for i in range (len(graph)):
        List=[]
        nodes.add(str(graph[i][0]))
        nodes.add(str(graph[i][1]))
        for j in range(len(graph)):
            if graph[i][0] == graph[j][0]:
                List.append(str(graph[j][1]))
        
        
        dictGraph[str(graph[i][0])] = List
    return nodes,dictGraph


def LongestPath(source,sink,graph):
      
    """
    nodes, dictGraph = BuildDict(graph)
    dictGraph1 = dictGraph.copy()
    topOrd = TopologicalOrdering(nodes, dictGraph) 
    
    #Initialise Variables
    queue = []
    weights = []
    visited = []  
    currentNodeList = []
    visit = 0
    weight = 0
    returnDict = {}
    visited.append(int(source))

    #Go through topological ordered graph and loop through initialising the queue
    for key, variables in dictGraph1.items():
        if int(key) == int(source):             
            for i in range(len(variables)):
                for j in range(len(graph)):
                        if int(graph[j][0]) == int(key) and int(graph[j][1]) == int(variables[i]):
                            queue.append(graph[j][1])
                            weights.append(graph[j][2])
                            
                            #Debugging Print tests
                            #print('node1',graph[j][0])
                            #print('node2',graph[j][1])
                            #print('weight',graph[j][2])
                            #print('')
    #visited.append(int(source)) 
    
        #Breadth first search to find the longest paths from source to sink (DOESNT WORK)
    while queue:
        currentNode = queue.pop(0)
        #weight += weights.pop(0)
        print('currentNode',currentNode)
        
        parent = (list(dictGraph1.keys())[list(dictGraph1.values()).index(str(currentNode))])
        print(parent)
        returnDict[currentNode] = (parent)
        
        if currentNode not in visited:
            visited.append(currentNode)
            
            if currentNode == int(sink):
                print(returnDict)                        
                return visited

            for node in queue:
                print('node',node)
                if node not in visited:
                    for x in range (len(graph)):
                        if node == graph[x][0]:
                            queue.append(graph[x][1])
                            
                            #weights.append(graph[x][2])
                
                #currentNodeList = []
                        
    print(returnDict)                        
    print('weightFIN1',weight)
    print('visitedFIN1',visited)
    
    visited.append(node)
    queue.append(node)

   # while queue:
    #    s = queue.pop(0) 
     #   print (s, end = " ") 
#
 #       for neighbour in graph[s]:
  #          if neighbour not in visited:
   #             visited.append(neighbour)
    #            queue.append(neighbour)
                 
"""
#Pseudo code for the problem
"""
longest-path(G)
✄ Input: Weighted DAG G = (V, E)
✄ Output: Largest path cost in G
Topologically sort G
for each vertex v ∈ V in linearized order
do dist(v) = max(u,v)∈E {dist(u) + w(u, v)}
return maxv∈V {dist(v)}
"""

#Main function to run the script
if __name__ == "__main__":
    fileName = '../dataSets/rosalind_ba5d.txt'
    source,sink,graph = ReadFile(fileName)
    print(LongestPath(source,sink,graph))
    