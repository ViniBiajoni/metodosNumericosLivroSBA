#Programa do para converter número binário fracionário para decimal

#Algotirmo Apresentado no livro (texto página 42) Ex: 6 bits .101101 -> 0.703125
#  

#Lê Vetor Binario e Armazenar em uma Lista
num_bits = int(input("Digite o número de bits após a vírgula do binário: ")) # Digitar o numero de bits
val_bin=[] # Numero binário (armazenado em vetor)
val_dec=0.0
for i in range(num_bits):
    bit = int(input(f"Digite o bit {str(i)} da esquerda para a direita: "))
    val_bin.append(bit)
    val_dec = val_dec + float(bit*(2**(-(i+1))))

print("O valor em decimal é:")
print(val_dec)
