valor = float(input("Digite um valor em Metros: "))
km = valor / 1000
hm = valor / 100
dam = valor / 10
dm = valor * 0.1
cm = valor * 0.01
mm = valor * 0.001
print()
print("----------------TABELA DE CONVERSÕES----------------")
print()
print("O valor digitado foi: {} Metros".format(valor))
print()
print("Confira suas conversões abaixo:")
print("{} Metros tem {} Kilometros".format(valor, km))
print("{} Metros tem {:.4f} Hectometros".format(valor, hm))
print("{} Metros tem {:.4f} Decametros".format(valor, dam))
print("{} Metros tem {:.4f} Decimetros".format(valor, dm))
print("{} Metros tem {:.4f} Centimetros".format(valor, cm))
print("{} Metros tem {} Milimetros".format(valor, mm))
