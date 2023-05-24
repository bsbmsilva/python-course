# Manipulando listas
#Criando nova lista

nomes_paises = ["Brasil", "Argentina", "Colômbia", "Equador", "Chile"]
print('Lista nomes países original: ', nomes_paises)

print("Tamanho da lista: ", len(nomes_paises))
print('Formato da lista: ', type(nomes_paises))

#Alterar um item da lista

nomes_paises[2] = "Japão"
print('Alterando posição 2 para Japão: ', nomes_paises)

#Imprimir itens da lista

print('Imprimir do item 1 ao menor do que 4: ', nomes_paises[1:4])        #Imprimir do item 1 ao menor do que 4

print('Imprimir do início ao menor que 3: ', nomes_paises[:3])         #Imprimir do início ao menor que 3
print('Imprimir do item 2 ao final: ', nomes_paises[2:])         #Imprimir do item 2 ao final
print('Imprimir do início ao fim: ', nomes_paises[:])          #Imprimir do início ao fim

print('Imprimir do início ao fim pulando de 2 em 2: ', nomes_paises[::2])        #Imprimir do início ao fim pulando de 2 em 2
print('Imprimir do início ao fim na ordem inversa: ', nomes_paises[::-1])       #Imprimir do início ao fim na ordem inversa

#Função append - adiciona itens ao fim da lista

lista_capitais = []
lista_capitais.append("Brasília")
lista_capitais.append("São Paulo")
lista_capitais.append("Rio de Janeiro")
lista_capitais.append("João Pessoa")
lista_capitais.append("Recife")
lista_capitais.append("Fortaleza")
print('Lista Capitais, itens adicionados um por um: ', lista_capitais)

#Função insert - adiciona item em uma posição específica
##Observe que não sobrescreve, só desloca os outros itens

lista_capitais.insert(2, "Florianópolis")           #Inserir Florianópolis no item 2
print('Inserir Florianópolis no item 2: ', lista_capitais)

#Função remove - Remove um valor específico da lista
##Se esse valor aparecer mais de uma vez, remove o primeiro

lista_capitais.remove("Rio de Janeiro")
print('Remover Rio de Janeiro: ', lista_capitais)       #Remover Rio de Janeiro

#Função pop - remove o item de uma posição específica
##Se não for indicada a posição ele remove o primeiro item

lista_capitais.pop(1)                #Remover item da posição 1
print('Remover item da posição 1: ', lista_capitais)

# Criação de uma tupla

nomes_paises = ("Canadá", "Bogotá", "Finlândia", "Noruega")
print('Criação de uma tupla: ', nomes_paises)
print('Tamanho da tupla: ', len(nomes_paises))
print('Formato da tupla: ', type(nomes_paises))

#É mais fácil atribuir uma variável para cada item de uma tupla

c, b, f, n = nomes_paises
print('Primeiro e terceiro itens da tupla: ', c, f)