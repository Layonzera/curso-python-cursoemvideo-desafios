v_casa = float(input('Qual o valor da casa? '))
s_cliente = float(input('Qual o valor do seu salario? '))
a_pagar = int(input('Em quantos anos pretende pagar a casa? '))

p_mensal = v_casa / (a_pagar * 12)
minimo = s_cliente * 30 / 100

if p_mensal <= minimo:
  print('Emprestimo permitido')
else:
  print('Emprestimo negado')