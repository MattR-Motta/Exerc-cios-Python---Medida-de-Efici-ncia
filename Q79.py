def cadastrar_produto(nome, preco, quantidade):
    if not nome.strip():
        raise ValueError("O nome não pode ser vazio")
    if preco <= 0:
        raise ValueError("O preço tem que ser maior que zero")
    if quantidade < 0:
        raise ValueError("A quantidade tem que ser maior que zero")
    return "Produto cadastrado com sucesso"
try:
    nome = input("digite o nome do produto: ")
    preco = float(input("digite o preço do produto: "))
    quant = int(input("Digite a quantidade do produto: "))
    print(cadastrar_produto(nome,preco,quant))
except ValueError as erro:
    print(f"Erro ao cadastrar o produto: {erro}")