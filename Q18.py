dias = ['Domingo', 'Segunda', 'Terça','Quarta', 'Quinta', 'Sexta','Sábado']
soma = 0
for i in range(len(dias)):
    vlr = float(input(f"Digite o valor arrecadado no(a) {dias[i]}: "))
    soma += vlr
print(f"O total arrecadado na semana é de R$ {soma:.2f}")