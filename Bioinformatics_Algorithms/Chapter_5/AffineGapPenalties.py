import copy
import sys
sys.setrecursionlimit(999999999)

def ReadScoreMatrix(File):
    Matrix = []
    for line in open(File, 'r'):
        line = line.split()
        Matrix.append(line)
    Letters = Matrix.pop(0)
    for i in range(len(Matrix)):
        Matrix[i].pop(0)
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            Matrix[i][j] = int(Matrix[i][j])
    return Matrix, Letters

def Backtracking (v, w, aminosequence, matrix, opengap, extendgap):
    string1 = len(v)
    string2 = len(w)
    uppergrid = []
    middlegrid = []
    lowergrid = []
    backtrackup = []
    backtrackdown = []
    backtrackmiddle = []
    score = 0
    for i in range(string1 + 1):
        empty = []
        backempty = []
        for j in range(string2 + 1):
            empty.append(0)
            backempty.append("")
        uppergrid.append(copy.deepcopy(empty))
        middlegrid.append(copy.deepcopy(empty))
        lowergrid.append(copy.deepcopy(empty))
        backtrackdown.append(copy.deepcopy(backempty))
        backtrackup.append(copy.deepcopy(backempty))
        backtrackmiddle.append(copy.deepcopy(backempty))
    backtrackmiddle.pop()
    backtrackup.pop()
    backtrackdown.pop()
    #all functions above are used to build the grid and the backtrack matrices. There is a problem with building them on python, and it was necessary to use the deep copy function
    #the deep copy function allows to change one of them without chaning them all.
    for i in range(1, string1+1):
        for j in range(1, string2+1):
            Open1 = middlegrid[i-1][j] - opengap
            Gap1 = lowergrid[i-1][j] - extendgap
            lowergrid[i][j] = max(Open1, Gap1)
            lowercopy = copy.deepcopy(lowergrid[i][j])
            #There the deep copy was also needed, as the lowergrid could be changed later.
            if lowergrid[i][j] == Gap1:
                backtrackdown[i-1][j-1] = "lowergrid"
            else:
                backtrackdown[i-1][j-1] = "middle-to-lower"

            Open2 = middlegrid[i][j-1] - opengap
            Gap2 = uppergrid[i][j-1] - extendgap
            uppergrid[i][j] = max(Open2, Gap2)
            uppercopy = copy.deepcopy(uppergrid[i][j])
            #same case as for the lower grid

            if uppergrid[i][j] == Gap2:
                backtrackup[i-1][j-1] = "uppergrid"
            else:
                backtrackup[i-1][j-1] = "middle-to-upper"
            Amino1 = aminosequence[v[i-1]]
            Amino2 = aminosequence[w[j-1]]
            Score = matrix[Amino1][Amino2]
            # print("Score", Score)
            comparison = [int(lowergrid[i][j]), int(uppergrid[i][j]), int(middlegrid[i-1][j-1] + Score)]
            middlegrid[i][j] = max(comparison)
            #this step is trying to implement the book pseudo codes, by taking the max of the possible choices
            # print("lower", lowergrid[i][j])
            # print("upper", uppergrid[i][j])
            # print("score and middle", middlegrid[i-1][j-1] + Score)
            if middlegrid[i][j] == lowercopy:
                backtrackmiddle[i-1][j-1] = "lower-to-middle"
            elif middlegrid[i][j] == uppercopy:
                backtrackmiddle[i-1][j-1] = "upper-to-middle"
            else:
                backtrackmiddle[i-1][j-1] = "middlegrid"
            #this step is to try to build the back tracking
    # print("middle", backtrackmiddle)
    # print("up", backtrackup)
    # print("down", backtrackdown)

    return middlegrid[string1][string2], backtrackup, backtrackmiddle, backtrackdown

