# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 12:10:12 2021

@author: rob
"""

#Reading in the file
def ReadFile (fileName):    
    with open(fileName, "r") as file:
        
        nodes = set()
        edges = {}
        
        for line in file:
            node,edge = line.strip().split('->')
            node = node.strip()
            edge = edge.strip().split(',')
            
            if node not in edges:
                edges[node] = []
                nodes.add(node)
            for e in edge:
                edges[node].append(e)
                nodes.add(e)
            
    return nodes, edges

def TopologicalOrdering(nodes,edges):
    #Variable Initialisation
    graph = []
    candidates = set()
    values = edges.values()
    for node in nodes:
        #Test for ba5d code
        """
        #for v1 in values:
            #print(v1)
            #if str(node) not in v1:
                #print(node)
                #continue
        """  
        #create set of nodes from dict listing all possible paths, not all nodes have outputs
        if str(node) not in [x for v in edges.values() for x in v] or str(node) in values:
            candidates.add(node)
    #TODO REMOVE IF USING ba5n!!!
    candilist = list(candidates)
    #Test for ba5d code
    """
    #for value in candilist:
     #   if value != '0':
      #      candidates.remove(value)
    """
    #goes through node by node removing edges to create an order of nodes
    while len(candidates) != 0:
        a = candidates.pop()
        graph.append(a)   
        #Try and catch to ignore an error which would crash the script where a node would have no more edges
        try:
            outEdges = edges.pop(a)
            for node in outEdges:
                  
                #Finds if node has no incmoing edges, if it has incoming edges next node
                if str(node) not in [x for v in edges.values() for x in v] or str(node) in values:
                    candidates.add(node)
        except:
            continue
    #removes edge
    for value in graph:
        if value in candilist:
            if value != '0':
                graph.remove(value)
    return graph
 
if __name__ == "__main__":
    fileName = '../dataSets/rosalind_ba5n.txt'
    nodes,edges = ReadFile(fileName)
    TopologicalOrdering(nodes, edges)
