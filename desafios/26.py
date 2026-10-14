texto = input('Informe um texto para ser verificado: ')
appear_a = texto.upper().count('A')
first_position_a = texto.upper().index('A')
last_position_a = texto.upper().rindex('A')

print(f'Total de aparicoes de "A" no texto: {appear_a}')
print(f'Primeira aparicao de "A" no texto no indice: {first_position_a}')
print(f'Ultima aparicao de "A" no texto no indice: {last_position_a}')