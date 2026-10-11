m = [[300,-50,500], [-79,-30,800]]
print(m[0][0],m[0][1],m[0][2])
print(m[1][0],m[1][1],m[1][2])
quantPositivos = 0
for i in m:
    for vlr in i:
        if vlr > 0:
            quantPositivos += 1

print(f"A quantidade de valores positivos nessa matriz é igual a: {quantPositivos}")