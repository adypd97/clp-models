#!/usr/bin/env python3

'''
Sample Observations
V   I     T1     T2  T3  T4  T5  T6  T7  T8

50  0.23  25     27  29  33  35  38  36  21
50  0.23  28     31  36  42  44  49  44  23
50  0.23  28     31  36  42  44  49  44  23 X
50  0.23  32     37  42  50  54  59  53  25
'''

D = 45  # mm, diameter
L = 450 # mm, length

V = 50
I = 0.23
Q = V * I
A = 3.14*D*L*10E-06

def Ts(T): # T ~ T1,2,...,7
    # avg surface Temp
    return [ sum(t)/len(t) for t in T ]

def h_exp(ts, ta):
    assert len(ts) == len(ta), "lengths don't match"
    return [ (Q/A)*(vs-va) for vs,va in zip(ts,ta)]

def main():
    obs_s = [ [25,27,29,33,35,38,36],
              [28,31,36,42,44,49,44],
              [32,37,42,50,54,59,53],
            ]

    obs_a = ta = [21,23,25]
    ts = Ts(obs_s)
    h  = h_exp(ts, ta)

    print(f'h values: {h}')
    print(f"average h_exp = {sum(h)/len(h)} watts/m^2*degree_celcius")


if __name__ == "__main__":
    main()

