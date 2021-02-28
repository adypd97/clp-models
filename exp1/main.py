#!/usr/bin/env python3

from lib import U, effectiveness, correction_params, find_T_o
from params import  D_o, N, L, c_p, gen_T_o, gen_T_c_i, gen_T_h_i
import matplotlib.pyplot as plt
#from scipy.interpolate import make_interp_spline

def show(x, y, title='Avg Overall Heat Transfer Coeff of Exchanger vs DTC', xlabel='DTC', ylabel='Avg U', saveas='UvsDTC.png'):
    plt.title(title)
    plt.figure(figsize=(16,8))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.plot(x, y)
    plt.legend(['x axis: DTC [CWT+1, 90] degree celcius'])
    plt.savefig(saveas)
    plt.show()

def run(T, T_h_i, T_c_i, T_h_o, T_c_o, dtc, flag=1):
    _U  = list(map(lambda w, x, y, z: U(m_c, c_p, w, x, y, z, D_o, N, L), T_h_i, T_c_i, T_h_o, T_c_o))
    _e  = list(map(lambda w, x, y, z: effectiveness(m_h, m_c, c_p, w, x, y, z), T_h_i, T_h_o, T_c_i, T_c_o))
    #print("DTC: {0} , AVERAGE U: {1:.2f}".format(dtc, sum(_U) / len(_U)))
    #print("DTC: {0} , AVERAGE e: {1:.2f}".format(dtc, sum(_e) / len(_e)))
    if flag:
        return sum(_U) / len(_U)
    else:
        return sum(_e) / len(_e)


def main(DTC):
    # theoretical outlet temperatures
    avg_U = list()
    avg_e = list()
    for dtc in DTC:
        T_th = find_T_o(m_h, m_c, dtc, CWT)
        T_h_i = gen_T_h_i(dtc)
        T_c_i = gen_T_c_i(CWT)
        T_h_o = gen_T_o(T_th)
        T_c_o = gen_T_o(T_th)
        avg_U.append(run(T_th, T_h_i, T_c_i, T_h_o, T_c_o, dtc))
        avg_e.append(run(T_th, T_h_i, T_c_i, T_h_o, T_c_o, dtc, flag=0))
    show(DTC, avg_U)
    show(DTC, avg_e, title='Avg Effectiveness of Exchanger vs DTC', ylabel='Avg e', saveas='evsDTC.png')


if __name__ == "__main__":
    # Variables (Control) Parameters
    CWT = 20    # cold water temperature (inlet)
    DTC = [ i for i in range(90, CWT, -1) ]     # hot water temperature (inlet)
    m_h = 75   # flow rate for hot water  (kg/s) (check TODO)
    m_c = 50   # flow rate for cold water (kg/s) (check TODO)
    main(DTC)
