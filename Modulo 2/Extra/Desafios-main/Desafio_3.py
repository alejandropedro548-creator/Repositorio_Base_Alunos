# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada
# Exemplo:
# Você digitou o número : 10
# --------------- Tabuada do 10 ------------------
# 10 X 0 = 0
# 10 X 1 = 10
# E assim sucessivamente....
numero = int(input("Digite um número: "))
print(f"Você digitou o numero: {numero}")
print(f" --------------- Tabuada do {numero} ------------------")
for i in range(11):
    print(f"{numero} X {i} = {numero * i}")