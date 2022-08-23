//programa de ajuste não polinomial 
clear
printf('Dados de entrada (valores de x e y) \n')
Tabela=read('Cap7_Tabela_exemplo7-3.txt',-1,2)
x=Tabela(:,1);
y=Tabela(:,2);
n_pontos=length(x);
printf('Número total de pontos da amostra = %g \n', n_pontos)
//definição do número de funções que compõem o ajuste
n_funcoes=3;
printf('Número de funções que participam do ajuste = %g \n', n_funcoes)
funcprot(0);
//definição das funções que compõem o ajuste
function g1=funcao1(x)
    g1=log(x)
endfunction
//valores de funcao1
for i=1:n_pontos
    Aux(i,1)=funcao1(x(i));
end
function g2=funcao2(x)
    g2=cos(x)
endfunction
//valores da funcao2
for i=1:n_pontos
    Aux(i,2)=funcao2(x(i));
end
function g3=funcao3(x)
    g3=exp(x)
endfunction
//valores da funcao3
for i=1:n_pontos
    Aux(i,3)=funcao3(x(i));
end
//Formação da matriz A e do vetor b do sistema linear Ax=b, cuja solução
// corresponde aos coeficientes da função global a ser ajustada
for i=1:n_funcoes
    for j=1:n_funcoes
        soma=0;
        for k=1:n_pontos
            soma=soma+Aux(k,i)*Aux(k,j);
        end
        A(i,j)=soma;
    end
end
//matriz A
printf('Matriz de coeficientes = \n'); disp(A)
//Formação do vetor b
for i=1:n_funcoes
    soma=0;
    for k=1:n_pontos
        soma=soma+y(k)*Aux(k,i);
    end
    b(i)=soma;
end
//vetor b
printf('Vetor independente = \n'); disp(b)
//Obtenção dos parâmetros da função de ajuste
printf('parâmetros da função de ajuste: \n')
alfa=A\b
disp(alfa)
//obtenção do gráfico de y e da função de ajuste
for k=1:n_pontos
    f_ajuste(k)=alfa(1)*funcao1(x(k))+alfa(2)*funcao2(x(k))+alfa(3)*funcao3(x(k));
end
plot2d(x,y,-5)
plot2d(x,f_ajuste,5)
