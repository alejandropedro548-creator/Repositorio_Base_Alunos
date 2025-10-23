# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

soma = nota1 + nota2 + nota3

media = soma / 3

print("| ______________________________ |")
print("| SISTEMA DE PROVAS")
print("| ______________________________ |")
print(f"| Nome do aluno: {nome}")
print(f"Nota da primeira prova: {nota1}")
print(f"Nota da segunda prova: {nota2}")
print(f"Nota da terceira prova: {nota3}")
print("| ______________________________ |")
print(f"| Aluno: {nome} ")
print(f"| Média: {media}")
print("| Aluno aprovado")
print("| ______________________________ |")