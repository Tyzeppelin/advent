#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    with open("1.txt", 'r') as f:
        lines = [l.rstrip() for l in f.readlines()]
        l = sorted([int(n.rstrip().split("   ")[0]) for n in lines])
        r = sorted([int(n.rstrip().split("   ")[1]) for n in lines])
        s = sum([abs(a-b) for a,b in zip(l, r)])
        print(s)
