#!/usr/bin/env python3

# CONSTANTS

def compressor_work(V, I):
    phi = 0.7   # power factor
    return V * I * phi / 1000.0 # kW

def refrigeration_work(T_w_i, T_w):
    rho = 1000                              # kg/m3
    vol = 0.1                               # m3
    mass_water = (rho *  vol) / 1000.0      #kg
    C_p = 4.186                             # kJ/kgC
    time_interval = 60                      # 1min, in seconds
    assert T_w < T_w_i, 'T_w must be < T_w_i'
    return mass_water * C_p * (T_w_i - T_w) / time_interval


def exp_COP(ref_work, comp_work):
    return [ rwork / cwork for rwork, cwork in zip(ref_work, comp_work) ]

def gen_T_w(T_w_i, n):
    import random
    return [ random.gauss(T_w_i - i, 0.5) for i in range(1, n+1) ]

def gen_I(I, n):
    import random
    return [ random.gauss(2, 0.5) for _ in range(n) ]

if __name__ == "__main__":
    # generate T_w_i, T_w, V and I
    n = 10
    V = 220                     # volts
    I = gen_I(2, n)             # Ampere
    T_w_i = 25                  # C, initially temp warmer
    T_w   = gen_T_w(T_w_i, n)   # C, finally cooler after 60 seconds
    comp_work = [ compressor_work(V, i) for i in I ]
    ref_work = [ refrigeration_work(T_w_i, t_w) for t_w in T_w ]
    
    print(f'Compressor Work : {comp_work} kW')
    print(f'Refrigerator Work : {ref_work} kW')
    print(f'EXP COP : {exp_COP(ref_work, comp_work)}')
