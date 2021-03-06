#!/usr/bin/env python3

from lib import U, effectiveness, correction_params, find_T_o
from params import  D_o, N, L, c_p, gen_T_o, gen_T_c_i, gen_T_h_i
import matplotlib.pyplot as plt
#from scipy.interpolate import make_interp_spline

def show(x, y, title='Avg Overall Heat Transfer Coeff of Exchanger vs DTC', xlabel='DTC', ylabel='Avg U', saveas='UvsDTC.png'):
    plt.figure(figsize=(16,8))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.plot(x, y)
    plt.legend(['x axis: Cold Fluid Flow rate (LPH)'])
    plt.title(title)
    plt.savefig('./results/' + saveas)
    plt.show()

def output(dtc, _U, _e, T_h_i, T_h_o, T_c_o, T_c_i):
    print("DTC: {0} , AVERAGE U: {1:.2f}".format(dtc, sum(_U) / len(_U)))
    print("========")
    print("DTC: {0} , AVERAGE e: {1:.2f}".format(dtc, sum(_e) / len(_e)))
    print("No.  T_h_i    T_h_o   T_c_i   T_c_o")
    for i in range(len(T_h_i)):
        print("{0:3d}   {1:.2f}    {2:.2f}   {3:.2f}   {4:.2f}".format(i, T_h_i[i], T_h_o[i], T_c_i[i], T_c_o[i]))

def run(T, T_h_i, T_c_i, T_h_o, T_c_o, dtc, m=0, flag=1):
    _U  = list(map(lambda w, x, y, z: U(m, c_p, w, x, y, z, D_o, N, L), T_h_i, T_c_i, T_h_o, T_c_o))
    _e  = list(map(lambda w, x, y, z: effectiveness(m_h, m, c_p, w, x, y, z), T_h_i, T_h_o, T_c_i, T_c_o))
    output(dtc, _U, _e, T_h_i, T_h_o, T_c_o, T_c_i)
    if flag:
        return sum(_U) / len(_U)
    else:
        return sum(_e) / len(_e)


def main(DTC, m_c):
    # theoretical outlet temperatures
    avg_U = list()
    avg_e = list()
    dtc = DTC
    for m in m_c:
        T_th = find_T_o(m_h, m, dtc, CWT)
        T_h_i = gen_T_h_i(dtc)
        T_c_i = gen_T_c_i(CWT)
        T_h_o = gen_T_o(T_th)
        T_c_o = gen_T_o(T_th)
        avg_U.append(run(T_th, T_h_i, T_c_i, T_h_o, T_c_o, dtc, m))
        avg_e.append(run(T_th, T_h_i, T_c_i, T_h_o, T_c_o, dtc, m, flag=0))
    show(m_c, avg_U, title='Avg Overall Heat Transfer Coeff vs Cold Fluid Flow rate (DTC=60C)', xlabel='m_c(LPH)', saveas='Uvsm_c.png')
    show(m_c, avg_e, title='Avg Effectiveness of Exchanger vs Cold Fluid Flow rate (DTC=60C)', xlabel='m_c (LPH)', ylabel='Avg e', saveas='evsm_c.png')


if __name__ == "__main__":
    # Variables (Control) Parameters
    CWT = 20    # cold water temperature (inlet)
    #DTC = [ i for i in range(90, CWT, -1) ]     # hot water temperature (inlet)
    DTC = 60
    m_h = 75
    #m_h = [ i for i in range(75, 0, -1) ] #75   # flow rate for hot water  (kg/s) (check TODO)
    #m_c = 50   # flow rate for cold water (kg/s) (check TODO)
    m_c = [ i for i in range(1, 75, 1) ] #75   # flow rate for hot water  (kg/s) (check TODO)
    main(DTC, m_c)
