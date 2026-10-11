m = [[300,400,500], [600,700,800]]
print(m[0][0],m[0][1],m[0][2])
print(m[1][0],m[1][1],m[1][2])
menor = min(min(i) for i in m)
print(f"O menor valor é: {menor}")