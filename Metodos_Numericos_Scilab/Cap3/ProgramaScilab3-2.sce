//Programa para se obter o zero de uma função pelo Método da Bisseção
funcprot(0);
clear
clc
//definição da função cujo zero deve ser obtido
function y=funcao(x)
  y=cos(x)-3+exp(x)
endfunction
//definição de parâmetros do problema
n=0
nmax=30
tol=0.5e-6
a=0.8
b=1.0
d=(b-a)/2
while (n <= nmax & d>tol)
    c=(a+b)/2
    d=(b-a)/2
    n=n+1
    if (funcao(c)*funcao(a)) > 0
        a=c
    else
        b=c
    end
end
printf('solução com %d bisseções.\n',n)
printf('raiz = %f',c)
