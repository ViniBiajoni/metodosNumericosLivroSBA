import numpy as np

#Fatoração LDU
def LDU(A,b):
    n = len(A)

    L,A = elimGauss(A)
    # Fatora b
    y=b
    for j in range(n-1):
        for i in range(j+1,n):
            y[i] = y[i] - L[i,j]*y[j]

    D=np.identity(n)
    for i in  range(n):
        D[i,i]=A[i,i]

    z=np.zeros(n)
    for i in range(n):
        z[i]=y[i]/D[i,i]

    for i in  range(n):
        A[i,:]=A[i,:]/A[i,i]    

    U=A
    #x=U\z ou x = (U^-1)*z
    x = np.linalg.inv(U)@z

    return L,D,U,x      
    
# Eliminação de Gauss
def elimGauss(A):
    n=len(A)
    L=np.identity(n)
    for i in range(n-1):
        #Elemento pivô
        piv =  A[i,i]
        for j in range(i+1,n):
            #Multiplicador 
            m = (A[j,i]/piv)
            L[j,i] = m
            A[j,:] = A[j,:] - m*A[i,:]
 
    return L,A

# Função Principal do programa   
if __name__ == '__main__':

    # Exemplo simples 3x3 solução:  x= [-1/3, 2/3, 0]
    A=[[1,2,3], [4,5,6], [7,8,8]]
    b = [1,2,3]

    # Exemplo do livro 4.1 e 4.2:  
    # A=[[4, -2, -3, 6],
    #    [-6, 7, 6.5, -6],
    #    [1, 7.5, 6.25, 5.5],
    #    [-12, 22, 15.5, -1]]
    # b = [12, -6.5, 16, 17]

    # # Exemplo da lista 1  
    # A=[ [2, -1, 0, 0, 0, 0], 
    #     [-1, 2, -1, 0, 0, 0], 
    #     [0, -1, 2, -1, 0, 0], 
    #     [0,  0, -1, 2, -1, 0], 
    #     [0,  0, 0, -1, 2, -1], 
    #     [0,  0, 0, 0, -1, 2] ]

    # #b = [2, -1, 7, 5, 4, 3]
    # b = [0, 0, 0, 0, 0, 1]

    # # Exemplo da lista 1  
    # A=[ [2, 0, 0, 8, 0], 
    #     [0, 2, 0, 0, 0], 
    #     [0, 0, 4, 0, 0], 
    #     [4, 0, 0, 16, 0], 
    #     [1,  1, -1, 2, -1]]

    # #b = [2, -1, 7, 5, 4, 3]
    # b = [0, 0, 0, 0, 0, 1]

    #Exemplo Slide
    # A=[ [ 6, 1,  -2,  0],
    #     [ 0, 9,   0,  4],
    #     [ 2,-1,  10, -1],
    #     [ 0, 0,  -1,  8]]
    # b = [12, -6.5, 16, 17]
    
    A=np.array(A,dtype=np.float64)
    print(f'Determinante de A: {np.linalg.det(A)}')
    
    # Solução do Sistema
    L,D,U,x = LDU(A,b)

    print('Matriz A:')
    print(A)
    print('Matriz L:')
    print(L)
    print('Matriz D:')
    print(D)
    print('Matriz U:')
    print(U)
    print('Solução x:')
    print(x)
