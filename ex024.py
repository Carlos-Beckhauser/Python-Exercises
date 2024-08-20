nomeCidade = input("Digite sua cidade: ")
stringSplit = nomeCidade.split()
checkCidade = "Santo" in stringSplit[0]
print("O nome da sua cidade começa com 'Santo' ?\nR: {}".format(checkCidade))
