#crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#depois disso, mostre a listagem de números gerados e tabém indique o menor e o maio número da tupla

import random

valores = tuple(random.randint(1, 10) for _ in range(5))
print(valores)

print('''\nSelecione a opção:
\n[1] Mostrar todos os valores
[2] Mostrar o maior número da tupla
[3] Mostrar o menor número da tupla
''')
opcao = str(input('Informe a opcão selecionada => '))

if opcao == '1':
    print('Valores: ')
    print(valores)
elif opcao == '2':
    print('Maior: ')
    maior = max(valores)
    print(maior)
elif opcao == '3':
    print('Menor: ')
    menor = min(valores)
    print(menor)
else:
    print('A opção informada é inválida!')
