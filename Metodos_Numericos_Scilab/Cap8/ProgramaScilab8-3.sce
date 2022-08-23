//Programa para integração numérica no intervalo [a,b],
//subdividido em n_subint partes (múltiplo de 3), adotando-se a Regra 3/8 de Simpson
//==================================================
clear(); //limpa a memória
//==================================================
//definição da função a ser integrada
function nome = integrando(x)
    nome=(log(x)^2)/x
endfunction
//==========================================================================
funcprot(0);
//definição do intervalo de integração, tolerância e número de subintervalos
a=input('entre com o extremo inferior do intervalo de integração   ');
b=input('entre com o extremo superior do intervalo de integração   ');
tol=input('entre com o valor da tolerância (precisão) para integração   ');
n_subint=input('entre com o número (múltiplo de 3) de subintervalos   ');
//cálculos da Regra 3/8 de Simpson
h=(b-a)/n_subint
x=a:h:b
    for i=1:n_subint+1
        y(i)=integrando(x(i))
    end
I=(3*h/8)*(y(1)+3*sum(y(2:3:n_subint-1))+3*sum(y(3:3:n_subint))+...
    2*sum(y(4:3:n_subint-2))+y(n_subint+1))
//=========================================================================
//determinação do valor da integral
printf('Valor da Integral pela Regra 3/8 de Simpson  = %g', I)
