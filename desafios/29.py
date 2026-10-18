km_total = float(input('Digite a velocidade do carro: '))

if km_total > 80:
  print('Voce foi multado!')
  print(f'Sua multa e de: R${(km_total - 80) * 7:.2f}')
else:
  print('Velocidade no limite permitido')
