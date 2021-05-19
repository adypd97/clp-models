#!/usr/bin/env python3

A       = 0.128 # m^2, Area of measuring tank
rho     = 1000  # kg/m^2, density of fluid
mtr_eff = 0.8   # motor efficiency assumed
g       = 9.81  # acc. due to gravity
h_pg    = 1     # m, height of pressure gauge from vacuum gauge
P       = 10E-04   # fix later TODO

emc     = 3200
'''
Sample Observations
N    Pd  Ps  R1  R2  t   tp
1200 0.2 60  0   11  20  32.19
1200 0.3 80  11  18  20  34.12
'''

def rise(r1, r2):
    return [ abs(v1 - v2)/100 for v1,v2 in zip(r1,r2)]

def Ei(tp): # pump input
    return [ P*(3600/emc)*t for t in tp ]

def Es(tp): # shaft output
    return [ P*mtr_eff*(3600/emc)*t for t in tp ]

def head(pd, ps):
    return [10*(vd + vs/760) + h_pg for vd,vs in zip(pd,ps)]

def discharge(r1,r2,t):
    return [(A*r)/t for r in rise(r1,r2)]

def Eo(pd,ps,r1,r2): #pump output
    t = 20 # sec
    Q = discharge(r1,r2,t) 
    H = head(pd,ps)
    assert len(Q) == len(H), "Q and H have diff lens"
    return [ g*q*h for q,h in zip(Q,H)] # rho/1000 = 1

def eta_o(pd,ps,r1,r2,tp): # overall efficiency
    return [(eo/ei)*100 for eo,ei in zip(Ei(tp), Eo(pd,ps,r1,r2))]

def eta_p(pd,ps,r1,r2,tp): # pump efficiency
    return [(eo/es)*100 for eo,es in zip(Eo(pd,ps,r1,r2), Es(tp))]


def show_plot(x, y, xlabel='Discharge Q (x10e-4 m^3/s)', 
        ylabel='Pump efficiency', 
        title='Discharge Q vs Pump efficiency',
        savefig='results/pumpeffvsQ.png'):
    import  matplotlib.pyplot as plt
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(savefig)
    plt.show()

def main():
    pd = [0.2,0.3,0.4]
    ps = [60,80,100]
    r1 = [0,11,18]
    r2 = [11,18,23]
    tp = [32.19,34.12, 35.10]
    t  = 20
    h = head(pd,ps)
    eff = eta_p(pd,ps,r1,r2,tp)
    dis = discharge(r1,r2,t)
    dis = [d*10000 for d in dis]
    print(eff)
    print(dis)
    show_plot(dis, eff)
    print('---')
    print(h)
    print(dis)
    show_plot(dis, h, xlabel='Discharge Q (x10e-4 m^3/s)',
            ylabel='Head (m)',
            title='Discharge Q vs Head',
            savefig='results/headvsQ.png')
    

if __name__ == "__main__":
    main()