def LCS(backtrackup, backtrackmiddle, backtrackdown, v, w, i, j, level, aligned1, aligned2):
    # print(i)
    # print(j)
    if level == "uppergrid":
        backtracking = backtrackup
    elif level == "lowergrid":
        backtracking = backtrackdown
    elif level == "middlegrid":
        backtracking = backtrackmiddle
    if i < 0 and j < 0:
        print(aligned1[::-1])
        print(aligned2[::-1])
        return aligned1[::-1], aligned2[::-1]

    if backtracking[i][j] == "lowergrid":
        Alignment_of_v = aligned1 + v[i]
        Alignment_of_w = aligned2 + "-"
        return LCS(backtrackup, backtrackmiddle, backtrackdown, v, w, i-1, j, "lowergrid", Alignment_of_v, Alignment_of_w)
    elif backtracking[i][j] == "uppergrid":
        # print("Aqui1")
        Alignment_of_v = aligned1 + "-"
        Alignment_of_w = aligned2 + w[j]
        return LCS(backtrackup, backtrackmiddle, backtrackdown, v, w, i, j-1, "uppergrid", Alignment_of_v, Alignment_of_w)
    elif backtracking[i][j] == "middlegrid":
        Alignment_of_v = aligned1 + v[i]
        Alignment_of_w = aligned2 + w[j]
        return LCS(backtrackup, backtrackmiddle, backtrackdown, v, w, i-1, j-1, "middlegrid", Alignment_of_v, Alignment_of_w)
    elif backtracking[i][j] == "middle-to-lower":
        Alignment_of_v = aligned1 + v[i]
        Alignment_of_w = aligned2 + "-"
        return LCS(backtrackup, backtrackmiddle, backtrackdown, v, w, i-1, j, "middlegrid", Alignment_of_v, Alignment_of_w)
    elif backtracking[i][j] == "middle-to-upper":
        Alignment_of_v = aligned1 + "-"
        Alignment_of_w = aligned2 + w[j]
        return LCS(backtrackup, backtrackmiddle, backtrackdown, v, w, i, j-1, "middlegrid", Alignment_of_v, Alignment_of_w)
    elif backtracking[i][j] == "lower-to-middle":
        Alignment_of_v = aligned1
        Alignment_of_w = aligned2
        return LCS(backtrackup, backtrackmiddle, backtrackdown, v, w, i, j, "lowergrid", Alignment_of_v, Alignment_of_w)
    elif backtracking[i][j] == "upper-to-middle":
        Alignment_of_v = aligned1
        Alignment_of_w = aligned2
        return LCS(backtrackup, backtrackmiddle, backtrackdown, v, w, i, j, "uppergrid", Alignment_of_v, Alignment_of_w)
    #this recursive code is to build the aligned sequence based on the backtrack matrix build on the previous function. It is also an implementing of the book pseudo codes.

def AminoSequence():
    aminoacids_set = {'A':  0,'C':  1,'D':  2,'E':  3,'F':  4,'G':  5,'H':  6,'I':  7,'K':  8,'L':  9,'M': 10,'N': 11,'P': 12,'Q': 13,'R': 14,'S': 15,'T': 16,'V': 17,'W': 18,'Y': 19}
    return aminoacids_set
    #this create our "dictionary", i.e., the amino acid sequence and positions.

def Align(v,w):
    len_1 = len(v)
    len_2 = len(w)
    score = ReadScoreMatrix("SCOREMATRIX.txt")[0]
    extgap = 1
    opengap = 11
    score_grid = Backtracking(v,w,AminoSequence(),score,opengap,extgap)[0]
    backtrackup = Backtracking(v,w,AminoSequence(),score,opengap,extgap)[1]
    backtrackdown = Backtracking(v,w,AminoSequence(),score,opengap,extgap)[3]
    backtrackmiddle = Backtracking(v,w,AminoSequence(),score,opengap,extgap)[2]
    LCS(backtrackup, backtrackmiddle, backtrackdown, v, w, len_1-1,len_2-1, "middlegrid", "", "")
    print(score_grid)
    #this function is responsible to link the functions above with the gaps and extend gaps penalties.

if __name__ == "__main__":
    v = "PCQYGGTISRMTGNRKYKVFPEETLCGDGGMNVYIVRWLHKPRHIWPGETLNCFTDKKFNEDNKAMKLREAHSVWLDAAHGK"
    w = "PRQYGGTIPRMTGNRKIKVFPGMEVTIVRSIWDHKSRHIWPGETLNCFTDKKFNEDNKLLCGLQRPMCVWLNAAHGK"
    Align(v,w)


