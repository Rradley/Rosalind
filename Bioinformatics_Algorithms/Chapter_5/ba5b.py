# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:48:33 2021

@author: rob
"""

def ReadFile (fileName):    
    with open(fileName, "r") as file:
        matrix = file.readline().split()
        n = int(matrix[0])
        m = int(matrix[1])

        down = []
        right = []
        direction = down
        for line in file:
            row = line.strip()
            if row == '-':
                direction = right
                continue
            l = row.split(' ')
            direction.append(l)
        return n,m,down,right

def ManhattanTourist(n,m,down,right):
    s = []
    for i in range(n + 1):
        l = []
        for j in range(m + 1):
            l.append(0)
        s.append(l)
    
    for i in range(1,n + 1):
        s[i][0] = s[i-1][0] + int(down[i][0])
    for j in range (1,m + 1):
        s[i][0] = s[i-1][0] + int(right[i][0])
    for i in range (1,n + 1):
        for j in range (1,m + 1):
            s[i][j] = max(s[i-1][j] + int(down[i][j]), s[i][j-1] + int(right[i][j]))
    return s[n][m]


if __name__ == "__main__":
    fileName = '../dataSets/rosalind_ba5b.txt'
    n,m,down,right = ReadFile(fileName)
    print(ManhattanTourist(n, m, down, right))
            