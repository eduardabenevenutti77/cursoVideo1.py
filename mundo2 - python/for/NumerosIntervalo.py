#crie um programa que mostre na tela todos os números pares no intervalo entre 1 e 50

print('\n\t \033[1;33mVeja todo os números pares que existem no intervalo de 1 à 50\033[m\n')

for c in range(0, 50):
    if(c%2==0):
        print(c)
