ano_atual = int(input('Informe o ano: '))

if (ano_atual % 4 == 0 and ano_atual % 100 != 0) or (ano_atual % 400 == 0):
  print('Ano bissexto')
else:
  print('Ano nao bissexto')