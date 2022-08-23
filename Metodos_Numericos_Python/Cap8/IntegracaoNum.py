
import numpy as np

#####Trapézios
# //Programa para se obter o valor da integral de uma função no intervalo [a,b],
# // através da Regra dos Trapézios Repetida, com certo grau de precisão,
# //estabelecido pelo parâmetro tol (tolerância)
# //=====================================================
# //definição da função a ser integrada
# def func(x):
#     y =np.e**((-x**2))
#     #y = np.sqrt(6*x-5)
#     return y
# # //definição da derivada a segunda a ser integrada
# def d2func(x):
#     y =4*x**2*np.e**(-x**2) - 2*np.e**(-x**2)
#     return y
# # //definição da derivada a segunda a ser integrada
# def d4func(x):
#     y=16*x**4*np.e**(-x**2) - 48*x**2*np.e**(-x**2) + 12*np.e**(-x**2)
#     return y

def func(x):
    y=x**5+1
    return y
def d2func(x):
    y=5*(x**4)
    return y

def d4func(x):
    y=60*x**2
    return y

def M2(vec_x):
    vec_d2 = d2func(vec_x)
    return max(vec_d2)

def M4(vec_x):
    vec_d4 = d2func(vec_x)
    return max(vec_d4)


def metodo_trapezio(a,b,m):
    h=(b-a)/m
    x = np.zeros(m+1)
    y = np.zeros(m+1)
    for i in range (m+1):
        x[i]=i*h+a
        y[i]=func(x[i])

    #Trapezio
    I_TR= y[0]
    for i in range(1,m):
        I_TR = I_TR +  2*y[i]
    I_TR = I_TR + y[m]
    
    I_TR = I_TR*(h/2)

    erro_t = erro_trapezio(h,x,m)
    return I_TR, erro_t

def metodo_13Simpson(a,b,r):
    m=2*r
    h=(b-a)/(m)
    n_pontos =m+1
    x = np.zeros(n_pontos)
    y = np.zeros(n_pontos)

    for i in range (n_pontos):
        x[i]=i*h+a
        y[i]=func(x[i])

    I_13SR= y[0]
    coef=4
    for i in range(1,m):
        I_13SR = I_13SR +  coef*y[i]
        if(coef==4): coef = 2
        else: coef = 4

    I_13SR = I_13SR + y[m]
    I_13SR = I_13SR*(h/3)

    erro_13s = erro_13simpson(h,x,m)

    return I_13SR, erro_13s

def metodo_38Simpson(a,b,r):
    m=3*r
    h=(b-a)/m
    x = np.zeros(m+1)
    y = np.zeros(m+1)

    for i in range (m+1):
        x[i]=i*h+a
        y[i]=func(x[i])


    I_38SR= y[0]
    coef=3
    for i in range(1,m):
        if(i%3 == 0):coef = 2
        else: coef = 3
        I_38SR = I_38SR +  coef*y[i]

    I_38SR = I_38SR + y[m]
    I_38SR = I_38SR*(h*3/8)

    erro_38s = erro_38simpson(h,x,m)

    return I_38SR, erro_38s

def erro_trapezio(h,x,m):
    erro_t = abs(-m*h**3*M2(x)/12)
    return erro_t

def erro_13simpson(h,x,m):
    erro_13s = abs(-h**5*M4(x)/90*(m/2))
    return erro_13s

def erro_38simpson(h,x,m):
    erro_38s = abs(-3*h**5*M4(x)/80*(m/3))
    return erro_38s
if __name__ == "__main__":
    #exemplo 8.3
    a=0
    b=2
    m=4;
    ms=2
    I_tr , erro_tr   = metodo_trapezio(a,b,m)
    I_13s, erro_13s  = metodo_13Simpson(a,b,ms)
    I_38s, erro_38s  = metodo_38Simpson(a,b,ms)


    print('')
