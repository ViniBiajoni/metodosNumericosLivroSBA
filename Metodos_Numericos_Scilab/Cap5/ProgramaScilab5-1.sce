// definição das equações do sistema
function y=funcao(x)
  y(1)=x(2)-(exp(x(1)/2)+exp(-x(1)/2))/2
  y(2)=9*x(1)*x(1)+25*x(2)*x(2)-225
endfunction
//valor inicial da solução
x0=[2.5;2];
//solução do sistema
solucao=fsolve(x0,funcao)
disp(solucao)
