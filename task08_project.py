'''Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. 
Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.'''

ids = []
doces = 0 #pares
amargos = 0 #ímpares

for i in range(0,10):
  ids.append(int(input(f'Digite o código do produto {i + 1}:')))

for id in ids:
  if id % 2 == 0:
    doces += 1

  else:
    amargos += 1

print(f'Doces: {doces}\nAmargos: {amargos}')
