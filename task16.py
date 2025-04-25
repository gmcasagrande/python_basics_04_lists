numeros = [2, 9, 8, 15, 23, 91, 112, 256]

for i in numeros:
  raiz = i ** 0.5;
  print(f'Raiz de {i} = {raiz:.2f} | é inteiro? :', raiz // 1 == raiz)
