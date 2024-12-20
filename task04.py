'''Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.'''

lista = []
for i in range(1,6):
  num = int(input(f'Digite o {i}° número: '))
  lista.append(num)

lista.reverse()
lista
