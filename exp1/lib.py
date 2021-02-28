#!/usr/bin/env python3
'''
Shell and Tube Heat Exchanger
'''

import math
from params import *

def Q(m, c, T_in, T_out):
    return (m * c * abs(T_out - T_in)) * 2.78e-4 

def find_T_o(m_h, m_c, T_h_i, T_c_i):
    ''' return T_o (for both streams)
        assuming that the exchanger is very long
        and Q_h = Q_c (heat exchanger is isolated)
    '''
    return (m_h * T_h_i + m_c * T_c_i) / (m_h + m_c)

def LMTD(T1, T2):
    '''
    If both liquids are same
    delta_T_m = delta_T_h = delta_T_c
    '''
    return abs(T1 - T2)

def A(D,N,L):
    return math.pi * D * N * L
    
def correction_params(T_c_i, T_c_o, T_h_i, T_h_o):
    try:
        r = round(abs((T_h_o - T_h_i)/(T_c_i - T_c_o)), 2)
        p = round(abs((T_c_o - T_c_i) / (T_h_i - T_c_i)), 2)
    except ZeroDivisionError:
        return None, None
    return r, p

'''
def get_S_for_F(r):
    return math.sqrt( r**2 + 1 ) / ( r - 1 )

def get_W_for_F(r, p):
    return ( 1 - p*r ) / ( 1 - p )

def get_Wo_for_F(p):
    return 1 - p 

def get_F(T_h_i, T_c_i, T_h_o, T_c_o):
    LINK TO EQUATIONS : https://www.wolframcloud.com/objects/demonstrations/CorrectionFactorForShellAndTubeHeatExchanger-source.nb
    r, p = correction_params(T_c_i, T_c_o, T_h_i, T_h_o)
    if r == p == None:
        return 0.5

    if r < 1:
        S = get_S_for_F(r)
        W = get_W_for_F(r, p)
        term = ( 1 + W - S + S*W ) / ( 1 + W + S - S*W )
        print(term)
        return S * math.log(W) / math.log(term)

    else:
        Wo = get_Wo_for_F(p)
        r2 = math.sqrt(2)
        return ( r2 * ( 1 - Wo ) / Wo ) / ( math.log( \
               (Wo / ( 1 - Wo) + 1 / r2) / ( Wo / ( 1 - Wo ) - 1 / r2)) )
'''


def U(m, c, T_h_i, T_c_i, T_h_o, T_c_o, D, N, L):
    ''' Heat Transfer Coefficient (U)'''
    F = 0.8 #get_F(T_h_i, T_c_i, T_h_o, T_c_o)
    return Q(m, c, T_c_i, T_c_o) / (F * A(D, N, L)  \
            * LMTD(T_h_i, T_c_i))

def C(m, c_p):
    return m * c_p

def get_C_min(m_h, m_c, c_p):
    C_h, C_c = C(m_h, c_p), C(m_c, c_p)
    return min(C_h, C_c)

def get_C_max(m_h, m_c, c_p):
    C_h, C_c = C(m_h, c_p), C(m_c, c_p)
    return max(C_h, C_c)

def max_Q(m_h, m_c, T_h_in, T_c_in, c_p):
    return get_C_min(m_h, m_c, c_p) * (T_h_in - T_c_in)

def effectiveness(m_h, m_c, c_p, T_h_i, T_h_o, T_c_i, T_c_o):
    EPS = 1e-6
    C_min = get_C_min(m_h, m_c, c_p)
    C_h = C(m_h , c_p)
    C_c = C(m_c , c_p)
    if abs(C_min - C_h) < EPS:
        return abs(T_h_i - T_h_o) / (T_h_i - T_c_i)
    elif abs(C_min - C_c) < EPS:
        return abs(T_c_i - T_c_o) / (T_h_i - T_c_i)

def c_ratio(m_h, m_c, c_p):
    return get_C_min(m_h, m_c, c_p) / get_C_max(m_h, m_c, c_p) 




