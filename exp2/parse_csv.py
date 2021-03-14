#!/usr/bin/env python3

import csv
from pprint import pprint as pp

DIR_PATH = "./input/"
TEMPFILE = DIR_PATH + 'R134a_TempSat.csv'
PRESFILE = DIR_PATH + 'R134a_PresSat.csv'
SUPERFILE = DIR_PATH +  'R134a_Super.csv'

def transpose(l):
    return [[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]
        
def table(filename):
    '''Construct a lookup table from csv file

    Input: filename
    Output: Lookup table 'd'
    '''
    with open(filename) as cf:
        reader = csv.reader(cf, delimiter=',')
        values = []
        for i,row in enumerate(reader):
            if i < 2 :
                continue
            elif i == 2:
                params = list(map(lambda word: word.strip(), row))[:-1]
                d = {key : [] for key in params}
                continue
            elif row[0] == '' or row == None:
                continue
            values.append(list(map(lambda val: float(val), row[:-1])))
    values = transpose(values)
    for i, key in enumerate(d.keys()):
        d[key] = values[i]

    return d

def show_table(d):
    for k,v in d.items():
        print("Key", k)
        print("Value", v)
        print("-----")

# R134a : Critical Pressure: 4.059 MPa, Critical Temperature 101.06°C
if __name__ == "__main__":
    temp = table(TEMPFILE)
    pres = table(PRESFILE)
    show_table(temp)
