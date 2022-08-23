#Programa do Método da Secante

#Algotirmo Apresentado no livro (página 78)
#Exemplo 3.6:
# Valor inicial do processo iterativo: 1
# Valor inicial do processo iterativo: 0.8
# Valor inicial da tolerância: 0.0000005 
# Número maximo de iterações: 20 


import numpy as m


# Define Função
def fct(x):
    #y =  m.cos(x) - 3 + m.exp(x)
    #y = 1/x - x**2*m.exp(-x)
    #y=x*(m.cosh(200/x)-1)-100
    #y = (1+x)**(-12) +8.5*x-1
    y = (m.sin(x)**3)/(x-m.sin(x)*m.cos(x))-1
    return y


x=[]
x.append( float(input("Digite o valor inicial do processo iterativo: ")))
x.append( float(input("Digite o SEGUNDO valor do processo iterativo: ")))
tol = float(input("Digite o valor inicial da tolerância: "))
precisao = len(str(tol)) + 1 # Ajusta as impressões na saida de acordo com o número de casas da tolerância
iter_max = int(input("Digite o número maximo de iterações: "))
iter = 1
desvio_absoluto = m.inf
while (desvio_absoluto > tol and iter <=iter_max):
    print(f"Iteração {iter}") 
    delta = fct(x[iter])*(x[iter]-x[iter-1])/(fct(x[iter])-fct(x[iter-1]))
    x.append(x[iter] - delta)
    print(f"x{iter}=",round(x[iter],precisao))
    desvio_absoluto = abs(x[iter]-x[iter-1])
    desvio_relativo = abs(desvio_absoluto/x[iter])
    print(f"Desvio Abs.= {round(desvio_absoluto,precisao)}")
    print(f"Desvio Rel.= {round(desvio_relativo,precisao)}")
    iter = iter + 1
    print("--------------------------------------")
iter -=1
if(iter > iter_max):
    print("liminte máximo de iterações alcançado")
else:
    print(f"A solução obtida foi: {round(x[iter],precisao)}")
    print(f"o numero de iterações foi de {iter}")

