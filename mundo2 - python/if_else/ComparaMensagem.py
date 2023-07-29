#escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
# 1-> o PRIMEIRO VALOR é maior; 2-> o SEGUNDO VALOR é maior & 3-> NÃO EXISTE valor maior, ambos são iguais

print('\n\t \033[1;33mDescubra qual é maior!\033[m')

num1 = int(input('\n Informe o 1º valor => '))
num2 = int(input(' Informe o 2º valor => '))

if num1>num2:
    print('\n \033[1;32mO número {} é maior que o número {}\033[m'.format(num1,num2))
elif num2>num1:
    print('\n \033[1;32mO número {} é maior que o número {}\033[m'.format(num2,num1))
else:
    print('\n \033[1;32mO número {} e o número {} são iguais\033[m'.format(num1,num2))