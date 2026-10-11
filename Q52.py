farmacia = {}
for i in range(5):
    med = input("Digite o nome do medicamento: ")
    quant = int(input("Digite a quantidade em estoque: "))
    farmacia[med] = quant
consulta = input("Digite o nome do medicamento que deseja consultar: ")
print(farmacia[consulta])