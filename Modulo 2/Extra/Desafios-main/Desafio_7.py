# Crie uma função que calcule o valor da gorjeta de um garçom, baseada na qualidade do serviço
# qualidade_servico: 'ruim', 'medio', 'bom', 'excelente'
valor_conta = float(input("Digite o valor da conta: "))
avaliacao = input("Digite a qualidade do serviço; 'ruim', 'medio', 'bom', 'excelente',: ")
def gorjeta(valor_conta,avaliacao):
    if avaliacao == "ruim":
        print(f"O valor da conta é: {valor_conta}")
        print(f"A qualidade do serviço é: {avaliacao}")
        print(f"O valor da gorjeta é: R${valor_conta * 0}")
    elif avaliacao == "medio":
        print(f"O valor da conta é: {valor_conta}")
        print(f"A qualidade do serviço é: {avaliacao}")
        print(f"O valor da gorjeta é: R${valor_conta * 2.5}")
    elif avaliacao == "bom":
        print(f"O valor da conta é: {valor_conta}")
        print(f"A qualidade do serviço é: {avaliacao}")
        print(f"O valor da gorjeta é: R${valor_conta * 4.0}")
    elif avaliacao == "excelente":
        print(f"O valor da conta é: {valor_conta}")
        print(f"A qualidade do serviço é: {avaliacao}")
        print(f"O valor da gorjeta é: R${valor_conta * 5.0} ")   
    else: 
        print("Avaliação Inválida")
# A função deve pedir o valor da conta e a qualidade do serviço
# Se a qualidade for ruim a gorjeta é 0
# Se a qualidade for media a gorjeta é %2.5 do valor da conta
#Se a qualidade for bom a gorjeta é %4 do valor da conta
#Se a qualidade for excelente a gorjeta é %5 do valor da conta

#Exemplo:
# valor_conta = 100
# qualidade_servico = 'excelente'
# o valor da gorjeta é de R$ 5,00
gorjeta(valor_conta, avaliacao)