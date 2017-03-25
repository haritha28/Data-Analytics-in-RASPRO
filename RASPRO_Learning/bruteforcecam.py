#!/usr/bin/python
import csv
import numpy as np

hamming_array = []

def cam_distance(chr1, chr2):
    n1 = len(chr1)
    n2 = len(chr2)
    diff = abs(n1 - n2)
    return diff

def camloop(data, value):
    normal_value = 'A'
    add = 0
    i = 0
    j = 0
    for i in range(value[0]):
        j = 0
        add = 0
        for j in range(value[1]):
            trial = cam_distance(data[i][j], normal_value)
            add = add + trial
            j = j  + 1
        hamming_array.append(add)
        i = i + 1
    print np.argmin(hamming_array,0)


with open('data.csv','rb') as csvfile:
    data = list(csv.reader(csvfile, delimiter=","))
    data = np.array(data[0:])
    value = list((np.shape(data)))
    camloop(data, value)
