#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import operator
import time

_primes = [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 41, 43, 47]

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
    """
    n -> how many time
    l -> length of the number
    """
    return sum([10**x for x in range(0, l*n, l)])


def sum_npeat(a, b, n=2):
    assert math.floor(math.log10(a)) == math.floor(math.log10(b)), f"a:{a} and b:{b} must be the same size"
    l_a = math.floor(math.log10(a)) + 1
    npeat_factor = _npeat(n, l_a)
    # We can do better
    # return sum([p * npeat_factor for p in range(a, b+1)])
    # We did better !
    return npeat_factor * (b - a + 1) * (a + b) / 2
    

def set_npeat(a, b, n=2):
    assert math.floor(math.log10(a)) == math.floor(math.log10(b)), f"a:{a} and b:{b} must be the same size"
    l_a = math.floor(math.log10(a)) + 1
    npeat_factor = _npeat(n, l_a)
    return {npeat_factor * m for m in range(a, b+1)}

def rect_range(i, j, sz):
    # min
    a = int(i) if len(i) == sz else 10**(sz-1)
    # max
    b = int(j) if len(j) == sz else 10**sz - 1
    return a,b


def day_two():
    # plan:
    part_1 = 0
    part_2 = 0
    with open("day_two.txt", 'r') as f:
        for l, u in [r.split("-") for r in f.read().rstrip().split(",")]:
            low = int(l)
            up = int(u)
            l_low = len(l)
            l_up = len(u)
            low_bound = math.ceil(l_low / 2)
            up_bound = l_up // 2 + 1
            part1_range = list(range(low_bound, up_bound, 1))
            # Part 1: we get the range of the size of the len 
            # Part 2: we use a set because I am not smart enough
            invalid_set = set()
            print("$", low, up)
            for sz in range(l_low, l_up+1):
                #print("------------------", sz)
                l_adj = low  if low >= 10**(sz-1) else 10**(sz-1)
                l_adj_str = str(l_adj)
                u_adj = up if up <= 10**sz-1 else 10**sz-1
                u_adj_str = str(u_adj)
                # size of 1 <- auto in
                invalid_set |= {int("1"*sz)}
                print(sz, [1] + [e for e in range(1, up_bound, 1) if e in _primes and sz % e == 0])
                #print(l_adj, u_adj)
                for q in [1] + [e for e in range(1, up_bound, 1) if e in _primes and sz % e == 0]:
                    #print("q:", q, invalid_set)
                    # min
                    a = int(l_adj_str[:q]) if int(l_adj_str[:q] * (sz//q)) >= int(l_adj) else int(l_adj_str[:q]) + 1
                    # max
                    b = int(u_adj_str[:q]) if int(u_adj_str[:q] * (sz//q)) <= int(u_adj) else int(u_adj_str[:q]) - 1
                    print("=", l, u, a, b, sz, q)
                    if sz / q == 2.0:
                        s2 = sum_npeat(a, b, 2)
                        print(low, up, sz, q, l_adj, u_adj, a, b, s2, sorted(set_npeat(a, b)), sum(set_npeat(a, b)))
                        part_1 += s2
                    invalid_set = invalid_set 
            #print(l, u, sorted(invalid_set))
            else:
                print("=======================")

    print("Is part1 correct?", part_1 == 32976912643, 32976912643)

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
