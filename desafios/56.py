soma_idade = 0
nome_homem_mais_velho = ''
maior_idade = 0
mulher_menor_20 = 0

for i in range(4):
  nome = str(input('Digite seu nome: '))
  idade = int(input('Digite sua idade: '))
  sexo = str(input('Digite seu sexo: '))

  soma_idade += idade

  if sexo == 'Masculino':
    if idade > maior_idade:
      maior_idade = idade
      nome_homem_mais_velho = nome

  if sexo == 'Feminino':
    if idade < mulher_menor_20:
      mulher_menor_20 += 1

print(f'Media idade: {soma_idade / 4}')
print(f'Nome homem mais velho: {nome_homem_mais_velho}')
print(f'Total de mulheres menores de 20 anos: {mulher_menor_20}')
