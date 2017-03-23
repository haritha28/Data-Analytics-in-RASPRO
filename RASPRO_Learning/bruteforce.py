#!/usr/bin/python
import csv
import numpy as np

# int hamming_array[]

def hamming_distance(chr1, chr2):
    diffs = len(chr1)- len(chr2)
    #print diffs
    return abs(diffs)

def hloop(data,value):
    add = 0
    i = 0
    j = 0
    k = 0
    for k in range(value[0]):
        i = 0
        add = 0
        for i in range(value[0]):
            j = 0
            for j in range(value[1]):
                trial = hamming_distance(data[k][j], data[i][j])
                add = add + trial
                #print add
                j = j  + 1
            i = i + 1
        print add
    k = k + 1



with open('data.csv','rb') as csvfile:
    # reader1 = csv.reader(csvfile, delimiter=",")
    # no_cols = len(reader1.next())
    data = list(csv.reader(csvfile, delimiter=","))
    #no_rows = len(reader2)
    data = np.array(data[0:])
    value = list((np.shape(data)))
    #no_rows = value[0]
    #no_columns = value[1]
    hloop(data, value)
    # print np.apply_along_axis(hloop, 0, data)
