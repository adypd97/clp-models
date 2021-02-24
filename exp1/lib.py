#!/usr/bin/env python3
'''
Shell and Tube Heat Exchanger
'''

import math
from params import *

def Q(m, c, T_in, T_out):
    return m * c * abs(T_out - T_in) 

def LMTD(T1, T2, T3, T4):
    return (T1 - T3 - T2 + T4)/ math.log(abs((T1 - T3)/(T2 - T4)))

def A(D,N,L):
    return math.pi * D * N * L

def correction_params(T_c_i, T_c_o, T_h_i, T_h_o, flag=1):
    r = round(abs((T_h_o - T_h_i)/(T_c_i - T_c_o)), 2)
    p = round(abs((T_c_o - T_c_i) / (T_h_i - T_c_i)), 2)
    if flag :
        return r
    else:
        return p

def U(m, c, T_h_in, T_h_out, T_c_in, T_c_out, D, N, L, ):
    ''' Heat Transfer Coefficient (U)'''
    # TODO: r and p are incorrect (both > 1)
    #r = correction_params(T_c_in , T_c_out,  T_h_out, T_h_in)
    #p = correction_params(T_c_in , T_c_out,  T_h_out, T_h_in, 0)
    F = 0.5 # temp fix

    return Q(m, c, T_h_in, T_h_out)/ (F * A(D, N, L)  \
            * LMTD(T_h_in, T_h_out, T_c_in, T_c_out))

def C(m, c_p):
    return m * c_p

def get_C_min(m_h, m_c, c_p):
    C_h, C_c = C(m_h, c_p), C(m_c, c_p)
    return C_h if C_h - C_c < 0 else C_c

def max_Q(m_h, m_c, T_h_in, T_c_in, c_p):
    return get_C_min(m_h, m_c, c_p) * (T_h_in - T_c_in)

def ntu_method(m_h, m_c, c_p, T_h_i, T_h_o, T_c_i, T_c_o):
    EPS = 1e-6
    C_min = get_C_min(m_h, m_c, c_p)
    C_h = C(m_h , c_p)
    C_c = C(m_c , c_p)
    if abs(C_min - C_h) < EPS:
        return abs(T_h_i - T_h_o) / (T_h_i - T_c_i)
    elif abs(C_min - C_c) < EPS:
        return abs(T_c_i - T_c_o) / (T_h_i - T_c_i)





