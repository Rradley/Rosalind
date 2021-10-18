import sys
sys.setrecursionlimit(5000)

def LCSbacktrack(str1, str2):

    len_str1 = len(str1)
    len_str2 = len(str2)
    backtrack= [[0 for i in range(len_str2)] for j in range(len_str1)]
    s = [[0 for i in range(len_str2+1)] for j in range(len_str1+1)]

    for i in range(1,len_str1+1):
        s[i][0]=0
    for j in range(1,len_str2+1):
        s[0][j]=0

    for i in range(1, len_str1+1):
        for j in range(1, len_str2+1):

            if str1[i-1] == str2[j-1]:
                s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1]+1)
                if s[i][j] == s[i-1][j]:
                    backtrack[i-1][j-1] = 'u'
                elif s[i][j] == s[i][j-1]:
                    backtrack[i-1][j-1] = 'l'
                elif s[i][j] == s[i-1][j-1]+1:
                    backtrack[i-1][j-1] = 'd'
            else:
                s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1])
                if s[i][j] == s[i-1][j]:
                    backtrack[i-1][j-1] = 'u'
                elif s[i][j] == s[i][j-1]:
                    backtrack[i-1][j-1] = 'l'
                elif s[i][j] == s[i-1][j-1]:
                    backtrack[i-1][j-1] = 'd'

    return backtrack
def outputLCS(backtrack, str1, i, j):
    if i < 0 or j < 0:
        return ""
    if backtrack[i][j] == 'u':
        return outputLCS(backtrack, str1, i-1, j)
    elif backtrack[i][j] == 'l':
        return outputLCS(backtrack, str1, i, j-1)
    elif backtrack[i][j] == 'd':
        return outputLCS(backtrack, str1, i-1, j-1) + str1[i]

def LongestCommonSubsequence(str1, str2):

    backtrack = LCSbacktrack(str1,str2)

    len_str1 = len(str1) - 1
    len_str2 = len(str2) - 1

    return outputLCS(backtrack, str1, len_str1, len_str2)

if __name__ == "__main__":

    file = open('../dataSets/rosalind_ba5c.txt', 'r')

    str1 = file.readline().rstrip('\n')
    str2 = file.readline().rstrip('\n')

    print(LongestCommonSubsequence(str1, str2))
