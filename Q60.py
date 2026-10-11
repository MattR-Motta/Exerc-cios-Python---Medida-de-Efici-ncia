def conversaoTemp(x):
    c = (5/9) * (x-32)
    print(f"A conversão de {x}°F para °C foi de: {c}°C")
f = float(input("Digite a temperatura em °F para converter para °C: "))
conversaoTemp(f)