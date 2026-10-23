numero_primo = int(input('Informe o numero para verificar se e primo: '))
mult = 0

for i in range(2, numero_primo):
  if numero_primo % 2 == 0:
    print(f'Multiplo de {i}')
    mult += 1

if mult == 0:
  print('E primo')
else:
  print('Nao e primo')