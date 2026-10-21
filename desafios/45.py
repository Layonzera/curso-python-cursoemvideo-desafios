import random

# jokenpo_list = ['Pedra', 'Papel', 'Tesoura']
jokenpo_choice_computer = 'Tesoura'
jokenpo_user = input('Pedra, Papel ou Tesoura? ')
jokenpo_computador = random.choice(jokenpo_choice_computer)

if jokenpo_user == 'Pedra' or jokenpo_user == 'Papel' or jokenpo_user == 'Tesoura':
  if jokenpo_user == 'Pedra' and jokenpo_choice_computer == 'Pedra':
    print(f'Usuario jogou: {jokenpo_user}')
    print(f'Computador jogou: {jokenpo_choice_computer}')
    print(f'EMPATE!')
  elif jokenpo_user == 'Papel' and jokenpo_choice_computer == 'Pedra':
    print(f'Usuario jogou: {jokenpo_user}')
    print(f'Computador jogou: {jokenpo_choice_computer}')
    print(f'VENCEDOR: Usuario!')
  elif jokenpo_user == 'Tesoura' and jokenpo_choice_computer == 'Pedra':
    print(f'Usuario jogou: {jokenpo_user}')
    print(f'Computador jogou: {jokenpo_choice_computer}')
    print(f'VENCEDOR: Computador!')
  elif jokenpo_user == 'Pedra' and jokenpo_choice_computer == 'Papel':
    print(f'Usuario jogou: {jokenpo_user}')
    print(f'Computador jogou: {jokenpo_choice_computer}')
    print(f'VENCEDOR: Computador!')
  elif jokenpo_user == 'Papel' and jokenpo_choice_computer == 'Papel':
    print(f'Usuario jogou: {jokenpo_user}')
    print(f'Computador jogou: {jokenpo_choice_computer}')
    print(f'EMPATE!')
  elif jokenpo_user == 'Tesoura' and jokenpo_choice_computer == 'Papel':
    print(f'Usuario jogou: {jokenpo_user}')
    print(f'Computador jogou: {jokenpo_choice_computer}')
    print(f'VENCEDOR: Usuario!')
  elif jokenpo_user == 'Pedra' and jokenpo_choice_computer == 'Tesoura':
    print(f'Usuario jogou: {jokenpo_user}')
    print(f'Computador jogou: {jokenpo_choice_computer}')
    print(f'VENCEDOR: Usuario!')
  elif jokenpo_user == 'Papel' and jokenpo_choice_computer == 'Tesoura':
    print(f'Usuario jogou: {jokenpo_user}')
    print(f'Computador jogou: {jokenpo_choice_computer}')
    print(f'VENCEDOR: Computador!')
  else:
    print(f'Usuario jogou: {jokenpo_user}')
    print(f'Computador jogou: {jokenpo_choice_computer}')
    print(f'EMPATE!')
else:
  print('Somente pode jogar PEDRA, PAPEL ou TESOURA!')
