#crie uma tupla preenchida com os 20 primeiros colocados do CBF, na ordem de colocação. 
#depois mostre:
#a) apenas os 5 primeiros colocados; b) os últimos 4 colocados na tabela; 
#c) uma lista com os times em ordem alfabética; d) em que posição na tabela está o tima da chapecoense.

times = ('palmeiras', 'grêmio', 'atlético-mg', 'flamengo', 'botafogo', 'bragantino', 'fluminense', 'athetico-pr', 'internacional', 'fortaleza', 'são paulo', 'cuibá', 'corinthias', 'cruzeiro', 'vasco', 'santos', 'bahia', 'goiás', 'coritiba', 'américa-mg')

print('''\n Selecione a opção:
\n[1] Mostrar os 5 primeiros colocados
[2] Mostrar os 5 últimos colocados
[3] Listar times em ordem alfabética
[4] Qual posição está o time da chapecoense''')
opcao = str(input('Informe a opcão selecionada => '))

if opcao == '1':
    print('Os 5 primeiros colocados: ')
    for equipe in range (5):
        print(equipe[times])
elif opcao == '2':
    print('Os 5 últimos colocados: ')
    print(times[-5])
