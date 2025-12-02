# Na mesma linha dos exercicios anteriores crie uma função chamada pode_ver_filme que recebe a idade e a classificação indicativa do filme
# classificacao: 'L' (Livre), 'Maior de 12', 'Maior de 14', 'Maior 16', 'Maior 18'
idade = int(input("Digite sua idade: "))
classificacao = input("Digite a classificação: 'L', '12', '14', '16', '18': ")
def pode_ver_filme():
    if idade >= 0 and classificacao == "L":
        print("Pode assitir")
    elif idade >= classificacao:
        print("Pode assistir")
    else:
        print("Não pode assitir o filme")
pode_ver_filme()        
#Exemplo:
# idade = 10
# classificacao = 'Maior de 12'
# resposta = "Não pode assitir o filme"
