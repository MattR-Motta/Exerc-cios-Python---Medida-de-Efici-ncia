import random 

num = random.randint(1, 10)
tentativa = int(input("Digite um número entre 1 e 10: "))

if tentativa == num:
    print("Parabéns! Você acertou!")
else:
    print("Você errou! O número certo era: ", num)