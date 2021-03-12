import random
from statistics import mean

def t_cal(V, I, T7):
    Q = V * I
    K1 = 52
    K2 = 1.4
    K3 = 0.12
    X1 = 0.02
    X2 = 0.015
    X3 = 0.012
    D = 0.25
    A = 3.14 * D * D / 4
    T5 = T7 + (Q * X3) / (2 * K3 * A)
    T3 = T5 + (Q * X2) / (2 * K2 * A)
    T1 = T3 + (Q * X1) / (2 * K1 * A)
    return T5, T3, T1


T5, T3, T1 = t_cal(73, 0.69, 28)
T6, T4, T2 = t_cal(73, 0.69, 28)
T7 = 30
T8 = 30

def data(lb, ub, n=100, dist=random.uniform):
    return [dist(lb, ub) for _ in range(n)]


def gen_V(V):
    error = 0.01  # 1% error
    ub = V
    lb = V - error * V
    return data(lb, ub)


def gen_I(I):
    error = 0.01  # 1% error
    ub = I
    lb = I - error * I
    return data(lb, ub)


def gen_T(T):
    error = 0.1  # 10% error
    lb = T - error * T
    return data(lb, 10 * error, dist=random.gauss)
'''
def gen_T5(T):
    error = 0.1  # 10% error
    lb = T - error * T
    return data(lb, 10 * error, dist=random.gauss)

def gen_T3(T):
    error = 0.1  # 10% error
    lb = T - error * T
    return data(lb, 10 * error, dist=random.gauss)

def gen_T1(T):
    error = 0.1  # 10% error
    lb = T - error * T
    return data(lb, 10 * error, dist=random.gauss)

def gen_T8(T):
    error = 0.1  # 10% error
    lb = T - error * T
    return data(lb, 10 * error, dist=random.gauss)

def gen_T6(T):
    error = 0.1  # 10% error
    lb = T - error * T
    return data(lb, 10 * error, dist=random.gauss)

def gen_T4(T):
    error = 0.1  # 10% error
    lb = T - error * T
    return data(lb, 10 * error, dist=random.gauss)

def gen_T2(T):
    error = 0.1  # 10% error
    lb = T - error * T
    return data(lb, 10 * error, dist=random.gauss)
'''

Vg = gen_V(73)
Ig = gen_I(0.7)
T1g = gen_T(T1)
T2g = gen_T(T2)
T3g = gen_T(T3)
T4g = gen_T(T4)
T5g = gen_T(T5)
T6g = gen_T(T6)
T7g = gen_T(T7)
T8g = gen_T(T8)

'''print("V: {0} , I: {1:.2f}".format(73, 0.69))
'''
print("Average(In degree C):  T1 = {0:.2f}   T2 = {1:.2f}    T3 = {2:.2f}   T4 = {3:.2f}   T5 = {4:.2f}   T6 = {5:.2f}   T7 = {6:.2f}   T8 = {7:.2f}".format(mean(T1g), mean(T2g), mean(T3g),mean(T4g),mean(T5g),mean(T6g),mean(T7g),mean(T8g)))
print("========")
print("No.     V      I      T1      T2      T3      T4      T5      T6      T7      T8")

for i in range(len(T1g)):
    print("{0:3d}   {1:.2f}    {2:.2f}   {3:.2f}   {4:.2f}   {5:.2f}   {6:.2f}   {7:.2f}   {8:.2f}   {9:.2f}   {10:.2f}".format(i+1, Vg[i], Ig[i], T1g[i], T2g[i], T3g[i],T4g[i],T5g[i],T6g[i],T7g[i],T8g[i]))

#print(gen_T7(30))   #room temperature
#print(gen_T8(30))
#print(gen_I(0.7))
#print(gen_V(73))
# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
