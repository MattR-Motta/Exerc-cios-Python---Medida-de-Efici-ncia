precos = ['100','200','300']

for i in precos:
    try:
        vlr = float(i)
    except ValueError:
        print("Preço inválido")
    else:
        desconto = vlr * 0.10
        vlrFinal = vlr - desconto
        print(f"Preço normal: {vlr:.2f}")
        print(f"Preço com desconto: {vlrFinal:.2f}")
