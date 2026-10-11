num = int(input("Digite um número: "))
soma = 0
for i in range(1,num):
    if num % i == 0:
        soma += i

if soma == num:
    print("É um número perfeito")
else:
    print("Não é um número perfeito")