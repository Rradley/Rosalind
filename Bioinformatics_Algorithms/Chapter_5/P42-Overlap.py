def Overlap(v, w):
    v="-"+v
    w="-"+w
    
    graph=[[0 for j in range(len(w))] for i in range(len(v))]   #create the Allignment graph for saved the scores
    BT=[[None for j in range(len(w))] for i in range(len(v))]        #create the backtrack for the movements

    for j in range(1, len(w)):
        graph[0][j]=graph[0][j-1]-2
        BT[0][j]="x"
        
    for i in range(1,len(v)):
        for j in range(1,len(w)):
            x=graph[i][j-1] - 2         #x and y are the penalties
            y=graph[i-1][j] - 2
            if v[i]==w[j]:
                z=graph[i-1][j-1] + 1    #match
            else:
                z=graph[i-1][j-1] - 2    #mismatch
            
            graph[i][j]=max(x,y,z)
            if graph[i][j]== z:          
                BT[i][j]="z"
            elif graph[i][j]==y:
                BT[i][j]="y"
            elif graph[i][j]==x:
                BT[i][j]="x"
                
    i = len(v) - 1
    j = max(range(len(w)), key=lambda x: graph[i][x])
    maxscore = graph[i][j]
    
    vp=""     #create the variable v' to save the allignment of v
    wp=""     #create the variable w' to save the allignment of w
    
    while BT[i][j] is not None:
        movement = BT[i][j]
        if movement == "z" :     #if the Backtrack was on diagonal, add the same Base to both v' and w'
            vp = v[i] + vp
            wp = w[j] + wp
            i -= 1
            j -= 1
        elif movement == "x" :   #if the Backtrack was on right, add "-" to v' and the same Base to w'
            vp = "-" + vp
            wp = w[j] + wp
            j -= 1
        elif movement == "y" :   #if the Backtrack was on down, add "-" to w' and the same Base to v'
            vp = v[i] + vp
            wp = "-" + wp
            i -= 1
    
    print(maxscore)
    print(vp)
    print(wp)