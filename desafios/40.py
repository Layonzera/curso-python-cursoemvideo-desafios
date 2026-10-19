nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
  print('REPROVADO')
  print(f'Media: {media}')
elif media >= 5 and media <= 6.9:
  print('RECUPERACAO')
  print(f'Media: {media}')
else:
  print('APROVADO')
  print(f'Media: {media}')