'''Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e os votos computados podem ser observados abaixo:
Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos'''

votos = [1334, 982, 1751, 210, 1811]
pesquisa = {}

for i in range(0, len(votos)):
  pesquisa[f'Design {i+1}'] = votos[i]

vencedor = ''
votosrecebidos = 0
total = 0

for design in pesquisa.keys():
  total += pesquisa[design]
  if pesquisa[design] > votosrecebidos:
    votosrecebidos = pesquisa[design]
    vencedor = design

# informe o design vencedor e a porcentagem de votos recebidos.

porcentagem = int((votosrecebidos * 100) / total)

print(f'Pesquisa: {pesquisa}')
print(f'O produto vencedor foi o {vencedor} que recebeu {porcentagem}% dos votos.')
