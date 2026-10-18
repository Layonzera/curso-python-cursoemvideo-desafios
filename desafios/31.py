d_viagem = float(input('Digite a ditancia de uma viagem em KM: '))

if d_viagem <= 200:
  print(f'Total a pagar: R${d_viagem * 0.50:.2f}')
else:
  print(f'Total a pagar: R${d_viagem * 0.45:.2f}')