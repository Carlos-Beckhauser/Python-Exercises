nome = input("Qual seu nome aluno ? \n")
nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
media = float((nota1+nota2)/2)
print("Seja bem-vindo", nome, "\nSua primeira nota foi:", nota1, "\nSua segunda nota foi:", nota2)
print()
print("Caro aluno {} \nSua media é: {}".format(nome, media))
