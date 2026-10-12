import traceback
dados = ['10','abcdefgh',7]
def processarDados(x):
    for i in dados:
        try:
            num = float(i)
            print(f"Valor processado: {num}")
        except(TypeError,ValueError):
            print(f"Erro ao processar o elemento: {i}")
            traceback.print_exc()
processarDados(dados)