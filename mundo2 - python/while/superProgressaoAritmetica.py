#melhore o progama da progressão aritmetica..pergunte ao usuário se ele deseja mostrar + alguns termos
#o programa deve encerrar quando o usuário digitar 0

primeiroTermo = int(input("Informe 1º termo => "))
razao = int(input("Digite a razão: "))

termo = primeiroTermo

cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont<=total:
        print("{} -> ".format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input("Quantos termos vc quer a mais? "))
