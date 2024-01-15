# variáveis compostas - tuplas, listas e dicionários

# listas:
# as listas são mutáveis, portanto, sendo diferente das tuplas!
# usa-se [];
# lanche = ['pizza', 'pudim', 'azeite'] - exemplo
# pode-se adicionar elementos na lista, pelo método append (insere o novo elemento após o último da lista);
# lanche.append['sorvete']

lanche = ['pizza','pudim', 'azeite']
print(lanche)

lanche.append('sorvete')
print(lanche)

# para adicionar elementos antes do primeiro elemento da lista, usa-se o método insert;
# lanche.insert(0, 'abacate')

lanche.insert(0, 'abacate')
print(lanche) 

# para apagar elementos da lista, usa-se o método del
# del lanche[3] ([posicao])

del lanche[4]
print(lanche)

# ou podemos utilizar o método pop para eliminar o último elemento da lista

lanche.pop(3)
print(lanche)

# ou também, o método remove e nele passando o valor (conteúdo) que será deletado

lanche.remove('abacate')
print(lanche)

# pode-se utilizar o método remove com o auxílio da estrutura de repetição if

if 'azeite' in lanche:
    lanche.remove('azeite')
else:
    print('Não existe esse elemento na lista!')
    
# podemos tabmém criar listas através da função range

valores = list(range(4, 11)) 
print(valores)

#começa na valor 4 e finaliza a lista no valor 10
# o método sort - ordena lista que não estão ordenadas

valor = [8, 2, 6, 9, 10, 45, 50, 0, 1]
valor.sort()
print(valor)

# a função len retorna o comprimento da lista

print(len(valor))