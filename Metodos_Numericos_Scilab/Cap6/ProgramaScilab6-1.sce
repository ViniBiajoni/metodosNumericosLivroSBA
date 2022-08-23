//Sistema de Vandermonde Va=f
//Definição da matriz V
V=[1 1.5 1.5^2 1.5^3 1.5^4;1 3.5 3.5^2 3.5^3 3.5^4;1 7 7^2 7^3 7^4;
1 11.5 11.5^2 11.5^3 11.5^4;1 14 14^2 14^3 14^4]
//Definição do vetor f
f=[3;6;2.5;9.5;7.4]
//Solução do sistema
a=V\f
printf('coeficientes do polinômio em ordem crescente: \n')
disp(a)
