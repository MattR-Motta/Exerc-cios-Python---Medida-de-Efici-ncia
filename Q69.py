try:
    arquivo = open("relatorio_vendas.txt", "r")
    print(arquivo.read())
except FileNotFoundError:
    print("O arquivo não foi encontrado")
finally:
    print("Encerrando")
