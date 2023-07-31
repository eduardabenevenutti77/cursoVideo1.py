#leia o peso de 5 pessoas, e mostre o maior e o menor lido

print('\n\t \033[1;33mVerifique o seu peso\033[m\n')

maior = 0
menor = 1000

for c in range(1, 6):
  
    peso = float(input(' Informe o peso da {} pessoa => '.format(c)))

    if peso>maior:
        maior = peso
    if peso<menor:
        menor = peso

print('\n O menor peso é {}kg e o maior é {}kg'.format(menor,maior))
