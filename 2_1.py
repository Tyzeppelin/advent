#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator

if __name__ == "__main__":

    def is_safe(n: list[int]):
        ord = operator.ge if n[0] < n[1] else operator.le
        prev = n[0]
        errors = 0
        for e in n[1:]:
            if ord(prev, e) or abs(e-prev) > 3 or abs(e-prev) < 1:
                errors += 1
                if errors > 0:
                    return 0
                continue
            prev = e
        #print("valide ->", n)
        return 1


    with open("2.txt", 'r') as f:
        lines = [[int(e) for e in l.rstrip().split(" ")] for l in f.readlines()]
        #diffs = [i-j for i, j in zip(lines[:-1], lines[1:])]
        #print(lines) 
        print(sum([is_safe(l) for l in lines]))


