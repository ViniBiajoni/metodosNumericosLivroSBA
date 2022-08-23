import numpy as np
def dg1(x):
    y = -1/1.2 *(0.5*x*np.exp(0.5*x) + np.exp(0.5*x))

    return y

def dg2(x):
    y = -5 *(0.5*np.exp(0.5*x)/(np.exp(0.5*x) + 1.2)**2)

    return y

def dg3(x):
    y = -0.5 *(5- 1.2*x)*np.exp(-0.5*x) - 1.2*np.exp(-0.5*x)

    return y

def L(x):
    l = 1*x*np.sinh(200/x)
    return l

def q9(x):
    y = 3*x**2 - 5*np.cos(x)
    return y

    

print('n')
