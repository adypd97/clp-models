#!/usr/bin/env python3

# Known Parameters
L = 0.75 # meters (length of tube)
N = 23   # number of tubes
D_o = 0.016 # meters (outer diameter of tubes)
D_i = 0.013 # meters (inner diameter of tubes)
T_h_i = [58.2, 57.7, 57.7, 57.8]
T_h_o = [38.6, 34.1, 35.6, 36.8]
T_c_i = [19.7, 16.8, 17.0, 17.3]
T_c_o = [39.7, 35.5, 37.0, 38.2]

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
c_p = 4.18 # constant (assumed), kJ/Kg*K

m_h = 75  # flow rate for hot water
m_c = 50  # flow rate for cold water
