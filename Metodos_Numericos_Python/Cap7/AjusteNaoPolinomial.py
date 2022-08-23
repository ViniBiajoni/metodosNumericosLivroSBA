
import numpy as np
import matplotlib.pyplot as plt
####Ajuste Não Polinomial

# //definição das funções que compõem o ajuste
def func1(x):
    y=np.log(x)
    return y

def func2(x):
    y=np.cos(x)
    return y

def func3(x):
    y=np.e**x
    return y


if __name__ == '__main__':
    # x = np.array([-1.,-.7,-.4,-.1,0.2,0.5,0.8,1.0]);
    # y = np.array([ 36, 17,8.5,4.0,1.6,0.7,0.4,0.1]);
    #Exemplo 7.3
    x = np.array([0.25,0.65,0.95,1.25,1.75,2.00,2.25,2.55,2.75,3.05]);
    y = np.array([0.20,-.25,-1.1,-.45,0.25,0.10,-.30,0.25,0.55,1.05]);

    #Número total de pontos da amostra
    n_pontos=x.shape[0]

    # Número de funções que compõem o ajuste
    n_funcoes=3;

    #Vetor de Funções
    funcs = [func1, func2, func3]

    #Construção da Matriz A
    A=np.zeros([n_funcoes,n_funcoes],np.float64)

    #-Matriz contendo o resultado de cada função em cada ponto
    x_funcs = np.zeros([n_funcoes,n_pontos],np.float64)
    for f in range(n_funcoes):
        for i in range(n_pontos):
            x_funcs[f,i] = funcs[f](x[i])
    #-Constroi A com os resultados das funções
    for i in range(n_funcoes):
        for j in range(n_funcoes):
            soma = 0.0
            for k in range(n_pontos):
                soma = soma + x_funcs[i,k]*x_funcs[j,k]
            A[i,j] = soma
          

    #Construção do Vetor b
    b=np.zeros(n_funcoes,dtype = np.float64)
    for i in range(n_funcoes):
        for j in range(n_pontos):
            b[i] += y[j]*x_funcs[i,j]

    #Coeficientes da função de ajuste    
    alfa = np.linalg.inv(A)@np.transpose(b)

    ajuste = np.zeros(n_pontos,dtype=np.float64)
    for i in range(n_pontos):
        for j in range(n_funcoes):
            ajuste[i] = ajuste[i] +  alfa[j]*funcs[j](x[i])

     
    print("Matriz A")        
    print(A) 

    print("Matriz b")        
    print(b) 

    print("Parametros da Função de Ajuste")        
    print(alfa) 

    #Gráfico 
    #Pontos de entrada
    plt.scatter(x, y, marker = 'o',label = 'pontos da amostra', color = 'red')
    plt.plot(x, ajuste, label = 'Ajuste')

    
    # Nome dos Eixos
    plt.xlabel('Eixo - x')
    plt.ylabel('Eixo - y')
    # Título do Gráfico
    plt.title('Ajuste Não Polinomial')
    
    # Cria janela com Gráfico
    plt.legend()
    plt.show()
