frase = str(input("Digite uma frase: ")).lower().strip()
print("A letra 'a' aparece quantas vezes ? \nR: {} vezes".format(frase.count('a')))
print("Em qual posição o 'A' aparece primeira vez? \nR: Posição {}".format(frase.find("a")))
print("Em qual posição o 'A' aparece última vez? \nR: Posição {}".format(frase.rfind("a")))
