soma = 0
num = float(input("Digite um número(digite 0 para sair): "))
while num != 0:
    soma += num
    num = float(input("Digite um número(digite 0 para sair): "))
print(f"A soma dos números digitados é: {soma}")