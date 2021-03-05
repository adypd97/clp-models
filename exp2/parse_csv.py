#!/usr/bin/env python3

import csv

sz = 0
with open('R134a_PresSat.csv') as cf:
    reader = csv.reader(cf, delimiter=',')
    values = []
    for i,row in enumerate(reader):
        
        if i < 2 :
            continue
        elif i == 2:
            params = list(map(lambda word: word.strip(), row))[:-1]
            PresStat = {key : [] for key in params}
            continue
        elif row[0] == '':
            continue
        #sz += 1
        values.append(list(map(lambda val: float(val), row[:-1])))


def col_to_row(l, i, size):
    return [l[j][i] for j in range(size)]

def transpose(l):
    return [col_to_row(l, i, len(l)) for i in range(len(l[0]))]
    
values = transpose(values)
for i, key in enumerate(PresStat.keys()):
    PresStat[key] = values[i]


