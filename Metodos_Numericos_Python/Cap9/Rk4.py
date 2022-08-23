import numpy as np
import matplotlib.pyplot as plt

def func_analitica(x):
    dy_dx = 3/5*np.e**(x/3) + 2.4*np.e**(-x/2) 
    return dy_dx 

def func(x,y):
    dy_dx = (1/2)*np.exp(x/3) - (1/2)*y #Exemplo 9.2
    return dy_dx

def rk4(y0,x0,h,I):
    n =  (I[1] - I[0])/h
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

    _,ax = plt.subplots()
    ax.set(xlabel ='X', ylabel ='Y',
       xlim =(0,5.5), ylim =(0, 5),
       title ='Método Rk4')
    ax.grid()
    ya = func_analitica(np.array(x))
    plt.plot(x, ya, marker = 'x', label = 'Numérico')
    plt.plot(x, y , marker = '*', label = 'Analítico')
    plt.legend()
    plt.show()
    return


if __name__ == '__main__':
    #Pvi
    y0= 3
    x0= 0
    #intervalo
    I = [0,5]
    # Passo
    # num_sub_int = 4
    h = 1 
    # h = (I[1] - I[0])/num_sub_int
    rk4(y0,x0,h,I)
    
