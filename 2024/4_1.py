#!/usr/bin/env python
# -*- coding: utf-8 -*-



if __name__ == "__main__":

    with open("4.txt", 'r') as f:
        mat = [[c for c in line.rstrip()] for line in f.readlines()]

    def xmas(idx):
        return mat[idx[0][0]][idx[0][1]] == "M" and mat[idx[1][0]][idx[1][1]] == "A" and mat[idx[2][0]][idx[2][1]] == "S"

    count = 0
    # Looks like some code I could've written 10y ago
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 'X':

                if j < len(mat[i])-3 and xmas(((i, j+1), (i, j+2), (i, j+3))):
                    count += 1
                if j > 2 and xmas(((i, j-1), (i, j-2), (i, j-3))):
                    count += 1
                if i < len(mat)-3 and xmas(((i+1, j), (i+2, j), (i+3, j))):
                    count += 1
                if i > 2 and xmas(((i-1, j), (i-2, j), (i-3, j))):
                    count += 1
                if i < len(mat)-3 and j < len(mat[i])-3 and xmas(((i+1, j+1), (i+2, j+2), (i+3, j+3))):
                    count +=1
                if i < len(mat)-3 and j > 2 and xmas(((i+1, j-1), (i+2, j-2), (i+3, j-3))):
                    count += 1
                if i > 2 and j > 2 and xmas(((i-1, j-1), (i-2, j-2), (i-3, j-3))):
                    count += 1
                if i > 2 and j < len(mat[i])-3 and xmas(((i-1, j+1), (i-2, j+2), (i-3, j+3))):
                    count += 1

    print("XMAS? ", count)
