#!/usr/bin/env python3

from lib import U, effectiveness, correction_params, find_T_o
from params import T_h_i, T_c_i , D_o, N, L, m_h, m_c, c_p, DTC, CWT, gen_T_o
import matplotlib.pyplot as plt

def run():
    T_th = find_T_o(m_h, m_c, DTC, CWT)   # theoretical outlet temperatures
    T_h_o = gen_T_o(T_th)
    T_c_o = gen_T_o(T_th)
    _U  = list(map(lambda w, x, y, z: U(m_c, c_p, w, x, y, z, D_o, N, L), T_h_i, T_c_i, T_h_o, T_c_o))
    _e  = list(map(lambda w, x, y, z: effectiveness(m_h, m_c, c_p, w, x, y, z), T_h_i, T_h_o, T_c_i, T_c_o))
    print(_U)
    print(_e)

def show(x, y, title='Overall Heat Transfer Coeff', xlabel='time', ylabel='U'):
    x = [ i for i in range(0,100) ]
    plt.title(title)
    #plt.legend('DTC, CWT, m_h, m_c')
    plt.xlabel(xlabel)
    plt.ylable(ylabel)
    plt.grid(True)
    plt.hold(True)
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    run()
