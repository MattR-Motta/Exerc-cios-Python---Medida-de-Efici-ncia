def realizar_saque(saldo,valor_saque):
    if valor_saque <= 0:
        raise ValueError("O valor do saque tem que ser positivo")
    if valor_saque > saldo:
        raise Exception("Saldo insuficiente")
    novoSaldo = saldo - valor_saque
    return novoSaldo
try:
    saldo = 1000
    print(f"Saldo: {saldo:.2f}")
    vlrSaque = float(input("Dugite o valor que deseja sacar:"))
    print(realizar_saque(saldo,vlrSaque))
except ValueError as erro:
    print(erro)
except Exception as erro:
    print(erro)