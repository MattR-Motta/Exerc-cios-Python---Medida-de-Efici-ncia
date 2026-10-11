vagas = [[1,0,1], [1,1,0], [0,1,1]]
print(vagas[0][0],vagas[0][1],vagas[0][2])
print(vagas[1][0],vagas[1][1],vagas[1][2])
print(vagas[2][0],vagas[2][1],vagas[2][2])
livres = 0
ocupadas = 0
for i in vagas:
    for x in i:
        if x == 0:
            livres += 1
        else:
            ocupadas += 1
print(f"Vagas Livres: {livres}")
print(f"Vagas Ocupadas: {ocupadas}")