peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc =  peso / (altura ** 2)

if imc < 18.5:
  print(f'IMC: {imc}')
  print('ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
  print(f'IMC: {imc}')
  print('PESO IDEAL')
elif imc >= 25 and imc < 30:
  print(f'IMC: {imc}')
  print('SOBREPESO')
elif imc >= 30 and imc < 40:
  print(f'IMC: {imc}')
  print('OBESIDADE')
else:
  print(f'IMC: {imc}')
  print('OBESIDADE MORBIDA')