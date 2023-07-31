#leia um número inteiro e diga se é ou não primo

print('\n\t \033[1;33mVerifique se o número é inteiro ou não\033[m\n')

for c in range(0, 1):
    num = int(input('\n Digite o valor => '))
    if(num%num==0):
        print(' O número {} é primo...'.format(num))
    else:
        print(' O número {} não é primo...'.format(num))
