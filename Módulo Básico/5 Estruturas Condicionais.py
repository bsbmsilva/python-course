#Estruturas condicionais
    # Verificando qual o mais vantajoso, pagar 5 passagens para 5 pessoas ou uma corrida

valor_passagem = 4.3
valor_corrida = input("Qual o valor da corrida?")

if float(valor_corrida) > 5*valor_passagem:
    print("Pegue o ônibus")
if float (valor_corrida)<= 5*valor_passagem:
    print("Pague a corrida")

#Utilizando else
print('Mesmo problema utilizando if e else')

if float(valor_corrida) > 5*valor_passagem:
    print("Pegue o ônibus")
else:
    print("Pague a corrida")

#Utilizando If dentro do else
print('Mesmo problema utilizando mais opçoes, com if dentro do else')

if float(valor_corrida) <= 5*valor_passagem:
    print("Pague a corrida")
else:
    if float(valor_corrida) <= 6*valor_passagem:
        print("Aguarde um pouco, o valor da corrida pode baixar")
    else:
        print("Pegue o ônibus")

#Utilizando elif
print('Mesmo caso anterior, utilizando elif')

if float(valor_corrida) <= 5*valor_passagem:
    print("Pague a corrida")
elif float(valor_corrida) <= 6*valor_passagem:
    print("Aguarde um pouco, o valor da corrida pode baixar")
else:
    print("Pegue o ônibus")
