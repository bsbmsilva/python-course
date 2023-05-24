#Manipulando Strings

frase = "Só há um deus: \"a Morte\"" #Contra barra transforma o próximo elemento em um caractere
print('Imprimindo uma string: ', frase)

#Imprimir pedaços específicos de uma string

print('Item 3 da str: ', frase[3])
print('Impressão do início ao item 5: ', frase[:5])

#Função split - separa itens de uma str
nomes_cidades = "Brasília, São Paulo, Salvador, Florianópolis"
print('Imprimindo uma str: ', nomes_cidades)
print(type(nomes_cidades))
nomes_cidades = nomes_cidades.split(", ") #split separa a string em uma lista, dividida em ', '
print('Transformando str em lista: ', nomes_cidades)
print(type(nomes_cidades))

#Função strip - elimina espaços vazios de um str

cabecalho = "              Menu Principal             "
print(cabecalho)
print(cabecalho.strip()) #strip retira os espaços

#Funções para alternar entre maiúsculas e minúsculas

nome_cidade = "RiO DE jAneIRo"

print(nome_cidade)
print(nome_cidade.title())          #Somente primeira letra de cada palavra maiúscula
print(nome_cidade.capitalize())     #Somente primeira letra da sentença maiúscula
print(nome_cidade.lower())          #Tudo minúsculo
print(nome_cidade.upper())          #Tudo maiúsculo

#Algoritmo para evitar erros de leitura em str digitada

nome_cidade = input("Qual o nome da cidade brasileira conhecida como cidade maravilhosa?")
nome_cidade = nome_cidade.strip()

while nome_cidade.lower() != 'rio de janeiro':
    print("Tente novamente")
    nome_cidade = input("Qual o nome da cidade brasileira conhecida como cidade maravilhosa?")
    nome_cidade = nome_cidade.strip()

print("Booa, campeão")

#Verificar trecho de str

mensagem = "Você viu o que o Pietro disse na sala ontem?"
fui_citado = "Pietro" in mensagem #Verifica se há Pietro na mensagem
print(fui_citado)