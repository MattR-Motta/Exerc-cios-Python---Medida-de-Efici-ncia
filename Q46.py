m = [[300,400,500], [600,700,800], [100,200,900]]
print(m[0][0],m[0][1],m[0][2])
print(m[1][0],m[1][1],m[1][2])
print(m[2][0],m[2][1],m[2][2])

diagonalPrincipal = []
print("\nOs números da diagonal principal são: ")
for i in range(len(m)):
    print(m[i][i])
    diagonalPrincipal.append(m[i][i])
print(f'A soma dos números da diagonal principal é igual a: {sum(diagonalPrincipal)}')