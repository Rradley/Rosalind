def EditDistance(amino1,amino2):
    m=len(amino1)
    n=len(amino2)
    
    graph=[[0 for x in range(n+1)]for x in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0:               #if amino1 is empty, insert all amino2: edits=j
                graph[i][j]=j
            elif j==0:             #if amino2 is empty, remove all amino1: edits=i
                graph[i][j]=i
            elif amino1[i-1]==amino2[j-1]:     #if the character is the same, ignore and copy last value
                graph[i][j]=graph[i-1][j-1]
            else:                              #if the character is different, evaluate the possibilites (insert,removes,replace) and find the minumum edit operations
                graph[i][j]=1+min(graph[i][j-1], graph[i-1][j],graph[i-1][j-1])
    return graph[m][n]