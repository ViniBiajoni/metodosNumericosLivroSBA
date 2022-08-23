//Programa de ajuste polinomial
//Método dos Mínimos Quadrados Ponderados
//leitura dos dados de entrada
clear;
Tabela=read('Cap7_Tabela_exemplo7-2.txt',-1,2)
x=Tabela(:,1);
y=Tabela(:,2);
n_pontos=length(x);
printf('Número total de pontos da amostra = %g \n', n_pontos)
//definição do grau do polinômio a ser ajustado aos dados
n_grau=input('grau do polinômio a ser ajustado:  ');
//cálculo das somas dos valores de x e de suas potências
for i=1:2*n_grau
    x_soma(i)=sum(x.^i);
end
//Formação da matriz A e do vetor b do sistema linear Ax=b, cuja solução
// corresponde aos coeficientes do polinômio a ser ajustado
//Primeira linha da matriz A e do vetor b
A(1,1)=n_pontos;
b(1)=sum(y);
for k=2:(n_grau+1)
    A(1,k)=x_soma(k-1);
end
//Demais linhas de A
for i=2:(n_grau+1)
    for j=1:(n_grau+1)
        A(i,j)=x_soma(i+j-2);
    end
//Formação do vetor b
    b(i)=sum(x.^(i-1).*y);
end
printf('Matriz de coeficientes = \n')
disp(A)
printf('Vetor independente = \n')
disp(b)
//Determinação dos coeficientes do polinômio
alfa=A\b
a_transposto=alfa'
//formação do polinômio interpolante
printf('Polinômio interpolante \n')
p=poly(a_transposto,"x","coeff")
//obtenção do gráfico de y e p(x)
for k=1:n_pontos
    f_ajuste(k)=horner(p,x(k));
end
plot2d(x,y,-5)
plot2d(x,f_ajuste,5)
disp(p)
