ano_nascimento = int(input('Informe o ano do seu nascimento: '))

idade = 2026 - ano_nascimento

if idade > 18:
  print('Voce excedeu o tempo permitido para alistamento')
  print(f'Passou cerca de {idade - 18} anos para seu alistamento')
elif idade == 18:
  print(f'Ja esta na hora de se alistar')
else:
  print(f'Voce ainda esta muito novo para se alistar')
  print(f'Faltam cerca de {18 - idade} anos para se alistar')