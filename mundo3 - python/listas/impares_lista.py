# leia vários números e os coloque em uma lista
# depois disso, crie duas lista extras que vão conter apenas os números pares e impares digitados
# ao final, mostre o conteúdo das 3 listas geradas

lista_valores = []
lista_pares = []
lista_impares = []

while True: 
    try:
        valor = input(str('Informe o valor ou digite C para sair: '))
        if valor.lower() == 'c':
            break
        valor = int(valor)
        lista_valores.append(valor)
        if valor % 2 == 0:
            lista_pares.append(valor)
            print('O valor {} é par'.format(valor))
        else: 
            lista_impares.append(valor)
            print('O valor {} é impar!'.format(valor))
    except ValueError:
        print('Por favor, insira um valor numérico válido.')
            
print('O conteúdo da primeira lista é = {}'.format(lista_valores))
print('O conteúdo da lista pares é = {}'.format(lista_pares))
print('O conteúdo da lista impar é = {}'.format(lista_impares))