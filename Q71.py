class SaldoInsuficienteError(Exception):
    pass
def sacar(saldo,vlr):
    if saldo < vlr:
        raise SaldoInsuficienteError("Saldo insuficente para realizar o saque")
    saldo -= vlr
    return saldo
print("Seu saldo é de R$ 1000.00")
valor = float(input("Digite o valor que deseja sacar da sua conta: "))
print(sacar(1000,valor))