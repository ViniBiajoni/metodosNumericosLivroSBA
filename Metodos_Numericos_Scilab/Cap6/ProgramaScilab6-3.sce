//programa de interpolação pela Forma de Newton
//leitura dos dados de entrada
x=input('valores do vetor x :  ');
y=input('valores do vetor y:  ');
x_interpol=input('valor do ponto x a ser interpolado:  ');
//construção da tabela de diferenças divididas
n=length(x);
//cálculo das diferenças divididas de ordem 1
for i=1:n-1
    Dif_Div(i,1)=(y(i+1)-y(i))/(x(i+1)-x(i))
end
//cálculo das diferenças divididas de ordem superior
for j=2:n-1
    for i=1:n-j
        Dif_Div(i,j)=(Dif_Div(i+1,j-1)-Dif_Div(i,j-1))/(x(j+i)-x(i));
    end
end
//armazenamento das diferenças divididas
d(1)=y(1);
for k=2:n
    d(k)=Dif_Div(1,k-1);
end
//cálculo do valor de y_interpol no ponto x_interpol
delta_x=1;
y_interpol=d(1);
for i=2:n
    delta_x=delta_x*(x_interpol-x(i-1));
    y_interpol=y_interpol+d(i)*delta_x;
end
printf('valor de y interpolado = %g \n', y_interpol)
