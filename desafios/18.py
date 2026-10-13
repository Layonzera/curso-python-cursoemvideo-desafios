import math
angulo = int(input('Digite o angulo: '))
radiano = math.radians(angulo)
seno_angulo = math.sin(radiano)
cosseno_angulo = math.cos(radiano)
tangente_angulo = math.tan(radiano)

print(f'Seno de {angulo}: {seno_angulo:.2f}')
print(f'Cosseno de {angulo}: {cosseno_angulo:.2f}')
print(f'Tangente de {angulo}: {tangente_angulo:.2f}')
