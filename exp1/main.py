#!/usr/bin/env python3

from lib import U, effectiveness, correction_params, find_T_o
from params import T_h_i, T_h_o, T_c_i , T_c_o, D_o, N, L, m_h, m_c, c_p

def test_th_values():
    T_o = list(map(lambda x, y: find_T_o(m_h, m_c, x, y), T_h_i, T_c_i))
    _U  = list(map(lambda x, y, z: U(m_h, c_p, x, y, z, y, D_o, N, L), T_h_i, T_o, T_c_i))
    _e  = list(map(lambda x, y, z: effectiveness(m_h, m_c, c_p, x, y, z, y), T_h_i, T_o, T_c_i))
    print(_U)
    print(_e)

if __name__ == "__main__":
    test_th_values()
