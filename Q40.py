import random

num = random.randint(1, 100)
tentativa = int(input("Digite um número entre 1 e 100: "))
while tentativa != num:
    if tentativa > num:
        print("O número é menor")
    else:
        print("O número é maior")
    tentativa = int(input("Digite um número entre 1 e 100: "))
if tentativa == num:
    print("Você acertou!")