'''Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias por dia (em milhares) e pode ser observado a seguir:
[1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior.
Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).'''

# lista original
amostras = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

# lista com os percentuais:
porcentagem = []

# cálculo das posrcentagens:
for i in range(1, len(amostras)):
  percentual = (100 * (amostras[i] - amostras[i - 1]) / amostras[i - 1])

  # adiciona cada valor das porcentagens à lista com os percentuais:
  porcentagem.append(round(percentual,2)) # a função ROUND vai deixar o valor FLOAT com duas casas decimais

#print(f'Porcentagem de crescimento: \n {porcentagem}')
porcentagem
