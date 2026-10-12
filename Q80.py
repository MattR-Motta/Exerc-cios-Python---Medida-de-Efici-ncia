class ProdutoInvalidoError(Exception):
    pass
class ValorInvalidoError(Exception):
    pass
class QuantidadeinvalidaError(Exception):
    pass

def registrar_venda(produto, preco, quantidade):
    if not produto.strip():
        raise ProdutoInvalidoError("O produto não pode ser vazio")
    if preco <= 0:
        raise ValorInvalidoError("O preço tem que ser maior que zero")
    if quantidade < 0:
        raise QuantidadeinvalidaError("A quantidade tem que ser maior que zero")
    return {'produto': produto,'quantidade':quantidade,'total':preco*quantidade}

def gerar_relatorio(vendas):
    if not vendas:
        print("nenhuma venda registrada")
        return
    total = sum(i['total'] for i in vendas)
    produtos = {}

    for i in vendas:
        produtos[i['produto']] = (produtos.get(i['produto'], 0) + i['quantidade'])
    print(f"Total de vendas: {len(vendas)}")
    print(f"Produto mais vendido: {max(produtos, key=produtos.get)}")
    print(f"Faturamento: R${total:.2f}")
    print(f"Ticket médio: R${total/len(vendas):.2f}")
vendas = []

while True:
    produto = input("Nome do produto (ou fim para encerrar): ")
    if produto.lower() == 'fim':
        break

    try:
        preco = float(input("Digite o preço do produto: "))
        quant = int(input("Digite a quantidade do produto: "))
        venda = registrar_venda(produto,preco,quant)
    except(ValueError, ProdutoInvalidoError, ValorInvalidoError, QuantidadeinvalidaError) as erro:
        print(f"Erro: {erro}")
        with open("log_erros.txt", "a", encoding="utf-8") as arq:
            arq.write(str(erro)+'\n')
    else:
        vendas.append(venda)
        print("Venda registrada")
        try:
            with open("vendas.txt", "a", encoding="utf-8") as arq:
                arq.write(str(venda)+'\n')
        except OSError as erro:
            print(f"erro na hora de registrar a venda: {erro}")
    finally:
        print("Cadastro realizado")
gerar_relatorio(vendas)
