import numpy as np
from AffineGapPenalties import ReadScoreMatrix
from AffineGapPenalties import AminoSequence
#import the functions to read the score matrix and the amino acid sequence


def middleEdge(v,w, indels):
    # a new middle edge code needed to be done, as the previous one was taking too much processing time
    Matrix = ReadScoreMatrix('SCOREMATRIX.txt')[0]
    n = len(v)
    m = len(w)
    middleColumn = int(round(m/2) - 1)
    columnb = np.zeros(n+1) #create the column before
    for j in range(1,middleColumn+2):
        column =  np.zeros(n+1) #create the actual column
        column[0] = columnb[0] -indels

        for i in range(1,n+1):
            Upward = column[i-1] - indels
            Start2 = columnb[i] - indels

            if middleColumn < len(w):
                indexW =  AminoSequence()[w[j-1]]
                indexV = AminoSequence()[v[i-1]]

                comparison = Matrix[indexV][indexW] #compare the score

                going = columnb[i-1] + comparison
                column[i] = max(Upward, Start2, going)
            else:
                column[i] = max(Upward, Start2)

        if j < middleColumn+1:
            columnb = column
        begin_row = np.argmax(columnb)
        begin = (begin_row, j-1) #builds the incoming node on the middle column

        score = columnb[begin_row]
        right = column[begin_row]

        if begin_row < len(column)-1:
            diagonal= column[begin_row+1]
            down= columnb[begin_row+1]
        else:
            diagonal= -800000000000000
            down= -800000000000000
        direction = right
        dirStr = 'right'
        end = (begin_row, j)
        if diagonal >= direction:
            direction = diagonal
            dirStr = 'diagonal'
            end = (begin_row+1,j)

        if down >= direction:
            direction = end
            dirStr = 'down'
            end = (begin_row+1,j-1)
        #the next node of the middle edge is built

        middle_node = begin
        incoming_from_middle_node = end

        return middle_node, incoming_from_middle_node

def LSA(v, w, start1, bottom, start2, right):
    #it is needed to enter with the indel penalty here
    Indels = 5
    m = ""
    n = ""
    #tries to build recursion with two new strings m and n which size will vary
    for i in range(bottom):
        m += v[i]
    for j in range(right):
        n += w[j]
    middle = int((right+start2)/2)
    while len(m) and len(n) != 0:
        middle_edge = middleEdge(m, n, Indels) #recursive programing using the middleEdge function
        print("middle_edge", middle_edge)
        middle_node = middle_edge[0][0] #problem! I didn't found how to stop the loop. Therefore this crashes the program.
        LSA(v, w, start1, middle_node, start2, middle)
        if middle_edge[0][0] == middle_edge[1][0] or (middle_edge[1][0] - middle_edge[0][0] == 1 and middle_edge[1][1] - middle_edge[0][1] == 1):
            middle += 1
        if middle_edge[0][1] == middle_edge[1][1] or (middle_edge[1][0] - middle_edge[0][0] == 1 and middle_edge[1][1] - middle_edge[0][1] == 1):
            middle_node += 1
        return LSA(v, w, middle_node, bottom, middle, right)

if __name__ == "__main__":
    v = "PLEASANTLY"
    w = "MEASNLY"
    start1 = 0
    bottom = len(v)
    right = len(w)
    start2 = 0
    print(LSA(v, w, start1, bottom, start2, right))
