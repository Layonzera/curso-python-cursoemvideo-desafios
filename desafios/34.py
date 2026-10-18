s_funcionario = float(input('Digite seu salario: '))

if s_funcionario > 1250:
  print(f'Salario atualizado com 10%: R${((s_funcionario * 10) / 100) + s_funcionario:.2f}')
else:
  print(f'Salario atualizado com 15%: R${((s_funcionario * 15) / 100) + s_funcionario:.2f}')