qtd_dias_alugado = int(input('Informe os dias que o carro foi alugado: '))
qtd_km_percorrido = float(input('Informe a quilometragem total percorrida: '))
vt_dias_alugado = qtd_dias_alugado * 60
vt_km_percorrido = qtd_km_percorrido * 0.15
valor_aluguel_total = vt_dias_alugado + vt_km_percorrido

print(f'Valor total do aluguel com a quilometragem e de: R$ {valor_aluguel_total:.2f}')