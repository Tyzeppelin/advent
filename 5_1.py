#!/usr/bin/env python
# -*- coding: utf-8 -*-




if __name__ == "__main__":

    with open("5.txt", 'r') as f:
        rules = [lines.rstrip() for lines in iter(f.readline, "\n")]
        #print(ordered_pages)
        jobs = [lines.rstrip() for lines in f.readlines()]
        #print(printing_jobs)

    print("rules -> ", len(rules))
    print("jobs -> ", len(jobs))
   
    valids = 0

    for j in jobs:
        pages = j.split(',')
        for i in range(len(pages[:-1])):
            if pages[i] + "|" + pages[i+1] not in rules:
                break
        else:
            #print("OK", pages[len(pages)//2], len(pages)%2)
            valids += int(pages[len(pages)//2])

    print("valid jobs -> ", valids)
