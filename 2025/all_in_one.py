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
            print(instr, div, dial)
            if dial == 0:
                password_1 += 1
            if div != 0:
                password_2 += abs(div)
                print("\tpassword_2", password_2)

    return password_1, password_2

def day_two():
    # plan:
    # log10(up) => size repeatable = log10 / 2
    # up[:rep] - low[:rep]
    with open("day_two.txt", 'r') as f:
        for low, up in [r.split("-") for r in f.read().rstrip().split(",")]:
            #print(up - low, "\t", low, up,)
            rep_size = int(math.log10(int(low))) + 1 # need to account for the decimal part
            res = int(up[:rep_size]) - int(low[:rep_size])
            print(res)
    return "NOT YET"


if __name__ == "__main__":

    t1 = time.time()

    print("Day One - part 1 & 2")
    print("=>", day_one())
    print("********************")
    print("Day Two - part 1")
    print("=>", day_two())
    print("********************")

    print("done under", time.time() - t1, "seconds")
