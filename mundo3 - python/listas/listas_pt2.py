# variáveis compostas - tuplas, listas e dicionários

# listas:
# podemos armazenar listas dentro outras listas:

dados = []

dados.append('José Vilas Boas')
dados.append(25)
dados.append('José Boas')
dados.append(29)
print(dados)

pessoas = list()
pessoas.append(dados[:]) # assim é possível incluir uma estrutura dentro de outra

print("lista concatenada: {}".format(pessoas))

# outra maneira de fazer essa integração:

pessoa = [['Adilar', 48], ['Guilherme', 25], ['Elisangela', 47]]
print(pessoa)

print(pessoa[0][0]) # pega no index 0 e o elemento que está na posição 0
print(pessoa[0][1]) # pega no index 0 e o elemento que está na posição 0

# para exluir dados/elementos: 

dados.clear()
print("dados após a função clear: {}".format(dados))