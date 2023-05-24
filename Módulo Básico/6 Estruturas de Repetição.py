#Estruturas de Repetição
    #While - Contando quantos itens serão lavados em uma louça
'''
contador = 0
x = int(input('Quantos itens há para serem lavados?'))

while contador < x:
    contador = contador + 1
    if contador == 1:
        print(contador, "item limpo")
    else:
        print(contador, "itens limpos")
print("Fim da lavagem de louça\n")

#Utilizando break para finalizar o loop
print('Mesmo programa, utilizando break para finalizar o loop:')

contador = 0

while True:                                     #Programa ficará preso no while até o break
    if contador < x:
        contador = contador + 1
        if contador == 1:
            print(contador, "item limpo")
        else:
            print(contador, "itens limpos")
    else:
        break                                   #Fim do loop
        
print("Fim do loop")'''

#Estruturas de repetição
    #For - Calculando a médi de três notas

'''for variavel in range(5): #A função range vai de 0 até menor que 5
    print(variavel)

for variavel in range(1, 6): #Nesse caso range irá de 1 até menor que 6
    print(variavel)

for variavel in range(1, 11, 3): #Nesse caso range irá de 1 até menor que 11, mas em passos de 3
    print(variavel)'''

soma = 0

for i in range(1,4):
    nota = float(input(f'Informe a nota {i}: '))

    soma = soma + nota

media = soma / 3

print(f'A sua média é {media}')