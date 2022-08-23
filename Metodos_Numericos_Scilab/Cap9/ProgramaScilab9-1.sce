//Programa para resolver uma EDO
clc         // limpa o console
clear all   // limpa a memória
funcprot(0);
//definição da função externa (lado direito da EDO)
function ydot=f(t, y)
  ydot=[150-y]/200
endfunction
t0=0;       //tempo inicial
y0=20;      //valor inicial da função y(t)
t=0         //variável independente no intervalo [0;30]
i=1         //contador
while t<=30
    y=ode(y0,t0,t,f);
    y1(i)=y;
    t1(i)=t
    printf('quantidade de sal (kg)')
    disp(y)
    printf('tempo (min)')
    disp(t)
    t=t+1
    i=i+1
    printf('---------------------------------------------------- \n')
end
printf("FIM ======\n")
