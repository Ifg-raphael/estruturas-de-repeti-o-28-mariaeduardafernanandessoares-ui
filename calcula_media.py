#entrada do usuário como uma única linha de texto
entrada_texto = input("Digite os números separados por espaço: ")

#Separa a string em uma lista de strings.
numeros_em_texto = entrada_texto.split()

#Converte cada string da lista para um número float
numeros_da_media = [] #lista
for numero_texto in numeros_em_texto: #pra cada elemento em numero_em_texto o for vai realizar a tarefa
    numero_real = float(numero_texto) #conversão armazenando cada elemento em numero_real
    numeros_da_media.append(numero_real) #adicionando os numeros a lista

# Passo 4: Usa as funções sum(), para somar os elementos da lista e len() para contar os elementos
soma = sum(numeros_da_media)
quantidade = len(numeros_da_media)

# Calcula a média e imprime o resultado
media = soma / quantidade
print(f"{media}")
