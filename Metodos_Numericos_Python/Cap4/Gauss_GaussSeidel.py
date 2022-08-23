import numpy as np

#Metodo de Gauss-Jacobi e Gauss Seidel

#Exemplo 4.5 e 4.6 com erros no livro

def calculo_erro(x,x2,tipo,n):
    erro = np.zeros(n,dtype=np.float64)
    if tipo == 'absoluto':
        for i in range(n):  
            erro[i] = x[i] - x2[i]
        
    if tipo == 'relativo':
        for i in range(n):
            erro[i] = (abs(x[i]-x2[i]))/abs(x[i])   

    return erro 

def GaussJacobi(A,x,b,tol):
    n = A.shape[0]
    erro = np.zeros(n,dtype=np.float64)
    erro[:]= 1000
    iter=0
    while max(abs(erro))>=tol:
        x2 = x.copy()
        x= np.zeros(n, dtype = np.float64)
        for i in range(n):
            for j in range(n):  
                if (i != j):
                    x[i]= x[i]+ A[i,j]*x2[j]
            x[i] = (1/A[i,i])*(b[i] - x[i])
            
        erro = calculo_erro(x,x2,'absoluto',n)
        iter = iter+1    
   
    return x,iter

def GaussSeidel(A,x,b,tol):
    n = A.shape[0]
    erro= np.zeros(n,dtype=np.float64)
    erro[:]=1000
    iter=0
    while (max(abs(erro))>=tol):
        x2=x
        x=np.zeros(n)
        for i in range(n):
            for j in range(n):  
                if (i!=j):
                    if (j<i):
                        x[i]= x[i] + A[i,j]*x[j]
                    else:
                        x[i]= x[i]+ A[i,j]*x2[j]
            x[i] = (1/A[i,i])*(b[i] - x[i])

        erro = calculo_erro(x,x2,'relativo',n)
        iter=iter+1    

    return x, iter     

#Main

if __name__ == '__main__':

    A = np.array([[6,-1,2,0],[0,9,0,4],[2,-1,10,-1],[0,0,-1,8]])
    b = np.array([2,22,-11,9])
    x= np.array([0,0,0,0]) #initial solution
    tol = 10e-3
    # i = input('Digite 0 para Met. de Gauss e 1 para Gauss Seidel')
    # if i == '0' :
    #Gauss Jacobi
    sol_GJ,iter_GJ=GaussJacobi(A,x,b,tol) 
    # #Gauss Seidel 
    sol_GS,iter_GS =GaussSeidel(A,x,b,tol)    
    #     disp('Soluçao Final')
    #     disp(sol)  

    print("")
