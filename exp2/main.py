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
    STD = 0.5 # arbitrary
    return [ random.gauss(T_w_i - i, STD) for i in range(1, n+1) ]

def gen_I(I, n):
    import random
    STD = 0.1 # arbitrary
    MEAN_CURRENT = 2  # reasonable
    return [ random.gauss(MEAN_CURRENT, STD) for _ in range(n) ]

def show_plot(x, y):
    import  matplotlib.pyplot as plt
    plt.scatter(x, y)
    plt.xlabel('Degree of Cooling (in Centigrade)')
    plt.ylabel('Experimental COP')
    plt.title('Exp COP vs Degree of Cooling for r134a')
    plt.savefig('results/expCOPvscooling.png')
    plt.show()

def sim_exp_COP(T_w_i):
    # generate T_w_i, T_w, V and I
    n = 10                      # number of observations 
    V = 220                     # volts
    I = gen_I(2, n)             # Ampere
    T_w_i = T_w_i                  # C, initially temp warmer
    T_w   = gen_T_w(T_w_i, n)   # C, finally cooler after 60 seconds
    cooling = [ T_w_i - t_w for t_w in T_w ]
    comp_work = [ compressor_work(V, i) for i in I ]
    ref_work = [ refrigeration_work(T_w_i, t_w) for t_w in T_w ]
    expCOP = exp_COP(ref_work, comp_work)

        
    print(f'T_w_i (initial temperature of water) = {T_w_i:.2f}')
    print(f'Voltage = 220 V')
    title = f'I\tT_w\tT_w_i - T_w\tCompressor Work (kW)\tRefrigerator Work (kW)\tExp COP' 
    print("-"*( len(title) + 5*4))
    print(title)
    print("-"*(len(title) + 5*4))
    for i in range(n):
        print(f'{I[i]:4.2f}\t{T_w[i]:5.2f}\t{(T_w_i - T_w[i]):5.2f}\t\t{comp_work[i]:5.2f}\t\t\t{ref_work[i]:5.2f}\t\t\t{expCOP[i]:5.4f}')



    #print(f'Compressor Work : {comp_work} kW')
    #print(f'Refrigerator Work : {ref_work} kW')
    #print(f'Cooling : {cooling} kW')
    #print(f'EXP COP : {exp_COP(ref_work, comp_work)}')
    show_plot(cooling, expCOP)

if __name__ == "__main__":
    sim_exp_COP(40)
