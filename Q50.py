alunos = {}
for i in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

soma = 0
for vlrs in alunos.values():
    soma += vlrs
media = soma/len(alunos)
print(f'Média da turma: {media}')

for nome, nota in alunos.items():
    if nota >= 7:
        print(nome, "está aprovado") 