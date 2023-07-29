#escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a BASE DE CONVERSÃO:
# 1-> para binário; 2-> para octal & 3-> para hexadecimal
import math
print('\n\t Base de Conversão!')

num = int(input('\n Informe um número => '))
numConv = str(input(' Informe: \033[1;33m1 - binário, 2 - octal & 3 - hexadecimal\033[m => '))

if numConv == '1':
    transfBin = bin(num)
    print(' O número {} convertido para binário fica \033[1;33m{}\033[m'.format(num,transfBin))
elif numConv=='2':
    transfOctal = oct(num)
    print(' O número {} convertido para octal fica \033[1;33m{}\033[m'.format(num, transfOctal))
elif numConv=='3':
    transfHex = hex(num)
    print( 'O número {} convertido para hexadecimal fica \033[1;33m{}\033[m'.format(num, transfHex))
else:
    print('\033[1;31m O número informado não existe na tabela\033[m')