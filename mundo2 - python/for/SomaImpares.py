#calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500

print('\n\t \033[1;33mCalcelue a soma dos números ímpares que são múltiplos de 3, e que se encontram no intervalo de 1 à 500\033[m\n')

soma = 0

for c in range(1, 500):
    if (c%3==0):
        soma += c
print(' A soma dos números ímpares e que são múltiplos de 3 => {}'.format(soma))
