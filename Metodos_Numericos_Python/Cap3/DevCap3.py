
import sympy as sym
import numpy as np

#y = (5-x*m.exp(0.5*x))/1.2
#y  = 5/(m.exp(0.5*x + 1.2))
#y = (5 - 1.2*x)/(m.exp(0.5*x))

print('Derivada Ex 3')
x = sym.symbols('x')
print(sym.diff(x*sym.exp(0.5*x)  + 1.2*x -5))

print('1.1')
print(sym.diff((5-x*sym.exp(0.5*x))/1.2))

print('1.2')
print(sym.diff(5/(sym.exp(0.5*x)+1.2)))

print('1.3')
print(sym.diff((5-1.2*x)/(sym.exp(0.5*x))))

# print('ex 3')
# x = sym.symbols('x')
# print('   df/dx:')
# print(sym.diff(2*x**3 +sym.ln(x)-5))

print('5')
print(sym.diff((x**2)/2 +x*(sym.ln(x)-1)))

print('7')
print(sym.diff(x*(sym.cosh(200/x))))

print('9')
print(sym.diff(x**3 - 5*sym.sin(x)))

print('10')
print(sym.diff((sym.sin(x)**3)*(x-sym.sin(x)*sym.cos(x))-1))