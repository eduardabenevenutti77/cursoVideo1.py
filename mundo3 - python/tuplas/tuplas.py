# variáveis compostas - tuplas, listas e dicionários
#  = (atribui valor a variável - simples)
# variável simples (recebe apenas 1 elemento) | variável composta (recebe vários valores)
# variáveis compostas: tuplas, listas e dicionários
# tuplas: identifica os elementos por indices
# print(nome_tupla) - mostra todos os elementos | print(nome_tupla[indice]) - mostra somente o elemento desse indice | print(noome_tupla[-valor]) - mostra o último elemento
# pode-se utilizar o método len (comprimento) | len(nome_tupla) - mostra o comprimento da tupla
# estrutura de repetição dentro da tupla 
    #for nome_variável_for in nome_tupla:
        #print(nome_variável_for)
#tupla -> lanche = ('abacate','limão','uva')
#print(lanche[1]) - mostra a o lanche na 1ª posição (limão)

lanche = ('abacate', 'limao', 'uva', 'abacaxi')
print(lanche[1])
print(lanche[2:])
print(lanche[-1:])
print(lanche)

#mostrando os elementos da tupla dentro de uma estrutura de repetição for
for comida in lanche:
    print(f'eu vou comer {comida}')
    
print(len(lanche)) #mostra o tamanho da tupla

#mostrando usando cont e range com o tamanho da tupla
for cont in range(0, len(lanche)):
    print(lanche[cont])
       
#organiza os elementos da tupla em ordem
print(sorted(lanche))

#tuplas são imutáveis