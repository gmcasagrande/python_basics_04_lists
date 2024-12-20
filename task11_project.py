'''Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:
{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
'Produto D': 200, 'Produto E': 250, 'Produto F': 30}'''

vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
unid_produtomais = 0
total = 0

for produto in vendas.keys():
  total += vendas[produto]
  if vendas[produto] > unid_produtomais:
    unid_produtomais = vendas[produto]
    produtomais = produto

print(f'Foram vendidas um total de {total} unidades.')
print(f'O mais vendido foi o {produtomais}, que vendeu {unid_produtomais} unidades.')
