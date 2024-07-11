dia = int(input("Por quantos dias você alugou o carro ? "))
km = float(input("Quantos Km você percorreu com o carro ? "))

alugar_dia = dia * 60
alugar_km = km * 0.15
total = alugar_km + alugar_dia

print("Você alugou por {} dias, e percorreu {} Km".format(dia, km))
print("O total a pagar é: R$ {:.2f}".format(total))