'''Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta. 
A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área dessa floresta e armazenou essas informações em um dicionário. 
Nele, a chave descreve a área dos dados e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.
{'Área Norte': [2819, 7236],
'Área Leste': [1440, 9492],
'Área Sul': [5969, 7496],
'Área Oeste': [14446, 49688],
'Área Centro': [22558, 45148]}
Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica. Dica: use as funções built-in sum() e len().'''

coleta = {'Área Norte': [2819, 7236],
          'Área Leste': [1440, 9492],
          'Área Sul': [5969, 7496],
          'Área Oeste': [14446, 49688],
          'Área Centro': [22558, 45148]}

# atribuir variáveis para a área com maior diversidade
maiorsoma = 0
maiorarea = ''
mediatotal = 0

# segregar os dados
for (area, contagem) in coleta.items():
  # separar a contagem de animais e plantas e fazer os cálculos:
  soma = sum(contagem)
  media = (soma / len(contagem))
  mediatotal += media
  # verificar qual é a área com maior diversidade
  if soma > maiorsoma:
    maiorsoma = soma
    maiorarea = area

  print(f'A área {area} tem uma média de {media} espécies.')
print(f'A área com maior diversidade é a {maiorarea} com {maiorsoma} espécies.')

mediageral = (mediatotal / len(coleta))
print(f'A região tem uma média de {mediageral} espécies por área.')
