#Programa do Método de Ponto Fixo

#Algotirmo Apresentado no livro (texto página 69)

import numpy as m

# Define Função
def fcth(x):
    #y = m.cos(x) - 3 + m.exp(x)
    y=x
    return y

def fctg(x):
    #y= m.log(m.cos(x) - 3 + m.exp(x))
    #y = m.log(3-m.cos(x))
    #y = (5-x*m.exp(0.5*x))/1.2
    #y  = 5/(m.exp(0.5*x) + 1.2)
    #y = (5 - 1.2*x)/(m.exp(0.5*x))
    #y = m.log(4*(x)**2)
    y = (m.exp(x)/4)**(1/2)
    return y

iter=0
x=[]
x.append(m.float(input('Digite o valor inicial: ')))
tol = m.float64(input("Digite o valor inicial da tolerância: "))
precisao = len(str(tol)) + 1 
# Ajusta as impressões na saida de acordo com o número de casas da tolerância
iter_max = int(input("Digite o número maximo de iterações: "))

desvio_absoluto = m.inf
while (abs(desvio_absoluto)> tol) and (iter<=iter_max):
    print(f"Iteração {iter+1}") 
    g = fctg(x[iter]) #g(x)
    h = fcth(x[iter]) #h(x)
    print(f"g({x[iter]})=",h)
    print(f"h({x[iter]})=",g)
    x.append(g)
    iter = iter + 1
    desvio_absoluto = x[iter] - x[iter-1]
    desvio_relativo = desvio_absoluto/abs(x[iter])
    print(f"Desvio Abs.= {desvio_absoluto}")
    print(f"Desvio Rel.= {desvio_relativo}")
    print("--------------------------------------")
if(iter > iter_max):
    print("Liminte máximo de iterações alcançado")
else:
    print(f"A solução obtida foi: {x[iter]}")
    print(f"o numero de iterações foi de {iter}")