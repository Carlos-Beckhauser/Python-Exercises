name = input("Digite seu nome completo: ").strip()
nameSplit = name.split()
print("Seu primeiro nome é: {}".format(nameSplit[0]))
print("Seu último nome é: {}".format(nameSplit[len(nameSplit)-1]))
