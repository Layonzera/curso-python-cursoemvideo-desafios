ano_nascimento = int(input('Informe o ano de nascimento: '))
idade = 2026 - ano_nascimento

if idade <= 9:
  print(f'Idade {idade}')
  print('MIRIM')
elif idade <= 14:
  print(f'Idade {idade}')
  print('INFANTIL')
elif idade <= 19:
  print(f'Idade: {idade}')
  print('JUNIOR')
elif idade <= 20:
  print(f'Idade: {idade}')
  print('SENIOR')
else:
  print(f'Idade: {idade}')
  print('MASTER')