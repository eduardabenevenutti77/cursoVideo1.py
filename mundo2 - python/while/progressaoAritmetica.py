#leia o 1º termo e a razão de uma PA, mostre os 10 primeiros termos da progressão
#deve-se utilizar while

primeroTermo = int(input("Digite o 1º: "))
razao = int(input("Digite a razão: "))

termo = primeroTermo
cont = 1

while cont <= 10:
    print("{} -> ".format(termo), end='')
    termo += razao
    cont += 1
