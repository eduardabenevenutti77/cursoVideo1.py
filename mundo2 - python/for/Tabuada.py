#mostre a tabuada de um número usando o laço for

print('\n\t \033[1;33mVerifique a tabuada\033[m\n')

n = int(input(' Informe o número que você deseja descobrir a tabuada => '))
print('\n')

for c in range(0, 11):
    print("{} x {} = {}".format(c,n,n*c))
