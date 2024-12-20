'''O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:
{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.'''


colab = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
         'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
         'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
         'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

media_setor = [] # média de idade de cada setor
soma_medias = 0 # idade média geral entre todos os setores
acima_media = 0 # quantas pessoas acima da idade média geral

for (setor, idades) in colab.items():
  soma = sum(idades)
  media = int(soma / len(idades))
  print(f'A média de idade do {setor} é {media}.')
  soma_medias += media

media_geral = int(soma_medias / len(colab))
idades = colab.values()

for lista in idades:
  for idade in lista:
    if idade > media_geral:
      acima_media += 1

print(f'A média de idade de todos os colaboradores é {media_geral}.')
print(f'Há {acima_media} colaboradores com idade acima da média.')
