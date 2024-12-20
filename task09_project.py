'''Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito.
Cada questão vale um ponto e existem as alternativas A, B, C ou D.
Gabarito da prova:
01 - D
02 - A
03 - C
04 - B
05 - A
06 - D
07 - C
08 - C
09 - A
10 - B'''

gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
pontos = 0.0
certas = []
erradas = []

for i in range(0, len(gabarito)):
  resposta = str(input(f'Digite a resposta da questão {i+1}: ')).upper()
  if resposta == gabarito[i]:
    pontos += 1
    certas.append(i+1)
  else:
    erradas.append(i+1)

print(f'\nSua nota é {pontos} \nQuestões corretas: {certas} \nQuestões erradas: {erradas}')
