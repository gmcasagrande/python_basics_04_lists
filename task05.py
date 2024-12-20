'''Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.'''


num = int(input('Digite um número: '))
primos = []

#escolher os números entre 2 e o número limite:
for num_primo in range(2, num):
  #estabelecer comdições para que a variável PRIMO seja verdadeira:
  primo = True
  #criar um loop para averiguar se os números são primos:
  for divisivel in range(2, num_primo):
    #se o número escolhido for divisível por qualquer um na lista limite, a condição PRIMO será falsa e o número será descartado:
    if num_primo % divisivel == 0:
      primo = False
      break

  #o número não descartado será selecionado e adicionado à lista previamente vazia:
  if primo:
    primos.append(num_primo) 

print(f'A lista de números primos de 1 até {num} é {primos}')
