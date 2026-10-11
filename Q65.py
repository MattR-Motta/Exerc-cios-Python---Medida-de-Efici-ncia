def calcularCubo(x):
    return x ** 3
def calcularDivisaoCubo(y):
    if y % 3 == 0:
        return calcularCubo(y)
    else:
        return False
teste = int(input("Digite um número: "))
print(calcularDivisaoCubo(teste))