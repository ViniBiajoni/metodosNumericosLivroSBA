#Programa do para a conversão de número binário em decimal


#Algotirmo Apresentado no livro (página 37) Ex:5 bits 11011  -> 27

#Lê Vetor Binario e Armazenar em uma Lista
num_bits = int(input("Digite o número bits do binário: ")) # Digitar o numero de bits
val_bin=[]                # Numero binário (armazenado em vetor)
for i in range(num_bits):
    bit = int(input(f"Digite o bit {str(i)} da esquerda para a direita: "))
    val_bin.append(bit)

#Realiza a Conversão
val_dec=[]
val_dec.append(val_bin[0])
for k in range(num_bits-1):
    val_dec.append(val_bin[k+1]+2*val_dec[k])

#Imprime o valor final na base decimal
print("Valor Decimal")
print(val_dec[num_bits-1])

