vlrs = []
for i in range(12):
    vlr = float(input(f"Digite os gastos do {i+1}° mês do ano: "))
    vlrs.append(vlr)
print(f"O valor gasto anual é de R$ {sum(vlrs):.2f}")