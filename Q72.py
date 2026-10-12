def parse_cpf(cpf):
    if not cpf.isdigit() or len(cpf) != 11:
        raise ValueError("CPF no formato errado")
    return cpf

def main():
    cpf = input("Digite seu cpf: ")
    try:
        resultado = parse_cpf(cpf)
        print("CPF válido")
    except ValueError as erro:
        print(f"Erro: {erro}")
main()