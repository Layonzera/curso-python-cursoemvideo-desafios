import math
c_cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
c_cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(c_cateto_oposto, c_cateto_adjacente)

print(f'O comprimento da hipotenusa e: {hipotenusa}')