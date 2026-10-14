nome = input('Informe seu nome completo: ')
quebra_nome = nome.split()
primeiro_nome = quebra_nome[0]
ultimo_nome = quebra_nome[-1]

print(f'Nome completo: {nome}')
print(f'Primeiro nome: {primeiro_nome}')
print(f'Ultimo nome: {ultimo_nome}')