//programa de interpolação pela Forma de Lagrange
//dados de entrada
x=input('valores do vetor x :  ')
y=input('valores do vetor y:  ')
x_interpol=input('valor do ponto x a ser interpolado:  ')
n=length(x);  //quantidade de pontos
  for i=1:n
    L(i)=1;
    for j=1:n
      if j < > i
        L(i)=L(i)*(x_interpol-x(j))/(x(i)-x(j));
      end
    end
  end
  soma=0;
  for i=1:n
    soma=soma+y(i)*L(i);
  end
  y_interpol=soma   //valor interpolado
