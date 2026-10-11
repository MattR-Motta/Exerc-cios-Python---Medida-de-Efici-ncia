temps = []

for i in range(1,6):
    temp = float(input(f"Digite a temperatura do {i}º dia: "))
    temps.append(temp)

media = sum(temps)/len(temps)
print(f"A média de temperatura é de {media}°")
if media > 18 and media < 28:
    print("A média de temperatura está dentro da faixa ideal de cultivo")
else:
    print("A média de temperatura não está dentro da faixa ideal de cultivo")
print(temps)