import math
num = int(input("Digite um valor de Ângulo: "))
rad = math.radians(num)
cos = math.cos(rad)
sen = math.sin(rad)
tang = math.tan(rad)
print("O angulo digitado foi: {}".format(num))
print("-" * 20)
print("O cosseno deste angulo é: {:.2f}\nO seno desse angulo é: {:.2f}\nA tangente desse angulo é: {:.2f}".format(cos, sen, tang))
