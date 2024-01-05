#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de 
#zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 a 20) e mostrá-lo por extenso

valores = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

valor_usuario = int(input('Informe um valor entre 0 a 20: '))

if 0 <= valor_usuario <= 20:
    print('O valor informado pelo o usuário é: {}'.format(valores[valor_usuario]))
else:
    print('O valor informado está fora dos valores permitidos! Informe outro valor ;)')