#leia 6 números inteiros e mostre somente os pares, se o valor foi impar desconsidere-o

print('\n\t \033[1;33mCalcelue a soma dos números pares\033[m\n')

for c in range(1, 6):
    num = int(input('\n Digite {}º valor => '.format(c)))
    if (num%2==0):
        print(' \033[1;33mO número informado é par!!\033[m')
    else:
        print(' \033[1;31mO número foi desconsiderado, pois é um número ímpar..\033[m')
