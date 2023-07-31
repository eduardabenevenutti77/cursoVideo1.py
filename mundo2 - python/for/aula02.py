# estrutura de repetição - FOR
# laço com variavel de controle;
# => possibiliades dentro do programa;
# for(i=0;i>=2;i++) no c/++
# i=0-> variavel de inicialização, i>=2 -> condiçãp & i++ -> contador;

#-------------------------------------------------

#laçocnointervalo(1,10) - sem repetição
    #passo - está dentro do laço
#pega - está fora do laço

# c -> contador

#forcinrange(1,10): - sem repetição
    #passo - está dentro do laço
#pega - está fora do laço

#-------------------------------------------------

#laçocnointervalo(0,3) - com repetição
    #passo
    #pula
#passo
#pega

#forcinrange(0,3) - com repetição
    #passo
    #pula
#passo
#pega

#-------------------------------------------------

#laçocnointervalo(0,3) - aninhamento de condições
    #se tivermoeda
        #pega
    #passo
    #pula
#passo
#pega

#forcinrange(0,3): - aninhamento de condições
    #if tivermoeda:
        #pega
    #passo
    #pula
#passo
#pega

#-------------------------------------------------
for c in range(6, 0, -1): #-1 diminui; 2 pula
    print(c)
    #print('olá mundo')
print('fim do laço de repetição ;)')

print('--------------------------------------')

n=int(input('informe um valor '))
for c in range(0, n+1):
    print('o usuario escolheu essa quantidade de repetição - {}'.format(n))
print('\n\nfim do laço de repetição ;)')

print('--------------------------------------')

i = int(input('inicio => '))
f = int(input('fim => '))
p = int(input('passo => '))
for c in range(i, f+1,  p):
    print(c)
print('\n\nfim do laço de repetição ;)')

print('--------------------------------------')
s=0
for c in range(0, 4):
    n = int(input('digite um valor => '))
    s += n
print('\nsomatorio dos valores foi {} ;)'.format(s))