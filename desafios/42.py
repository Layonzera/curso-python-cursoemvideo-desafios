r1 = int(input('Digite a primeira reta: '))
r2 = int(input('Digite a segunda reta: '))
r3 = int(input('Digite a terceira reta: '))

if(r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
  print(f'Reta 1: {r1}')
  print(f'Reta 2: {r2}')
  print(f'Reta 3: {r3}')
  print('Podem formar um triangulo')
  if r1 == r2 == r3:
    print('Triangulo Equilatero, todos os lados iguais')
  elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Triangulo Isosceles, dois lados iguais')
  else:
    print('Triangulo Escaleno, todos os lados diferentes')
else:
  print('Nao podem formar um triangulo')