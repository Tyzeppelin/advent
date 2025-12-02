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


if __name__ == "__main__":

    t1 = time.time()

    print("Day one - part 1")
    print("=>", day_one())

    print("done under", time.time() - t1, "seconds")
