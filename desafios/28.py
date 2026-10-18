import random

n_usuario = int(input('Digite um valor entre 0 e 5: '))
n_computador = random.randint(0, 5)

if n_usuario == n_computador:
  print(f'Numero do usuario: {n_usuario} \nNumero do computador: {n_computador} \nVOCE VENCEU!')
else:
  print('Numero do usuario: {n_usuario} \nNumero do computador: {n_computador} \nVOCE PERDEU!')
