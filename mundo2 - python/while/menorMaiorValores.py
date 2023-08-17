#leia varios números inteiros, no final da execução mostre a média entre eles e qual foi o maior e o menor número
#o programa deverá perguntar ao usuário se ele deseja continuar ou não no programa

resp = 'S'
soma = quant = media = maior = menor = 0

while resp in 'Ss':
    nm = int(input('Digite um valor: '))
    soma += nm
    quant += 1
    if (quant == 1):
        maior = menor = nm
    else:
        if (nm > maior):
            maior = nm
        if (nm < menor):
            menor = nm
    resp = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
media = soma/quant
print("vc digitou {} números e a média foi {}".format(quant, media))
print("o maior valor foi {} e o menor valor foi {}".format(maior, menor))
