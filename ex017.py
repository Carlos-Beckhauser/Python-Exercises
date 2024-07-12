import math
cat_adj = float(input("Digite o valor do Cateto Adjacente: "))
cat_op = float(input("Digite o valor do Cateto Oposto: "))
calc = math.sqrt((cat_adj ** 2) + (cat_op ** 2))
print("O valor digitado do Cateto Adjacente é: {:.2f}\nO valor digitado do Cateto Oposto foi: {:.2f}".format(cat_adj, cat_op))
print("Com base nesses valores, o valor da Hipotenusa é: {:.2f}".format(calc))