#leia o nome, idade e sexo de 4 pessoas, e no final mostre:
#média de idades
#nome do homem mais velho
#quantas mulheres tem menos de 20 anos
import media as media

print('\n\t \033[1;33mCaracteristicas Gerais\033[m\n')

soma = 0
idade = 0
maior = 0
for c in range(1, 4):

    nome = str(input(' \n Informe o nome da {}ª pessoa => '.format(c)))
    idade = int(input(' Informe a idade da {}ª pessoa => '.format(c)))
    sexo = str(input(' Informe a sexualidade da {}ª pessoa => '.format(c))).upper()


media += idade
md = media/4

print(' \nA média das idades é {}'.format(md))

if sexo=='F'  and idade<20:
    soma += c;
    print(" \nExistem {} mulheres na lista que são menores de idade!\n".format(soma))
if sexo=='M' and idade<20:
    maior = idade
    name = nome
    print(' \nO nome do homem mais velho é {}'.format(name))
else:
    print('\n Não existe homem na lista ;)')
