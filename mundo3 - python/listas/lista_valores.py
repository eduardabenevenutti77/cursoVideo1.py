# fup que leia 5 valores númericos e guarde-os em uma lista
# no final, mostre qual foi o maior e o menor número valor digitado
# e suas repectivas posições na lista

lista = []

for cont in range(0, 5):
    lista_valores = int(input('Informe o {}º valor da {} posição: '.format(cont+1, cont)))
    lista.append(lista_valores)
print(lista)

maior_valor = max(lista)
menor_valor = min(lista)

posicao_maior = lista.index(maior_valor)
posicao_menor = lista.index(menor_valor)

print('O maior valor é {} e está na posição {}'.format(maior_valor, posicao_maior))
print('O menor valor é {} e está na posição {}'.format(menor_valor, posicao_menor))
