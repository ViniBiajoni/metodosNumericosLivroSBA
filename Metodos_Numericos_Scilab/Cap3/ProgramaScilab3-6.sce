//Programa para obter a solução de uma equação pelo Método de Newton
//Definição da função cujo zero se procura
funcprot(0);
function z=funcao(t)
    z=cos(t)-3+exp(t)
endfunction
//Obtenção da derivada da função
function y=derivada(t)
    y=-sin(t)+exp(t)
endfunction
//Definição do ponto inicial
a=input('Entre com o valor inicial do processo iterativo  ');
//Definição da tolerância
tol=input('Entre com a tolerância do processo iterativo  ');
//Definição do número máximo de iterações do processo 
k_max=input('Entre com o número máximo de iterações do processo  ');
//Início das iterações
k=1;
da=100; //valor elevado escolhido arbitrariamente
//Definição do valor inicial
x(k)=a;
//Processo iterativo
while(k <= k_max & da > tol)
    delta=-funcao(a)/derivada(a);
    x(k+1)=x(k)+delta;
    da=abs(x(k+1)-x(k));
    dr=da/x(k+1);
    a=x(k+1);
    k=k+1;
end
num_iter=k-1;
//mensagem para indicar que o número máximo de iterações foi atingido
if(k > k_max) then
    printf('Limite de iterações foi atingido  \n')
end
//solução da equação
printf('A solução obtida foi %f \n',a)
printf('O número de iterações foi de %d \n',num_iter)
