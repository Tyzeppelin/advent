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
   

    def sort(arr_in):
        arr = arr_in[:]

        for i in range(len(arr)-1, 0, -1):
            cut = True
            for j in range(i):
                if arr[j+1] +"|"+ arr[j] in rules:
                    _temp = arr[j+1]
                    arr[j+1] = arr[j]
                    arr[j] = _temp
                    cut = False
            if cut:
                return arr
        return arr

    valids = 0

    for j in jobs:
        pages = j.split(',')
        for i in range(len(pages[:-1])):
            if pages[i] + "|" + pages[i+1] not in rules:
                sorted_pages = sort(pages)
                print(pages, sorted_pages, sorted_pages[len(pages)//2])
                valids += int(sorted_pages[len(pages)//2])
                break

    print("valid jobs -> ", valids)
