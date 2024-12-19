#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


if __name__ == "__main__":
    
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    with open("3.txt", 'r') as f:
        instrs = f.read()

    for p in re.finditer(pattern, instrs):
        print(p)

    print("result: ", sum([int(x)*int(y) for x,y in re.findall(pattern, instrs)]))
