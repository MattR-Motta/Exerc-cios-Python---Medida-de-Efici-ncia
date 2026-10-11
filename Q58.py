def gorjeta(a):
    total = a*1.10
    valor = total-a
    print(f"O valor da gorjeta é de: R${valor:.2f}")
vlr = float(input("Digite o valor da conta para saber o valor da gorjeta do garçom: "))
gorjeta(vlr)
