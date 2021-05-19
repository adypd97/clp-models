#!/usr/bin/env python3

#brass
Rb = 18  # mm
lb = 136 # mm
kb = 121 # W/m-k
alphab = 3.7*10E-05 # m2/s

#steel
Rs = 18  # mm
ls = 136 # mm
ks = 25  # W/m-k
alphas = 0.6*10E-05 # m2/s

L = (Rb*lb)/(2*lb + 2*Rb)*10E-03 # m
s = 0.009   # m, V/A characteristic dimension of solids

def fourier(t,alpha):
    fno = [ (alpha*v)/(L**2) for v in t ]
    return sum(fno)/len(fno)

def biot(T, fno):
    Tenv = 17    # celcius
    T0   = T[0]
    from math import log
    biot = []
    for i in range(1, len(T)):
        biot.append((log((T[i] - Tenv)/(T0 - Tenv)))/fno)
    return sum(biot)/len(biot)

def main():
    #OBSERVATIONS
    # brass
    Tb = [18.8, 23.5, 29.6, 33.3, 36, 37.7, 39.1, 40.1, 40.9, 41.5, 42, 42.3,
            42.6, 42.8, 42.9, 43.1]
    tb = [ 10*i for i in range(1, 17)]

    assert len(Tb) == len(tb)
    # steel
    Ts = [18, 18.7, 22, 25.5, 28.4, 30.8, 32.8, 34.6, 36.2, 37.4, 38.5, 39.3, 
            40, 40.6, 41.1, 41.6, 41.9, 42.2, 42.5, 42.7, 42.8, 42.9]
    ts = [10*i for i in range(1, 23)]
    assert len(Ts) == len(ts)

    # Fourier numbers
    fourierb = fourier(tb, alphab)
    fouriers = fourier(ts, alphas)
    print(f'Brass Fourier No.          : {fourier(tb, alphab)}')
    print(f'Steel Fourier No.          : {fourier(ts, alphas)}')

    # Biot numbers
    biotb    = biot(Tb, fourierb)
    biots    = biot(Ts, fouriers)
    print(f'Brass Biot No.             : {biotb}')
    print(f'Steel Biot No.             : {biots}')

    # Heat transfer coeffs
    hb       = (biotb*kb)/L
    hs       = (biots*ks)/L
    print(f'Brass Heat Transfer Coeff. : {hb}')
    print(f'Steel Heat Transfer Coeff. : {hs}')



if __name__ == "__main__":
    main()
