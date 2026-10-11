disciplinas = ('Matemática','Português')
alunos = {}
for i in range(3):
    nome = input("Digite o nome do aluno: ")
    notaMat = float(input("Digite a nota de matemática do aluno: "))
    notaPor = float(input("Digite a nota de português do aluno: "))
    alunos[nome] = {'Matemática':notaMat,'Português':notaPor}
print(alunos)

for nome, notas in alunos.items():
    media = (notas['Matemática']+notas['Português']) / 2
    if media >= 7:
        print(f'{nome}, média: {media}, está aprovado')
    else:
        print(f'{nome}, média: {media}, está reprovado')
print("\n",disciplinas)