from random import randint
v = 0
while True:
    usuario = int(input("insira um valor = "))
    comp = randint(0,10)
    total = usuario + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'vc jogou {usuario} e o computador {comp}. total de {total}')
    if (tipo == 'P'):
        if total % 2 == 0:
            print("vc venceu!!")
            v += 1
        else:
            print("vc perdeu!!")
            break
    elif tipo == 'I':
        if (total % 2 == 1):
            print("vc venceu!!")
            v += 1
        else:
            print("vc perdeu!!")
            break
