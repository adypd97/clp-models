#!/usr/bin/env python3

'''
FROM LECTURE VIDEO
LPH      Celcius
F_h      T_h_i      T_h_o | F_c      T_c_i       T_c_o

75       58.2       38.6    50       19.7        39.7
         57.7       34.1             16.8        35.5
         57.7       35.6             17.0        37.0
         57.8       36.8             17.3        38.2

Repeat for different F_h/F_c and DTC
'''
# Known Parameters
L = 0.75 # meters (length of tube)
N = 23   # number of tubes
D_o = 0.016 # meters (outer diameter of tubes)
D_i = 0.013 # meters (inner diameter of tubes)
c_p = 4180 # constant (assumed), J/Kg*K
rho = 998  # water, kg/m^3


'''
Generate inlet stream temperatures, outlet stream temperatures,
and DTC 
'''
import random

def data(lb, ub, n=100, dist=random.uniform):
    return [ dist(lb, ub) for _ in range(n) ]

def gen_T_h_i(T):
    error = 0.01       # 1% error
    ub = T
    lb = T - error*T
    return data(lb, ub)

def gen_T_c_i(T):
    error = 0.01       # 1% error
    ub = T
    lb = T - error*T
    return data(lb, ub)

def gen_T_o(T_th):
    error = 0.1     # 10% error
    lb = T_th - error*T_th
    return data(lb, 10*error, dist=random.gauss)


'''
c_p = { 0.01 : 4.2199,
        10   : 4.1955,
        20   : 4.1844,
        25   : 4.1816,
        30   : 4.1801,
        40   : 4.1796,
        50   : 4.1815,
        60   : 4.1851,
        70   : 4.1902,
        80   : 4.1969,
        90   : 4.2053,
        100  : 4.2157}  # specific heat capacity of water (value)
                        # at temperature Celsius(key), units
                        # kJ/(kg K)
'''
