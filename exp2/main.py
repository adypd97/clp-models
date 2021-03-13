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
    time_interval = 60                      # seconds
    assert T_w < T_w_i, 'T_w must be < T_w_i'
    return mass_water * C_p * (T_w_i - T_w) / time_interval


def exp_COP(ref_work, comp_work):
    return ref_work / comp_work

if __name__ == "__main__":
    # generate T_w_i, T_w, V and I
    V = 220     # volts
    I = 2.2     # A
    T_w_i = 25  # C
    T_w   = 22  # C
    comp_work = compressor_work(V, I)
    ref_work = refrigeration_work(T_w_i, T_w)
    

    print(f'{comp_work} kW')
    print(f'{ref_work} kW')
    print(f'EXP COP : {exp_COP(ref_work, comp_work)}')
