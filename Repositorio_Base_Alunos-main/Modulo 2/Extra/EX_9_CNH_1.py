# Escreva um programa simples que pede a idade do usuário e 
# depois mostre na tela com valor BOOLEANO (True ou False) se o usuário pode tirar a CNH (Carteira Nacional de Habilitação) ou não.
# Para tirar carteira no Brasil, a idade mínima é 18 anos.

# OUTPUT ESPERADO:
# Exemplo 1:

# Digite sua idade: 19
# Pode tirar carteira de motorista? True

# Exemplo 2:
# Digite sua idade: 17
# Pode tirar carteira de motorista? False

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

idade = int(input('Digite a sua idade: '))

if idade >= 18:
    maior_idade = True
    print(f"Pode tirar carteira de habilitaçâo? {maior_idade}")
else:
    maior_idade = False
    print(f"Não pode tirar carteira de habilitaçâo? {maior_idade}")