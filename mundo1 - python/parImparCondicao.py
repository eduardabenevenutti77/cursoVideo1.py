#crie um programa que leia um número inteiro e mostre
#na tela se é par ou ímpar

nm = int(input('\nDigite um valor => '))
if(nm%2==0):
    print('\nO número {} é par!'.format(nm))
else:
    print('\nO número {} é ímpar!'.format(nm))