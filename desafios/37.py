n = int(input('Digite o valor inteiro: '))
print('1 - para binario')
print('2 - para octal')
print('3 - para hexadecimal')
opcao = int(input('Informe a opcao desejada para converter o numero digitado: '))

if opcao == 1 or opcao == 2 or opcao == 3:
  if opcao == 1:
    print(f'{n} convertido para binario: {bin(n)[2:]}')
  elif opcao == 2:
    print(f'{n} convertido para octal: {oct(n)[2:]}')
  else:
    print(f'{n} convertido para hexadecimal: {hex(n)[2:]}')
else:
  print('Por favor, selecione uma opcao disponivel.')