setoresProd = [[300,400,500], [600,700,800]]
print(setoresProd[0][0],setoresProd[0][1],setoresProd[0][2])
print(setoresProd[1][0],setoresProd[1][1],setoresProd[1][2])
total = 0
for i in setoresProd:
    for vlr in i:
        total += vlr

print(f"A soma dos valores da matriz de produção dos setores é igual a: {total}")