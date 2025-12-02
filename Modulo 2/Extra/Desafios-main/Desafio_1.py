# Faça um código que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input("Digite qual é o seu sálario: "))
# Exemplo de Resultado: O Seu salário atual é de R$1500,00 com o aumento de 15% seu novo salário será de R$1725,00
porcentagem = salario * 0.15
aumento = salario + porcentagem

print(f"Óla caro trabalhador, devido o seu esforço você conseguiu ser promovido na sua área e agora ira receber um sálario de : {aumento}")