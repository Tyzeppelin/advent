#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import operator
import time


def day_one():
    dial = 50
    password_1 = 0
    password_2 = 0
    with open("day_one_part_1.txt", 'r') as f:
        for instr in [l.rstrip() for l in f.readlines()]:
            op = operator.sub if instr[0] == "L" else operator.add 
            div, dial = divmod(op(dial, int(instr[1:])), 100)
            if dial == 0:
                password_1 += 1
            if div != 0:
                password_2 += abs(div)

    return password_1, password_2


def _npeat(n, l):
    return sum([10**x for x in range(0, l*n, l)])


def sum_npeat(a, b, n=2):
    assert math.floor(math.log10(a)) == math.floor(math.log10(b)), f"a:{a} and b:{b} must be the same size"
    l_a = math.floor(math.log10(a)) + 1
    npeat_factor = _npeat(n, l_a)
    # We can do better
    # return sum([p * npeat_factor for p in range(a, b+1)])
    # We did better !
    return npeat_factor * (b - a + 1) * (a + b) / 2
    

#def _8peat(n):
#    return (10**n-1)*8/9

def day_two():
    # plan:
    part_1 = 0

    with open("day_two.txt", 'r') as f:
        for l, u in [r.split("-") for r in f.read().rstrip().split(",")]:
            low = int(l)
            up = int(u)
            l_low = len(l)
            l_up = len(u)
            low_bound = math.ceil(l_low / 2)
            up_bound = l_up // 2 + 1
            # Part 1: we get the range of the size of the len 
            for q in range(low_bound, up_bound, 1):
                # min
                a = 10 ** (q-1) if 2*q != l_low else int(l[:q]) if int(l[:q]) >= int(l[q:]) else int(l[:q]) + 1
                # max
                b = 10 ** (q) - 1 if 2*q != l_up else int(u[:q]) if int(u[:q]) <= int(u[q:]) else int(u[:q]) - 1
                s2 = sum_npeat(a, b, 2)
                part_1 += s2

    return part_1, "NOT YET"


if __name__ == "__main__":

    t1 = time.time()

    print("Day One - part 1 & 2")
    print("=>", day_one())
    print("********************")
    print("Day Two - part 1")
    print("=>", day_two())
    print("********************")

    print("done under", time.time() - t1, "seconds")
