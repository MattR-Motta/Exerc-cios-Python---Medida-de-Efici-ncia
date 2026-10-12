def calcular_media(n1,n2,n3):
    notas = [n1,n2,n3]
    for i in notas:
        if i < 0 or i > 10:
            raise ValueError("As notas tem que estar entre 0 e 10")
    media = sum(notas)/3
    return media
try:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    media = calcular_media(n1,n2,n3)
    print(f"Média: {media}")
    if media >= 6:
        print("Aprovado")
    else:
        print("Reprovado")
except ValueError as erro:
    print(erro)
