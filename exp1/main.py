#!/usr/bin/env python3

from lib import U, ntu_method, correction_params
from params import T_h_i, T_h_o, T_c_i , T_c_o, D_o, N, L, m_h, m_c, c_p
import math

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
    for i in range(4):
        print('p ' + str(correction_params(T_c_i[i], T_c_o[i], T_h_i[i], T_h_o[i],0)))
        print('r ' + str(correction_params(T_c_i[i], T_c_o[i], T_h_i[i], T_h_o[i],1)))



if __name__ == "__main__":
    test_main()


    

