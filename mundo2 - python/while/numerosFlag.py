#leia varios números inteiros, o programa só deverá parar quando o usuário digitar 999
#mostre quantos números foram digitados e qual foi a soma entre eles
#desconsidere o flag
n = 0
soma = 0
while n != 999:
    n = int(input("Digite um valor"))
    soma += 1
print("Você precisou de {} tentativas, sendo a soma dessas tentativas = {}".format(soma))
