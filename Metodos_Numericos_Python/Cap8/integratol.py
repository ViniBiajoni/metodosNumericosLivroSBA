import numpy as np
from IntegracaoNum import *
# def func(x):
#     y=2*(x**3)+x**2+1
#     return y
# def d2func(x):
#     y=6*(x**2)+2*x
#     return y

# def d4func(x):
#     y=12
#     return y
# //=====================================================
# //definição do intervalo de integração
if __name__ == '__main__':
    a = 0
    b = 1

    tol = 0.000001

    n_discret = 100
    x=a
    intervalo = np.linspace(a,b,num = n_discret)
    d_intervalo = d2func(intervalo)
    d4_intervalo = d4func(intervalo)
    m2=max(d_intervalo)
    m4=max(d4_intervalo)
    # //Número de subintervalos para que se atinja a tolerância especificada
    m=int(np.ceil(np.sqrt(((b-a)**3*m2)/(12*tol))))
    m13=int(np.ceil((((b-a)**5*m4)/(90*tol*2))**(1/4)))
    m38=int(np.ceil((((b-a)**5*m4)/(80*tol))**(1/4)))

    I_tr,_ =metodo_trapezio(a,b,m)
    I_13,_ =metodo_13Simpson(a,b,m13)
    I_38,_ =metodo_38Simpson(a,b,m38)

    print(I_tr,I_13,I_38)
    print('')
# aux(i)=deriv2;
# if x<=b
# x=x+d;
# else
# end
# end
# //obtenção do valor máximo aproximado da 2a. derivada do integrando
# M2=max(aux);
# //Número de subintervalos para que se atinja a tolerância especificada
# m=sqrt(((b-a)^3*M2)/(12*tol));


# a=input('entre com o extremo inferior do intervalo de integração ');
# b=input('entre com o extremo superior do intervalo de integração ');
# tol=input('entre com o valor da tolerância (precisão) para integração ');
# //====================================================
# //número de pontos para se discretizar a 2a. derivada do integrando
# // no intervalo de integração [a,b]




# x=a;
# for i=1:n_discret+1
# [deriv1,deriv2]=numderivative(funcao,x,[],2);
# aux(i)=deriv2;
# if x<=b
# x=x+d;
# else
# end
# end
# //obtenção do valor máximo aproximado da 2a. derivada do integrando
# M2=max(aux);
# //Número de subintervalos para que se atinja a tolerância especificada
# m=sqrt(((b-a)^3*M2)/(12*tol));
# m_subinterv=ceil(m)
# //tamanho de cada subintervalo
# h=(b-a)/m_subinterv;
# x=a:h:b;
# for i=1:m_subinterv+1
# aux(i)=funcao(x(i));
# end
# I_trapezios=(h/2)*(aux(1)+2*sum(aux(2:m_subinterv))+aux(m_subinterv+1))

######1/3 Simpson
# //Programa para integração numérica no intervalo [a,b],
# //subdividido em n_subint partes (no. par), adotando-se a Regra 1/3 de Simpson
# //===============================================
# clear(); //limpa a memória
# global I //declara I (valor da integral) como variável global
# //===============================================
# //definição da função a ser integrada
# deff('integrando=funcao(x)','integrando=x*exp(-x)')
# //===============================================
# funcprot(0);
# //cálculos da Regra de Simpson
# function I=regra_simpson_1(a, b, n_subint, funcao)
# global I
# h=(b-a)/n_subint
# x=a:h:b
# for i=1:n_subint+1
# y(i)=funcao(x(i))
# end
# I=(h/3)*(y(1)+4*sum(y(2:2:n_subint))+2*sum(y(3:2:n_subint-1))+y(n_subint+1))
# endfunction
# //===================================================
# //determinação do valor da integral
# regra_simpson_1(0,1,20,funcao);
# printf('Valor da Integral pela Regra 1/3 de Simpson = %g', I)


######3/8
# //Programa para integração numérica no intervalo [a,b],
# //subdividido em n_subint partes (múltiplo de 3), adotando-se a Regra 3/8 de Simpson
# //==================================================
# clear(); //limpa a memória
# global I //declara I (valor da integral) como variável global
# //==================================================
# //definição da função a ser integrada
# deff('integrando=funcao(x)','integrando=(log(x)^2)/x')
# //==================================================
# funcprot(0);
# //cálculos da Regra de Simpson
# function I=regra_simpson_2(a, b, n_subint, funcao)
# global I
# h=(b-a)/n_subint
# x=a:h:b
# for i=1:n_subint+1
# y(i)=funcao(x(i))
# end
# I=(3*h/8)*(y(1)+3*sum(y(2:3:n_subint-1))+3*sum(y(3:3:n_subint))+...
# 2*sum(y(4:3:n_subint-2))+y(n_subint+1))
# endfunction
# //===================================================
# //determinação do valor da integral
# regra_simpson_2(1,%e^2,75,funcao);
# printf('Valor da Integral pela Regra 3/8 de Simpson = %g', I)

#if __name__ == '__main__':
