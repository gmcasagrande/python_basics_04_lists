'''Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.'''

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
quant_compras = len(gastos)
quant = 0

for compras in gastos:
  if compras > 3000.00:
    quant += 1
porcentagem = int((quant * 100) / quant_compras)

print(f'Foram realizadas {quant} compras acima de R$3000,00 que representam {porcentagem}% do total de compras.')
