# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
dias = float(input("Digite a quantidade de dias que você alugou o carro: "))
km = float(input("Digite a quantidade de km's rodados com o carro: "))
diaria = 50
total_dias = dias * diaria
total_km = km * 0.15
aluguel_total = total_dias + total_km

print(f"Você andou {km}km por 10 dias, entâo o preço a pagar é {aluguel_total}")