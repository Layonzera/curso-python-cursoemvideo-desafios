n_tabuada = int(input('Informe o valor para gerar a tabuada: '))

print(f'Tabuada do **{n_tabuada}**')
print('=' * 14)
for i in range(0, 11):
  print(f'{n_tabuada} x {i} = {n_tabuada * i}')