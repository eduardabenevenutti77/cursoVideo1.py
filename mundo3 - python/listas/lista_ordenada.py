# crie um programa onde o usuário possa digitar 5 valores númericos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort())
# no final, mostre a lista ordenada na tela - usar if

lista_numeros = []

for cont in range(5):
    try:
        valor = int(input('Digite {}º valor: '.format(cont+1)))
        index = 0
        while index < len(lista_numeros) and lista_numeros[index] < valor:
            index += 1
        lista_numeros.insert(index, valor)
    except ValueError:
        print('Por favor, insira um valor numérico válido.')

print('A lista ordenada = ', lista_numeros)