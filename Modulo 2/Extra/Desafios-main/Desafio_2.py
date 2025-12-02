# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor:
# Exemplo:
# Você digitou o número : 10
# O sucessor dele é o número : 11
# O antecessor dele é o número : 9

numero = int(input("Digite um número inteiro: "))
sucessor = numero + 1
antecessor = numero - 1
print(f"O sucessor do numero escolhido: {numero} e o número sucessor é {sucessor} e o antecessor é {antecessor}")