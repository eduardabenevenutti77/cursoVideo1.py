#pergunte a distancia de uma viagem em nkm
#calcule o preço da passagem, cobrando 0,50 por km para viagens até 200km
#e 0,45 para viagens mais longas

km = float(input('\nInforme a kilometragem da viagem => '))
if(km<=200):
    calculo = (km*0.50)
    print('\nO valor da passagem é de R$ {:.2f}'.format(calculo))
else:
    calculo2 = (km*0.45)
    print('\nO valor da passagem é de R$ {:.2f}'.format(calculo2))