#!/usr/bin/env python
# -*- coding: utf-8 -*-



if __name__ == "__main__":

    with open("4.txt", 'r') as f:
        mat = [[c for c in line.rstrip()] for line in f.readlines()]

    def xmas(idx):
        return (mat[idx[0][0]][idx[0][1]] == 'M' and mat[idx[1][0]][idx[1][1]] == 'S') \
                or (mat[idx[0][0]][idx[0][1]] == 'S' and mat[idx[1][0]][idx[1][1]] == 'M')

    count = 0
    # Looks like some code I could've written 10y ago
    for i in range(1,len(mat)-1):
        for j in range(1,len(mat[i])-1):
            if mat[i][j] == 'A':
                if xmas(((i-1, j-1), (i+1, j+1))) and xmas(((i-1, j+1), (i+1, j-1))):
                    count += 1

    print("X-MAS? ", count)
