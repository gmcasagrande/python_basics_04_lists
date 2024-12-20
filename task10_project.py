'''Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. 
Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. 
Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).'''

meses = 'Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembo Dezembro'
lista_meses = meses.split()
temperaturas = []
meses_acima_media = []

for i in range(0,12):
  temperatura = int(input(f'Temperatura média de {(lista_meses[i])}: '))
  temperaturas.append(temperatura)
media = sum(temperaturas) / len(temperaturas)

for x in range(0,(len(temperaturas))):
  if temperaturas[x] > media:
    meses_acima_media.append(lista_meses[x])
print(f'Média anual: {media}°C \nMeses acima da média: {meses_acima_media}')
