'''Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.'''

print('Use apenas números')
dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))

# verificar validade do dia:
if dia < 1 or dia > 31:
  print(f'Data inválida. O número {dia:02} não representa um dia.')
else:
  # verificar validade do mês:
  if mes < 1 and mes > 13:
    print(f'Data inválida. O número {mes:02} não representa um mês.')
  else:
    # verificar meses de 30 dias:
    if mes == (4 or 6 or 6 or 9 or 11):
      if dia > 30:
        print(f'Data inválida. O mês {mes:02} não possui o dia {dia}.')
      else:
        print(f'A data {dia:02}/{mes:02}/{ano:04} é válida.')

    # verificar fevereiro:
    else:
      if mes == 2:
        # verificar ano bissexto:
        if ano % 4 == 0 or (ano % 100 == 0 and ano % 400 == 0): # confirmado ano bissexto
          if dia < 30:
            print(f'A data {dia:02}/{mes:02}/{ano:04} é válida.')
          else:
            print(f'Data inválida. O mês {mes:02} não possui o dia {dia}.')

        # caso não seja ano bissexto:
        else:
          if dia > 28:
            print(f'Data inválida. O mês {mes:02} não tem o dia {dia} no ano de {ano:04}')

      else:
        print(f'A data {dia:02}/{mes:02}/{ano:04} é válida.')
