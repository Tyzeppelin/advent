#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


if __name__ == "__main__":
    
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))"

    with open("3.txt", 'r') as f:
        raw_instrs = f.read()

    instrs = re.findall(pattern, raw_instrs)

    sum = 0
    enabled = True
    for instr in instrs:
        if "do()" in instr:
            enabled = True
        elif "don't()" in instr:
            enabled = False
        elif enabled:
            sum += int(instr[1]) * int(instr[2])

    print("enabled mul -> ", sum)
