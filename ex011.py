a = float(input("Digite valor do Altura da parede: "))
b = float(input("Digite valor do Largura da parede: "))
area = a * b
tinta = area / 2
print("Sua parede tem Altura de {:.2f}cm e Largura de {:.2f}cm, e sua área é de: {:.2f}m², então precisa de {:.2f} Litros pra pintar sua parede".format(a, b, area, tinta))
