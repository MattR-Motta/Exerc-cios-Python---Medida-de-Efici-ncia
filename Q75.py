def conectar():
    for i in range(1,4):
        try:
            print(f"{i}º tentativa de conectar com a API")
            raise ConnectionError("API indisponível")
        except ConnectionError as erro:
            print(f"Falha na conexão: {erro}")
    print("Limite de tentativas atingido, encerrando")
conectar()