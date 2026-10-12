perfis = {'admin':['criar','visualizar','editar','excluir'], 'usuario':['criar','visualizar'], 'visitante':['visualizar']}
def permissoes(perfis, perfil, i):
    try:
        return perfis[perfil][i]
    except(KeyError, IndexError):
        return 'acesso_restrito'
print(permissoes(perfis, 'admin', 0))