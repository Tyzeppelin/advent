#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

if __name__ == "__main__":
    with open("1.txt", 'r') as f:
        lines = [(l.rstrip().split("   ")) for l in f.readlines()]
        l = set()
        r = defaultdict(lambda: 0)
        for lv, rv in lines:
            l.add(int(lv))
            r[int(rv)] += 1
        s = sum([k*v for k,v in r.items() if k in l])
        print(s)
