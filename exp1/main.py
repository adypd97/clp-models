#!/usr/bin/env python3

from lib import *
from params import *
import math

'''
LPH      Celcius
F_h      T_h_i      T_h_o | F_c      T_c_i       T_c_o

75       58.2       38.6    50       19.7        39.7
         57.7       34.1             16.8        35.5
         57.7       35.6             17.0        37.0
         57.8       36.8             17.3        38.2

Repeat for different F_h/F_c and DTC
'''

def test_U():
    res_u = list()
    for i in range(4):
        res_u.append(U(m_h, c_p, T_h_i[i], T_h_o[i], T_c_i[i], T_c_o[i], D_o, N, L))
    return res_u


def test_ntu_method():
    res_e = list()
    for i in range(4):
        res_e.append(ntu_method(m_h, m_c, c_p, T_h_i[i], T_h_o[i], T_c_i[i], T_c_o[i]))
    return res_e


def test_main():
    u = test_U()
    e = test_ntu_method()
    print(f'U : {u}')
    print(f'Effectivness : {e}')


if __name__ == "__main__":
    test_main()


    

