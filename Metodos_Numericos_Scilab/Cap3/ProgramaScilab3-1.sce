//Programa para procurar um intervalo [a,b] em que ocorre uma raiz de equação
clear;
function [a, b]=IntervaloRaiz(x0, delta_x, max_it, funcao) 
//valores iniciais do intervalo
a = x0;
b = x0 + delta_x;
//contador de tentativas para encontrar o intervalo da raiz
num_it = 0;
//busca pelo intervalo
while (funcao(a)*funcao(b)>0 & num_it < max_it)
    a = b;
    b = a + delta_x;
    num_it = num_it + 1;   
end
//mensagem para indicar que o limite de busca foi atingido
if (funcao(a)*funcao(b) > 0) then
    printf("Máximo de %d iterações atingido!\n",max_it);
    a = -%inf;
    b = %inf;
end
printf('número de tentativas: %g \n',num_it)
endfunction
//indicar a normalidade da definição de função
funcprot(0);
//=============================================
//definição da função cuja raiz é procurada
function y=funcao(x)
    y=x*cos(x)-1
endfunction
//=============================================
x0=input('valor inicial para a busca  ');
delta_x=input('tamanho do passo  ');
max_it=input('número máximo de tentativas  ');
[a,b]=IntervaloRaiz(x0,delta_x,max_it,funcao);
//impressão do intervalo
printf('limite à esquerda do intervalo: %f \n',a)
printf('limite à direita do intervalo: %f \n',b)
printf('valor da função à esquerda do intervalo: %f \n',funcao(a))
printf('valor da função à direita do intervalo: %f \n',funcao(b))


