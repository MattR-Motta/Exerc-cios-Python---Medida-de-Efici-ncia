while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade > 0:
            break
        else:
            print("Digite um número maior que 0")
    except ValueError:
        print("Digite um número")