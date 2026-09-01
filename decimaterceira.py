consumo1 = float(input("Digite o consumo de energia do setor 1: "))
consumo2 = float(input("Digite o consumo de energia do setor 2: "))
if consumo1 > consumo2:
    print(f"O maior valor registrado foi {consumo1}, no setor 1")
else:
    print(f"O maior valor registrado foi {consumo2}, no setor 2")