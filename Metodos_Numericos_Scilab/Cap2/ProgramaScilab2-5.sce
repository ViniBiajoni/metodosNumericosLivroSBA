//Programa para a conversão de um número fracionário decimal, com parte inteira nula, para binário
//Entrada de dados: digite o número decimal a ser convertido
clear; // elimina (limpa) as variáveis da memória
//inicia a contagem dos dígitos binários do número a ser obtido
k=1;
a=input('Forneça o número fracionário decimal a ser convertido: ')
r(1)=a;
k_lim=input('Forneça o número limite de dígitos binários desejados: ')
while (r(k) <> 0 & k<=k_lim)
    r_dobro=2*r(k);
    if(r_dobro >= 1)
        b(k)=1;
    else
        b(k)=0;
    end 
r(k+1)=r_dobro-b(k);
k=k+1;
end
//apresenta o número binário procurado
printf("Número Fracionário Decimal Convertido: \n")
//transforma em um string o conteúdo do vetor r
// em que estão armazenados os dígitos binários
str=string(b')
disp(str)
