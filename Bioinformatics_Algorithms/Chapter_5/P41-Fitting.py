def FitAlig(v, w):
    graph = []
    for i in range(len(w)+1):
        graph.append([0]*(len(v)+1))

    for i in range(1, len(w)+1):
        for j in range(1, len(v)+1):
            x = graph[i][j-1] - 1      #insert
            y = graph[i-1][j] - 1      #remove
            if w[i-1] == v[j-1]:            
                z = graph[i-1][j-1] + 1   #match
            else:
                z = graph[i-1][j-1] - 1   #missmatch

            graph[i][j] = max(x, y, z)
    
    maxscore = max(graph[-1])
    for k in range(len(graph[-1])-1, -1, -1):
        if graph[-1][k] == maxscore:
            j = k                   #to initialize counter "j" in the end of the sequence
            break

    vp = ""               #save the allignment for first seq
    wp = ""               #save the allignment for second seq
    i = len(graph) - 1    #initialize the counter "i" in the end of the sequence
    while True:
        if graph[i][j] == graph[i-1][j-1] + [-1, 1][v[j-1] == w[i-1]]:   #if match: copy the same base to the allignments seq
            vp = v[j-1] + vp
            wp = w[i-1] + wp
            i -= 1
            j -= 1
        else:
            move = max(graph[i][j-1], graph[i-1][j])
            if move == graph[i][j-1]:                      #if the movement was to right, add the "-" to the second seq
                vp = v[j-1] + vp
                wp = "-" + wp
                j -= 1
            elif move == graph[i-1][j]:                    #if the movement was to down, add the "-" to the second seq
                vp = "-" + vp
                wp = w[i-1] + wp
                i -= 1

        if i == 0 or j == 0:
            break
    
    print(maxscore)
    print("".join(vp))
    print("".join(wp))
