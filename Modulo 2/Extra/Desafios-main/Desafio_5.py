# Agora vamos dar uma relembrada na aula de funções, pegue o código do exercicio anterior e transfome numa função,
# essa função deve receber uma lista e dessa lista escolher algum nome e dar um print
# ou seja vocês vão precisar criar a função e depois "chamar" a mesma para que ela execute.
from random import choice
nomes = ["Miguel", "Kaio", "Leonardo", "Gustavo A"]
alunos = ["Motoboy", "Kaio", "Leonardo", "Alejandro"]
def ajudeorian(lista):
    '''
    Essa função escolhe um aluno, para ajudar.
    
    '''
    escolhido = choice(lista)
    print(f"O aluno da vez será o {escolhido}, Boa sorte!")

ajudeorian(lista=nomes)
ajudeorian(alunos)
