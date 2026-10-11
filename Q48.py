m = []
for i in range(3):
    linha = []
    for x in range(3):
        if i == x:
            linha.append(1)
        else:
            linha.append(0)
    m.append(linha)
print(m)