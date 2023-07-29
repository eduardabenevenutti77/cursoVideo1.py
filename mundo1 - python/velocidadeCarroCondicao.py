#escreva um programa que leia a velocidade de um carro
#se ela ultrapassar 80km, mostre uma mensagem dizendo que foi multado
#a multa vai custar 7 reais por cada km a cima do limite

km = float(input('\nDigite a kilometragem => '))
if(km>80):
    multa = (km-80)
    valorMulta = (multa*7)
    print('\nO valor a ser pago é de R$: {:.2f} !!'.format(valorMulta))
else:
    print('\nEstá dentro do valor limite!')