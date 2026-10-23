primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
n = int(input('Exibir quantos elementos: '))

ultimo = primeiro + (n -1) * razao
ultimo += 1

for i in range(primeiro, ultimo, razao):
  print(i)