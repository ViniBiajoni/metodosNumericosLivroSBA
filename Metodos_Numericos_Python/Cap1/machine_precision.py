import numpy as np

#Precisão Máquina Pyhon (Biblioteca Numpy)
print("Float:\n")
print(np.finfo(float).eps)
print('\n')

print("Float 32 bits:\n")
print(np.finfo(np.float32).eps)
print('\n')

print("Float 64 bits:\n")
print(np.finfo(np.float64).eps)
print('\n')

#Precisão Máquina Algoritmo
u = 1.0

while 1.0 + u != 1.0:
    u = 0.5*u #potências de 2 (2^-n) -> rápido decaimento
    print(f'Valor atual = {1.0 + u}\n')
u = 2*u
print("Zero da Máquina(Algoritmo):\n")
print(u)
print("finish")
