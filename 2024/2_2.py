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

    def is_safe_w_errors(n: list[int]):
        for d in range(len(n)):
            n_trunc = n[0:d]+n[d+1:len(n)]

            ord = operator.ge if n_trunc[0] < n_trunc[1] else operator.le
            prev = n_trunc[0]
            errors = 0
            start_idx = 0
            for e in n_trunc[1:]:
                if ord(prev, e) or abs(e-prev) > 3 or abs(e-prev) < 1:
                    errors += 1
                    break
                prev = e
            if errors == 0:
                return 1
        return 0

    with open("2.txt", 'r') as f:
        lines = [[int(e) for e in l.rstrip().split(" ")] for l in f.readlines()]

        nominal = sum([is_safe(l) for l in lines])
        print("nominal: ",nominal)
        tolerated = sum([is_safe_w_errors(l) for l in lines])
        print("tolerated: ", tolerated)

