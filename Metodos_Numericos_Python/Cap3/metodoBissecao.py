import numpy as np

def f(x):
    # f = x**6 - x -1
    # f = x**3 - 9*x + 3 
    #h = np.cos(x) - 3 + np.exp(x) 
    h=np.exp(x) -4*x**2
    return h


#Método da Bisseção

a=0.0
b=1
tol = 0.001
# a=1
# b=3
# tol = 0.001


x = (a+b)/2

iter=0

while abs(f(x)) > tol:

    print(f"Iteração {iter}\n")
    print(f"a = {a}\n")
    print(f"b = {b}\n")
    print(f"x = {x}\n")
    print(f"f(x) = {f(x)}\n")
    print(f'------------------')
    if f(a)*f(x)<0:
        a=a
        b=x
    elif f(x)*f(b)<0:
        a=x
        b=b
    
    x = (a+b)/2

    iter += 1

print(f"A raiz da função é : {x}")
print(f"Total de iterações = {iter}")