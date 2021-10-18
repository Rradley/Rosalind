# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 12:10:12 2021

@author: rob
"""

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
    graph = []
    candidates = set()
    values = edges.values()
    for node in nodes:
        """
        #for v1 in values:
            #print(v1)
            #if str(node) not in v1:
                #print(node)
                #continue
        """   
        if str(node) not in [x for v in edges.values() for x in v] or str(node) in values:
            candidates.add(node)
    #TODO REMOVE IF USING ba5n!!!
    candilist = list(candidates)
    """
    #for value in candilist:
     #   if value != '0':
      #      candidates.remove(value)
    """
    while len(candidates) != 0:
        a = candidates.pop()
        graph.append(a)       
        try:
            outEdges = edges.pop(a)
            for node in outEdges:
                  
                #Finds if node has no incmoing edges, if it has incoming edges next node
                if str(node) not in [x for v in edges.values() for x in v] or str(node) in values:
                    candidates.add(node)
        except:
            continue
    for value in graph:
        if value in candilist:
            if value != '0':
                graph.remove(value)
    return graph
 
if __name__ == "__main__":
    fileName = '../dataSets/rosalind_ba5n.txt'
    nodes,edges = ReadFile(fileName)
    TopologicalOrdering(nodes, edges)

def topological_ordering(graph):
    '''Returns a topological ordering for the given graph.'''
    # Initialize and covert variables appropriately.
    graph = set(graph)
    ordering = []
    candidates = list({edge[0] for edge in graph} - {edge[1] for edge in graph})

    # Get the topological ordering.
    while len(candidates) != 0:
        # Add the next candidate to the ordering.
        ordering.append(candidates[0])

        # Remove outgoing edges and store outgoing nodes.
        temp_nodes = []
        for edge in filter(lambda e: e[0] == candidates[0], graph):
            graph.remove(edge)
            temp_nodes.append(edge[1])

        # Add outgoing nodes to candidates list if it has no other incoming edges.
        for node in temp_nodes:
            if node not in {edge[1] for edge in graph}:
                candidates.append(node)

        # Remove the current candidate.
        candidates = candidates[1:]

    return ordering
