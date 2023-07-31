#leia uma frase e diga se ela é um palíndromo
#desconsidere os espaços

print('\n\t \033[1;33mVerifique se a frase é um palindroma\033[m\n')

frase = str(input('Digite uma frase: ')).strip().upper()
c = frase.split()
frasejunta = ''.join(c)
inverso = frasejunta[::-1]

if inverso != frasejunta:
    print('A frase: {} não é um Palíndromo'.format(frase))
else:
    print('A frase: {} é um Palíndromo'.format(frase))
