#Listas

#Criar listas vazias

lista = []
lista = list()

#Uma lista permite diferentes tipos de dados

lista = [32, 'Michel', 3.14, True]
lista_de_listas = [10, [1,2,3]]

#Indexação

for i in lista:
    print(i, type(i))

#Slices

print(lista[0:2])           #Imprime do item 0 até menor que 2
#lista[3:]  Imprime do item 3 até o final
#lista[2:20:2]  Imprime do item 2 até menor que 20, pulando de dois em dois

#Imprimindo o comprimento da lista
print(len(lista))

#Outra forma de imprimir a lista

for i in range(len(lista)):
    print(f'Elemento {i} da lista: ', lista[i])