#Estruturas Sequenciais

idade=input("Informe sua idade:")                       #Entrada de dados
print(idade, type(idade))

idade=int(idade)                                        #Conversão do tipo de variável
print(idade, type(idade))                               #Better idade = int(input("Informe sua idade:"))

salario_mensal=input("Digite o seu salário mensal: ")
salario_mensal=float(salario_mensal)
gasto_mensal=input("Digite o total do seu gasto mensal:")
gasto_mensal=float(gasto_mensal)

salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12

montante_economizado = salario_total - gasto_total
print("O total que você pode economizar por ano é de: ", montante_economizado)