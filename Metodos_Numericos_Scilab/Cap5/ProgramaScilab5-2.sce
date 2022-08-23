//definição das equações do sistema
funcprot(0);
function y=funcao(x)
  y(1)=x(2)-(exp(x(1)/2)+exp(-x(1)/2))/2
  y(2)=9*x(1)*x(1)+25*x(2)*x(2)-225
endfunction
//definição do valor inicial da solução
x0=[2.5;2.0];
//definição da tolerância
tol=5.0e-3;
//definição do número máximo de iterações
k_max=30;
//contador de iterações (valor inicial)
k=0;
//maior valor em delta_x inicial
delta_max=100;
printf("+++++ Início do processo iterativo +++++\n")
while(delta_max>tol & k<k_max)
//Cálculo da matriz Jacobiano em x0
  [H]=numderivative(funcao,x0)
//Cálculo do valor da função vetorial y em x0
  h=funcao(x0)
//Cálculo do vetor delta_x: solução de H*delta_x = - h(x)
  delta_x=inv(H)*(-h)
//Cálculo do valor máximo dentre os elementos do vetor delta_x
  delta_max=max(abs(delta_x));
//Novo valor de x
  x0=x0+delta_x
  printf("Iteração corrente %d \n",k)
  disp(x0)
  k=k+1
end
//Resultados
printf("===== RESULTADOS =====\n")
printf("número de iterações: %d \n", k)
printf("solução: \n")
disp(x0)
