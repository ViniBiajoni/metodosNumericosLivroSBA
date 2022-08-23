#Programa do para a Conversão de número decimal em binário

#Algotirmo Apresentado no livro (página 39) Ex: 187 -> 10111011

#Entrar com Número decimal
dec_val = int(input("Digite o valor do número decimal: "))
# Inicializar Lista Binaria
bin_val = []
resto_ant = 0
it = 0
while dec_val != 0:
    
    #Descobre os algarismos do resultado binário
    resto = dec_val % 2
    print(f'b{it} = ({dec_val+resto_ant}-{resto_ant})/2 = {resto}')
    resto_ant = resto
    it+=1
    if resto == 0:
        bin_val.append(0)
    else:
        bin_val.append(1)

    #Armazena o quociente da divisão por 2
    dec_val = dec_val//2 

# Inverte o vetor para obtenção da forma correta
bin_val = bin_val[::-1]
print("O valor binário é:")
print(bin_val)