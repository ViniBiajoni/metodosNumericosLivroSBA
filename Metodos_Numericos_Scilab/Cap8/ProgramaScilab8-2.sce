//Programa para integração numérica no intervalo [a,b],
//subdividido em n_subint partes (no. par), adotando-se a Regra 1/3 de Simpson
//===============================================
clear(); //limpa a memória
//definição da função a ser integrada
function nome = integrando(x)
    nome=x*exp(-x)
endfunction
//===============================================
funcprot(0);
//definição do intervalo de integração, tolerância e número de subintervalos
a=input('entre com o extremo inferior do intervalo de integração   ');
b=input('entre com o extremo superior do intervalo de integração   ');
tol=input('entre com o valor da tolerância (precisão) para integração   ');
n_subint=input('entre com o número (par) de subintervalos   ');
//===============================================
//cálculos da Regra de Simpson
h=(b-a)/n_subint
x=a:h:b
    for i=1:n_subint+1
        y(i)=integrando(x(i))
    end
    I=(h/3)*(y(1)+4*sum(y(2:2:n_subint))+2*sum(y(3:2:n_subint-1))+y(n_subint+1))
//===================================================
//determinação do valor da integral
printf('Valor da Integral pela Regra 1/3 de Simpson  = %g', I)
