#!/usr/bin/python
import csv
import numpy as np

#int hamming_array[]

# def haming_distance():

with open('data.csv','rb') as csvfile:
    data = list(csv.reader(csvfile, delimiter=","))
    data = np.array(data[0:])
    print(data[2,3])
    # haming_distance()
