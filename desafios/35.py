r1 = int(input('Digite a primeira reta: '))
r2 = int(input('Digite a segunda reta: '))
r3 = int(input('Digite a terceira reta: '))

if(r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
  print(f'Reta 1: {r1}')
  print(f'Reta 2: {r2}')
  print(f'Reta 3: {r3}')
  print('Podem formar um triangulo')
else:
  print('Nao podem formar um triangulo')