# Crie uma função chamada cumprimentar ela deve receber o nome e a hora, essa função deve gerar cumprimentos baseado no periodo do dia
# Periodos :    Manhã: 5 até 12, Tarde: 13 até 18, Noite: 18 até 24
nome = input("Digite seu nome: ")
horario = int(input("Digite o horario que você chegou: "))
def checagem():
    if horario >= 5 and horario <= 12:
        print(f"Nome: {nome}")
        print(f"Hora: {horario}")
        print(f"Bom Dia, {nome}")
    elif horario >= 13 and horario <= 18:
        print(f"Nome: {nome}")
        print(f"Hora: {horario}")
        print(f"Boa Tarde, {nome}")
    else:
        print(f"Nome: {nome}")
        print(f"Hora: {horario}")
        print(f"Boa Noite, {nome}")
checagem()
# Exemplo: 
# Nome: Allana
# Hora : 9
# Bom dia, Allana

# Exemplo2: 
# Nome: Gustavo B
# Hora : 15
# Boa Tarde, Gustavo B
