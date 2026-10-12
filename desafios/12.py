p_produto = float(input('Informe o valor do produto: '))
d_produto = (p_produto * 5) / 100
v_desconto = p_produto - d_produto

print(f'Valor com desconto: R$ {v_desconto:.2f}')