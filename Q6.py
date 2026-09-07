cod = int(input("Digite o código do equipamento: "))
if cod % 2 == 0:
    print("Número par, O equipamento pertence ao setor administrativo")
else: 
    print("Número ímpar, O equipamento pertence ao setor operacional")