pessoas_menores_de_idade = 0
pessoas_maiores_de_idade = 0

for i in range(7):
  pessoa_idade = int(input('Informe sua idade: '))
  if not pessoa_idade >= 21:
    pessoas_menores_de_idade += 1
  else:
    pessoas_maiores_de_idade += 1

print(f'Menores de idade: {pessoas_menores_de_idade}')
print(f'Maiores de idade: {pessoas_maiores_de_idade}')