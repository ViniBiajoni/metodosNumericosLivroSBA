import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':
    ####Ajuste Polinomial
    # //programa de ajuste polinomial pelo Método dos Mínimos Quadrados Ponderados
    # Exemplo 7.2)
    x = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]);
    y = np.array([3.0, 2.6, 4.9, 5.3, 7.0, 7.5, 7.8, 7.6, 9.5, 9.0, 9.5,10.5,10.0, 8.5, 8.3, 9.2, 8.7]);

    #Número Total de Pontos da Amostra
    n_pontos=x.shape[0];
    # Grau do polinômio a ser ajustado aos dados
    n_grau= 2;
    # Soma dos valores de x e de suas potências
    x_soma=np.zeros(2*n_grau, dtype = np.float64)
    for i in range(2*n_grau):
        x_soma[i]=sum(l**(i+1) for l in x)

    # //Formação da matriz A e do vetor b do sistema linear Ax=b, cuja solução
    # // corresponde aos coeficientes do polinômio a ser ajustado
    # //Primeira linha da matriz A e do vetor b
    A=np.zeros((n_grau+1,n_grau+1), dtype = np.float64)
    b=np.zeros(n_grau+1, dtype = np.float64)
    A[0,0]=n_pontos
    b[0]=sum(y)
    for k in range(1,n_grau+1):
        A[0,k] = x_soma[k-1]

    # //Demais linhas de A
    for i in range(1,n_grau+1):
        for j in range(n_grau+1):
            A[i,j]=x_soma[i+j-1]

    # //Formação do vetor b
    for i in range(1,n_grau+1):
        for j in range(n_pontos):
            b[i] += y[j]*(x[j]**i) 

    # //Determinação dos coeficientes do polinômio
    # alfa=A\b
    alfa = np.linalg.inv(A)@np.transpose(b)
    
    # POlinônio Interpolante
    y_ajuste = np.zeros(n_pontos,dtype=np.float64)
    for i in range(n_pontos):
        for j in range(n_grau+1):
            y_ajuste[i] = y_ajuste[i] + alfa[j]*x[i]**j

    print("Matriz A")        
    print(A) 

    print("Matriz b")        
    print(b) 

    print("Parametros da Função de Ajuste")        
    print(alfa) 

    #Gráfico 
    #Pontos de entrada
    plt.scatter(x, y, marker = 'o',label = 'Pontos da amostra', color = 'red')
    plt.plot(x, y_ajuste, label = 'Ajuste')

    
    # Nome dos Eixos
    plt.xlabel('Eixo - x')
    plt.ylabel('Eixo - y')
    
    # Título do Gráfico
    plt.title('Ajuste Polinomial Mínimos Quadrados')
    
    # Cria janela com Gráfico
    plt.legend()
    plt.show()






