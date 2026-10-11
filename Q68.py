while True:
    try:
        quant = int(input("Digite a quantidade de acionistas: "))
        lucro = float(input("Digite o lucro deste trimestre: "))
        divisao = lucro/quant
    except ValueError:
        print("Digite apenas números")
    except ZeroDivisionError:
        print("Não é possível dividir nada por zero")
    if quant > 0 and lucro > 0:
        print(f"A divisão dos lucros fica: R${divisao:.2f} pra cada")
        break
