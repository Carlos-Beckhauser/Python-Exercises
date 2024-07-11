preco = float(input("Qual é o preço do produto ? R$ "))
desc = preco - (preco * 0.05)
print("O valor do produto é R${:.2f}. Você tem 5% de desconto, "
      "então seu total a pagar é: R$ {:.2f}".format(preco, desc))
