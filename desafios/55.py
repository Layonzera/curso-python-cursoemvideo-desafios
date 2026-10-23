maior_peso = 0
menor_peso = 1000000000000000

for i in range(5):
  peso = float(input('Digite seu peso: '))
  if peso > maior_peso:
    maior_peso = peso
  else: 
    menor_peso = peso

print(maior_peso)
print(menor_peso)