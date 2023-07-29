#escreva um programa que faça o computador pensar
#em um número inteiro entre 0e5 e paça para o usuário descobrir
#qual é o número, o programa deve falar se acertou ou não

n = 5
n1 = int(input('\nDigite um valor entre 0 e 5 => '))

if (n == n1):
    print("\nvocê acertou o número, parabéns!!")
else:
    print('Você errou o número, tente novamente!')