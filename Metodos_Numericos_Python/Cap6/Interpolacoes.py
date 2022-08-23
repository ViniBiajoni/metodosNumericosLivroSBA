import numpy as np
import matplotlib.pyplot as plt

def vandermonde(x,y):
    num_points = x.shape[0]
    A=np.zeros((num_points,num_points),np.float64)
    
    for i in range(num_points):
        for j in range(num_points):
            A[i,j] = x[i]**j

    coef = np.linalg.inv(A)@np.transpose(y)
    
    return coef

def lagrange(x,y,x_interpol):
    #programa de interpolação pela Forma de Lagrange
    #dados de entrada
    #quantidade de pontos
    n=x.shape[0]
    L = np.zeros(n) 
    for i in range(n):
        L[i] = 1
        for j in range(n):
            if (j != i):
                L[i]=L[i]*(x_interpol-x[j])/(x[i]-x[j])
    
    #valor interpolado
    y_interpol=0
    for i in range(n):
        y_interpol=y_interpol+y[i]*L[i]
    
    

    return y_interpol

def newton_interpol2(x,y,x_interpol):
    #Programa de interpolação pela Forma de Newton
    #construção da tabela de diferenças divididas
    n = x.shape[0]
    Dif_Div =  np.zeros((n,n))
    #Cálculo das diferenças divididas de ordem 1
    for i in range(n):
        Dif_Div[i,0]=y[i]

    for j in range(1,n):
        cont = 0
        for i in range(n-j):
            Dif_Div[i,j] = (Dif_Div[i+1,j-1]-Dif_Div[i,j-1])/(x[j+i]-x[i])
            cont = cont + 1
    print('Tabela de Diferenças divididas do método de Newton')
    print(Dif_Div)
    #armazenamento das diferenças divididas
    d = np.zeros(n)
    d[0] = y[0]
    for k in range(n):
        d[k]=Dif_Div[0,k]

    y_interpol=d[0]
    for i in range(1,n):
        #componentes (x-xi)
        compx =1
        for j in range(i):
            compx = compx*(x_interpol-x[j])
        y_interpol=y_interpol+d[i]*compx
    return y_interpol


if __name__ == '__main__':
    #Exemplo 6.1, 6.2, 6.3
    x = np.array([1.5, 3.5, 7. ,11.5, 14]) 
    y = np.array([3,6,2.5,9.5,7.4])
    x_interpol = 10

    # Retorna Coeficientes do Polinômio
    coefs_vander = vandermonde(x,y)

    # Retorna o valor y referente ao valor x 
    y_lagrange = lagrange(x,y,x_interpol)
    y_newton = newton_interpol2(x,y,x_interpol) 

    print('Polinômio obtido método de Vandermonde')
    print(round(coefs_vander[0],6)),
    for i in range(1,len(coefs_vander)):
        print(f'{round(coefs_vander[i],6)}x^{i}'),
    print(f'Valor de f({x_interpol}), obtido pelo método de Lagrange')
    print(y_lagrange)
    print(f'Valor de f({x_interpol}), obtido pelo método de Newton')
    print(y_newton)
