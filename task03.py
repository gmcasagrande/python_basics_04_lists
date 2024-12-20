'''Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].'''

lista = []
for i in range(1,6):
  num = int(input(f'Digite o {i}° número: '))
  lista.append(num)

lista
