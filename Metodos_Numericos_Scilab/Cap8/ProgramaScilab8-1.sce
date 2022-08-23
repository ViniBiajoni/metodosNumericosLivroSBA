//Programa para se obter o valor da integral de uma função no intervalo [a,b],
// através da Regra dos Trapézios Repetida, com certo grau de precisão,
//estabelecido pelo parâmetro tol (tolerância)
//=====================================================  
//definição da função a ser integrada
function y=funcao(x)
    y=2*(x^3)+x^2+1
endfunction
//=====================================================
//definição do intervalo de integração
a=input('entre com o extremo inferior do intervalo de integração   ');
b=input('entre com o extremo superior do intervalo de integração   ');
tol=input('entre com o valor da tolerância (precisão) para integração   ');
//====================================================
//número de pontos para se discretizar a 2a. derivada do integrando
// no intervalo de integração [a,b]
n_discret=100;
d=(b-a)/n_discret;
x=a;
for i=1:n_discret+1
   [deriv1,deriv2]=numderivative(funcao,x,[],2);
   aux(i)=deriv2;
   if x<=b
       x=x+d;
   else
   end
end
//obtenção do valor máximo aproximado da 2a. derivada do integrando
M2=max(aux);
//Número de subintervalos para que se atinja a tolerância especificada
m=sqrt(((b-a)^3*M2)/(12*tol));
m_subinterv=ceil(m)
printf('Número de subintervalos \n')
disp(m_subinterv)
//tamanho de cada subintervalo
h=(b-a)/m_subinterv;
x=a:h:b;
for i=1:m_subinterv+1
    aux(i)=funcao(x(i));
end
I_trapezios=(h/2)*(aux(1)+2*sum(aux(2:m_subinterv))+aux(m_subinterv+1))
printf('valor da integral \n')
disp(I_trapezios)
