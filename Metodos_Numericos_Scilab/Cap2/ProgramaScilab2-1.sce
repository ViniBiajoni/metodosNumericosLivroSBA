//Programa para a conversão de um número inteiro binário em decimal
//Entrada de dados: digite o número binário a ser convertido entre colchetes
// com os dígitos separados por espaços
//Exemplo: [1 0 1 0 1 1 0]
clear; // elimina (limpa) as variáveis da memória
b=input('Forneça o vetor contendo o número inteiro binário a ser convertido: ')
//determinação do tamanho do vetor (1 x n) que contém o número binário
n=size(b,2);
//início do processo de conversão
a(1)=b(1);
//recursão
for k=1:n-1
    a(k+1)=b(k+1)+2*a(k);
end
//apresenta o número decimal procurado
printf("Número Inteiro Decimal Convertido:\n %g", a(n))
