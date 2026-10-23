palavra = str(input('Digite uma palavra para verificar se e palindromo: '))
palavra_invertida = ''

for letra in palavra:
  palavra_invertida += letra

if palavra == palavra_invertida:
  print('E um palindromo')
else:
  print('Nao e um palindromo')