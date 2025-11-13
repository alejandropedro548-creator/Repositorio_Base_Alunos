# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

produto = "FIAT TORO"
preco = 200000
porcentagem_desconto = 15

valor_desconto = preco * (porcentagem_desconto / 100)
preco_final = preco - valor_desconto

print(f"Produto: {produto}")
print(f"Preço: R${preco}")
print(f"Porcentagem de desconto: {porcentagem_desconto}%")
print(f"O {produto} com {porcentagem_desconto}% de desconto custará R$ {preco_final}")