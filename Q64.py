def soma(a,b,c):
    total = a+b+c
    if total <= 21:
        return total
    elif total > 21 and (a == 11 or b == 11 or c == 11):
        total = total - 10
    if total > 21:
        return -1
    return total
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
print(soma(n1,n2,n3))