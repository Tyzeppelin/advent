#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":

    with open("6.txt", 'r') as f:
        guard_map = [[c for c in line] for line in f.readlines()]


    guard_location = (0,0)
    cut = False
    for i in range(len(guard_map)):
        for j in range(len(guard_map[i])):
            if guard_map[i][j] in "^":
                guard_location = (i,j)
                cut = True
                break
        if cut:
            break

    out = False
    direction = "N"

    i,j = guard_location
    while not out:
        guard_map[i][j] = "X"
        if direction == "N": # i-1
            if i-1 < 0:
                break
            elif guard_map[i-1][j] == "#":
                direction = "E"
                j += 1
            else:
                i -= 1
        elif direction == "E": # j+1
            if j+1 >= len(guard_map[i]):
                break
            elif guard_map[i][j+1] == "#":
                direction = "S"
                i += 1
            else:
                j += 1
        elif direction == "S": # i+1
            if i+1 >= len(guard_map):
                break
            elif guard_map[i+1][j] == "#":
                direction = "W"
                j -= 1
            else:
                i += 1
        elif direction == "W": # j-1
            if j-1 < 0:
                break
            elif guard_map[i][j-1] == "#":
                direction = "N"
                i -= 1
            else:
                j -= 1
        else:
            print("not happening")
            break

 
    print(len(guard_map)*len(guard_map[0]))
    path_size = sum([sum([1 if c == 'X' else 0 for c in line]) for line in guard_map])
    print("Guard has walked", path_size, "squares")
