//Exemplo de erros de arredondamento - Valores da Tabela 2.3
//
x(1)=1/10;
k=1;
while (k<61)
    if (x(k) <= 0.5) then
        x(k+1)=2*x(k); 
        end
    if (x(k) > 0.5) then
        x(k+1)=2*x(k)-1;
    end
    k=k+1;
end
for i=1:61
    j=i-1
    printf('valor calculado em %d %f \n', j, x(i))
end
