#!/usr/bin/env python3 

def gen_P1(pi ,n):
    m = 0.008     # as per sample report
    return [ round(pi - m*i, 4) for i in range(n) ]

def gen_P(pi, n):
    ''' all hacked together '''
    MULT_FACTOR = 4.2
    p1 = gen_P1(pi, n)
    return p1, [ round(MULT_FACTOR * p, 4) for p in p1 ] 

def gen_T1(ti, n):
    ''' all hacked together'''
    m = 0.65
    return [ ti - m * i for i in range(n) ]

def gen_T2(ti, n):
    t1 = gen_T1(ti, n)
    K  = 40  # arbitrary
    return [ ti + K + 0.01*K*i for i in range(n) ]

def gen_T3(ti, n):
    t1 = gen_T1(ti, n)
    K = 20 # aribitrary
    return [ t1[0] + K + 0.001*t1[0]*i for i in range(n) ]

def gen_T4(ti, n):
    t1 = gen_T1(ti, n)
    K = 10 # arbitrary
    return [ round(t - K,4) for t in t1 ]


def th_COP(t0, t2):
    '''
    t0 -> temp of r134a at compressor inlet
    t2 -> temp of r134a at expansion inlet
    '''
    import CoolProp
    from CoolProp.Plots import PropertyPlot
    from CoolProp.Plots import SimpleCompressionCycle
    pp = PropertyPlot('HEOS::R134a', 'PH', unit_system='EUR')
    pp.calc_isolines(CoolProp.iQ, num=11)
    cycle = SimpleCompressionCycle('HEOS::R134a', 'PH', unit_system='EUR')
    T0 = 273 + t0 
    pp.state.update(CoolProp.QT_INPUTS,0.0,T0-10)
    p0 = pp.state.keyed_output(CoolProp.iP)
    T2 = 273 + t2
    pp.state.update(CoolProp.QT_INPUTS,1.0,T2+15)
    p2 = pp.state.keyed_output(CoolProp.iP)
    #pp.calc_isolines(CoolProp.iT, [T0-273.15,T2-273.15], num=2)
    cycle.simple_solve(T0, p0, T2, p2, 0.7, SI=True)
    cycle.steps = 50
    sc = cycle.get_state_changes() # all state values in this
    return cycle.COP_cooling()

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

def sim_exp_COP(T_w_i, n):
    # generate T_w_i, T_w, V and I
    n = n                      # number of observations 
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

    #show_plot(cooling, expCOP)
    return expCOP, T_w, I


if __name__ == "__main__":
    T_w_i = 40
    T_r_i = 28
    pi = 5     # MPa
    n = 40
    V = 220
    expCOP, T6, I = sim_exp_COP(T_w_i, n)
    P1, P2 = gen_P(pi, n)
    T1 = gen_T1(T_r_i,n)
    T2 = gen_T2(T_r_i, n)
    T3 = gen_T3(T_r_i, n)
    T4 = gen_T4(T_r_i, n)
    
    title_1 = f'P1\tP2\tT1\tT2\tT3\tT4\tT6\t  V  \tI'
    print("-"*(len(title_1) + 8*5))
    print(title_1)
    print("-"*(len(title_1) + 8*5))
    for i in range(n):
        print(f'{P1[i]:4.2f}\t{P2[i]:4.2f}\t{T1[i]:4.2f}\t{T2[i]:4.2f}\t{T3[i]:4.2f}\t{T4[i]:4.2f}\t{T6[i]:4.2f}\t{V:4d}\t{I[i]:4.2f}')

    thCOP = []
    for t1, t3 in zip(T1, T3):
        thCOP.append(th_COP(t1, t3))

    title = f'n\tEXP COP\t TH COP\t ERROR'
    print(f"Initial Water Temperature (C): {T_w_i:.3f}")
    print(f"Initial R134a Temperature (C): {T_r_i:.3f}")
    print(f"Number of Observations       : {n}")
    print('-'*(len(title) + 4*2))
    print(title)
    print('-'*(len(title) + 4*2))
    error = []
    i = 0
    for e, t in zip(expCOP, thCOP):
        print(f'{i}\t{e:6.4f}\t{t:6.4f}\t{(t - e)/t:6.4f}')
        error.append((t-e)/e)
        i += 1

    #show_plot([i for i in range(n)], error)

