#faça um programa que leia um ano qualquer
#e mostre se ele é bissexto

ano = int(input('\nInforme um ano => '))
if(ano%400==0):
    print('\nO ano {} é bissexto!!'.format(ano))
else:
    print('\nO ano {} não é bissexto'.format(ano))
