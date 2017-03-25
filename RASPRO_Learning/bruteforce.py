#!/usr/bin/python
import csv
import numpy as np

hamming_array = []

def hamming_distance(chr1, chr2):
    n1 = len(chr1)
    n2 = len(chr2)

    if (n1 != n2):
        diffs = len(chr1)- len(chr2)
        return abs(diffs)
    else:
        i = 0
        k = 0
        while( i < n1):
            if(chr1[i] != chr2[i]):
                k = k + 1
            i = i + 1
        return k


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
                j = j  + 1
            i = i + 1
        hamming_array.append(add)
    k = k + 1
    cm = np.argmin(hamming_array,0)
    print data[cm]


with open('data.csv','rb') as csvfile:
    data = list(csv.reader(csvfile, delimiter=","))
    data = np.array(data[0:])
    value = list((np.shape(data)))
    hloop(data, value)
