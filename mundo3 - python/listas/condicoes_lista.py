# crie um programa que leia vários números e o colque em uma lista
# depois disso, mostre: 
# a) quantos números foram digitados
# b) a lista de valores, ordenado de forma decrescente
# c) se o valor 5 foi digitado e está ou não na lista

lista_valores = []

while True:
    try:
        valor = input(str('Informe o valor ou digite C para sair: '))
        if valor.lower() == 'c':
            break
        valor = int(valor)
        lista_valores.append(valor)
    except ValueError:
        print('Por favor, insira um valor numérico válido.')
        
print('\nNúmeros digitados = {}'.format(lista_valores))

lista_ordenada = sorted(lista_valores, reverse=True)
print('A lista ordenada de forma decrescente é = {}'.format(lista_ordenada))

if 5 not in lista_valores: 
    print('O valor 5 não está presente na lista')
else: 
    print('O valor 5 está presente na lista')