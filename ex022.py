nome = input("Digite seu nome completo: ")
up = nome.upper()
low = nome.lower()
lista_strings = nome.split()  # Essa linha é pra transformar o Input de uma única string para uma lista de Strings
limpar_espacos = "".join(lista_strings)  # Esse comando é pra limpar espaços entre as strings
total_carac = len(limpar_espacos)  # Esse comando é pra contar numero de caracteres da variavel
total_string1 = len(lista_strings[0])  # Contar caracteres da primeira string
print("O nome com tudo em maiúsculo: {}".format(up))
print("o nome com tudo em minusculo: {}".format(low))
print("Removendo os espaços, o nome digitado tem: {} caracteres".format(total_carac))
print("O primeiro nome digitado tem: {} caracteres".format(total_string1))
