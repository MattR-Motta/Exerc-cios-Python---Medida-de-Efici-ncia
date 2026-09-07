soma = 0
for i in range(10):
    vlr = float(input("Digite o valor da sua cesta básica: "))
    soma += vlr
print(f"O total arrecadado nas cestas básicas é de R$ {soma:.2f}")