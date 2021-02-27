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


# Variables (Control) Parameters
DTC = 60    # hot water temperature (inlet)
CWT = 20    # cold water temperature (inlet)
m_h = 75   # flow rate for hot water  (kg/s) (check TODO)
m_c = 50   # flow rate for cold water (kg/s) (check TODO)

'''
Generate inlet stream temperatures, outlet stream temperatures,
and DTC 
'''
import random

def data(avg, std, n=100):
    ''' 
    TODO: Is this reasonable?
    Data generation function based
    on Gaussian Probability Distribution
    '''
    return [ random.gauss(avg, std) for i in range(n) ]

def gen_T_h_i(T):
    error = 1       # 1% error
    return data(T, error)

def gen_T_c_i(T):
    error = 1       # 1% error
    return data(T, error)

def gen_T_o(T_th):
    error = 20     # 10% error
    return data(T_th, error)

T_h_i = gen_T_h_i(DTC) # TODO : automate
T_c_i = gen_T_c_i(CWT)

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
