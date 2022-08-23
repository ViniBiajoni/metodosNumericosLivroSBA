//Programa para a conversão de um número decimal inteiro em binário
//Entrada de dados: Número decimal a ser convertido
clear; // elimina (limpa) as variáveis da memória
N=input('Digite o número decimal a ser convertido: ')
k=1;
a(k)=N;
while a(k)<>0
    r=modulo(a(k),2);
    if r==0 then b(k)=0;
    else b(k)=1;
    end
    a(k+1)=(a(k)-b(k))/2;
    k=k+1;
end
for i=1:k-1
  c(i)=b(k-i);
end
printf('Número binário convertido:\n ')
//transforma em um string o conteúdo numérico do vetor c (transposto) em que estão armazenados os dígitos binários
str=string(c')
