#Importações das bibliotecas nativas e 
#declaração da função referente ao problema
import numpy as np
import matplotlib.pyplot as plt

def func(x,y):
    dy_dx = (2*y)*((92-y)/92)

    return dy_dx

# Método de Euler
def euler(y0,x0,h,I):
    n = (I[1] - I[0])/h
    x= []
    y= []
    x.append(x0)
    y.append(y0)
    print(f"y{0} = {y0}")
    for i in range(int(n)):
        yk = y0+ h*func(x0,y0)
        print(f"y{i+1} = {yk}")
        y0 = yk
        x0 = x0 + h
        x.append(x0)
        y.append(y0)
    return

# Método de Euler Modificado
def euler_modif(y0,x0,h,I):
    n = (I[1] - I[0])/h
    x= []
    y= []
    x.append(x0)
    y.append(y0)
    print(f"y{0} = {y0}")
    for i in range(int(n)):
        yk_til = y0 + func(x0,y0)*h
        f_xy = func(x0,y0)
        f_til_xy = func(x0+h,yk_til)
        k = (f_xy + f_til_xy)/2
        yk = y0+ k*h
        print(f"y{i+1} = {yk}")
        y0 = yk
        x0 = x0 + h
        x.append(x0)
        y.append(y0)
    return

# Método de Runge-Kutta de 4ª Ordem
def rk4(y0,x0,h,I):
    n = (I[1] - I[0])/h
    x= []
    y= []
    x.append(x0)
    y.append(y0)
    print(f"y{0} = {y0}")
    for i in range(int(n)):
        k1= func(x0,y0)
        k2= func(x0 + (1/2)*h, y0 + (1/2)*k1*h)
        k3= func(x0 + (1/2)*h, y0 + (1/2)*k2*h)
        k4= func(x0 + h, y0 + k3*h)
        kmedia = (k1 + 2*k2 + 2*k3 + k4)/6
        yk = y0 + kmedia*h
        print(f"y{i+1} = {yk}")
        y0 = yk
        x0 = x0 + h
        x.append(x0)
        y.append(y0)
    #Construção do gráfico da solução numérica
    _,ax = plt.subplots()
    ax.set(xlabel ='X', ylabel ='Y',
       xlim =(0,5.5), ylim =(0, 5),
       title ='Método Rk4')
    ax.grid()
    plt.plot(x, y, marker = '*')
    plt.show()
    return

if __name__ == '__main__':  
        #Pvi
    y0= 10
    x0= 0
    #intervalo
    I = [0,3]
    # Passo
    h = 1 
    euler(y0,x0,h,I)
    euler_modif(y0,x0,h,I)
    rk4(y0,x0,h,I)


