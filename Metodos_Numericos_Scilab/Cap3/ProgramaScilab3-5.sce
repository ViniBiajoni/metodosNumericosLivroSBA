//Programa para se obter o zero de uma função
funcprot(0); 
//definição da função cujo zero deve ser obtido
function y=funcao(x)
    y=cos(x)-3+exp(x)
endfunction
//definição do valor inicial
x0=1;
//obtenção da solução
solucao=fsolve(x0,funcao)
printf('Solução: \n')
disp(solucao)
