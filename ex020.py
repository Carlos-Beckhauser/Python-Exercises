import random

aluno1 = input("Nome do 1º aluno: ")
aluno2 = input("Nome do 2º aluno: ")
aluno3 = input("Nome do 3º aluno: ")
aluno4 = input("Nome do 4º aluno: ")
grupo = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(grupo)
print_format = ", ".join(grupo)
print("O alunos do grupo são: {}, {}, {}, {}.".format(aluno1, aluno2, aluno3, aluno4))
print("-" * 30)
print("Foi sorteado a ordem que os alunos se apresentarão.\nA ordem é: {}".format(print_format))
