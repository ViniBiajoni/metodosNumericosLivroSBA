import numpy as np

def f(x):
    # f = x**6 - x -1
    # f = x**3 - 9*x + 3 
    h = np.cos(x) - 3 + np.exp(x) 
    return h

#Falsa Posição
a=0.8
b=1
tol = 0.5e-6

x = (a*f(b) - b*f(a))/(f(b)-f(a))

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

    x = (a*f(b) - b*f(a))/(f(b)-f(a))
    
    iter += 1

print(f"A raiz da função é : {x}")
print(f"Total de iterações = {iter}")