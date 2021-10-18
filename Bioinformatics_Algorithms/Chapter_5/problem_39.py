import sys
sys.setrecursionlimit(5000)

def LCSbacktrack(aminostr1, aminostr2, indA, SM, pen, local=True):

    len_amino1 = len(aminostr1)
    len_amino2 = len(aminostr2)

    backtrack = [[0 for i in range(len_amino2)] for j in range(len_amino1)]     
    s = [[0 for i in range(len_amino2+1)] for j in range(len_amino1+1)]

    for j in range(1,len_amino2+1):
        s[0][j] = s[0][j-1] - pen

    for i in range(1,len_amino1+1):
        s[i][0] = s[i-1][0] - pen

    for i in range(1,len_amino1+1):
        for j in range(1, len_amino2+1):

            i_aminostr1 = indA[aminostr1[i-1]]
            i_aminostr2 =  indA[aminostr2[j-1]]
            match = SM[i_aminostr1][i_aminostr2]
            if local:
                s[i][j] = max(0,s[i-1][j] - pen,s[i][j-1] - pen,s[i-1][j-1] + match)
            else:
                s[i][j] = max(s[i-1][j] - pen,s[i][j-1] - pen,s[i-1][j-1] + match)

            if s[i][j] == s[i-1][j] - pen:
                backtrack[i-1][j-1] = 'u'

            elif s[i][j] == s[i][j-1] - pen:
                backtrack[i-1][j-1] = 'l'

            elif s[i][j] == s[i-1][j-1] + match:
                backtrack[i-1][j-1] = 'd'

            elif s[i][j] == 0:
                backtrack[i-1][j-1] = 'r'
    return (s, backtrack)


def outputLCS(backtrack, aminostr1, aminostr2, i, j, al_str1, al_str2):

    
    if i < 0 and j < 0:
        return (al_str1[::-1], al_str2[::-1])
    
    if i < 0:
        nal_str1 = al_str1 + '-'
        nal_str2 = al_str2 + aminostr2[j]
        return outputLCS(backtrack,aminostr1,aminostr2,i,j-1, nal_str1, nal_str2)

    if j < 0:
        nal_str1 = al_str1 + aminostr1[i]
        nal_str2 = al_str2 + '-'
        return outputLCS(backtrack,aminostr1,aminostr2,i-1,j, nal_str1, nal_str2)

    if backtrack[i][j] == 'u':
        nal_str1 = al_str1 + aminostr1[i]
        nal_str2 = al_str2 + '-'
        return outputLCS(backtrack,aminostr1,aminostr2,i-1,j, nal_str1, nal_str2)
    elif backtrack[i][j] == 'l':
        nal_str1 = al_str1 + '-'
        nal_str2 = al_str2 + aminostr2[j]
        return outputLCS(backtrack,aminostr1,aminostr2,i,j-1, nal_str1, nal_str2)
    elif backtrack[i][j] == 'd':
        nal_str1 = al_str1 + aminostr1[i]
        nal_str2 = al_str2 + aminostr2[j]
        return outputLCS(backtrack,aminostr1,aminostr2,i-1,j-1, nal_str1, nal_str2)
    elif backtrack[i][j] == 'r':
        nal_str1 = al_str1 + aminostr1[i]
        nal_str2 = al_str2 + aminostr2[i]
        return (al_str1[::-1], al_str2[::-1])



def scorematrix(path):
    file = open(path, 'r')
    line = file.readline()

    SM = []
    line = file.readline().strip('\n')
    while line != "":
        line = [int(i) for i in line.split(' ')[1:] if i != '']
        SM.append(line)
        line = file.readline().strip('\n')

    return SM

def localAlignment(aminostr1,aminostr2):

    aminos = {'A':  0, 'C':  1, 'D':  2, 'E':  3, 'F':  4, 'G':  5, 'H':  6, 'I':  7, 'K':  8, 'L':  9, 'M': 10,
     'N': 11, 'P': 12, 'Q': 13, 'R': 14, 'S': 15, 'T': 16,'V': 17, 'W': 18, 'Y': 19}

    SM = scorematrix('PAM250.txt')
    pen = 5

    len_amino1 = len(aminostr1)
    len_amino2 = len(aminostr2)

    s, backtrack = LCSbacktrack(aminostr1, aminostr2, aminos, SM, pen)
    end= (0,0)

    largestDist = float('-inf')
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] > largestDist:
                largestDist = s[i][j]
                end = (i,j)
    i,j = end
    al_str1, al_str2 = outputLCS(backtrack, aminostr1, aminostr2, i-1, j-1, "", "") 

    return (s[i][j], al_str1, al_str2)


if __name__ == "__main__":
    
    file = open('../dataSets/rosalind_ba5f.txt', 'r')

    aminostr1 = file.readline().rstrip('\n')
    aminostr2 = file.readline().rstrip('\n')

    score, al_str1, al_str2  = localAlignment(aminostr1,aminostr2)

    print(score)
    print(al_str1)
    print(al_str2)