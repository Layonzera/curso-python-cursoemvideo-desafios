preco_produto = float(input('Digite o valor do produto: '))

print('1 - a vista dinheiro/cheque 10% desconto')
print('2 - a vista no cartao 5% desconto')
print('3 - 2x no cartao')
print('3x ou mais no cartao + 20% juros')
condicao_pagamento = int(input('Informe a opcao de pagamento: '))

if condicao_pagamento == 1:
  print(f'Valor total a pagar: R$ {preco_produto - (preco_produto * 10 / 100):.2f}')
elif condicao_pagamento == 2:
  print(f'Valor total a pagar: R$ {preco_produto - (preco_produto * 5 / 100):.2f}')
elif condicao_pagamento == 3:
  print(f'Valor total a pagar: R$ {preco_produto:.2f}')
else:
  print(f'Valor total a pagar: R$ {preco_produto + (preco_produto * 20 / 100):.2f}')