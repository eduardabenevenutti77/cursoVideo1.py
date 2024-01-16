# crie um programa onde o usuário pode digitar vários valores númericos e cadastre-os em uma lista
# caso o número já exista na lista, ele não deverá ser adicionado. 
# no final, deverá ser exibido os valores únicos digitados e em ordem crescente

lista_numeros = []

while True: 
    try: 
        valor = input(str('Insira um valor ou insira a letra C para sair: '))
        if valor.lower() == 'c':
            break
        valor = int(valor)
        if valor not in lista_numeros:
            lista_numeros.append(valor)
            print('O valor {} foi adicionado na lista!'.format(valor))
        else:
            print('O valor {} já está presente na lista!'.format(valor))
    except ValueError:
        print('Por favor, insira um valor numérico válido.')

lista_ordenada = sorted(lista_numeros)
print('A lista ordenada é {}'.format(lista_ordenada))
