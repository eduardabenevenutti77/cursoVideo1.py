#faça um programa que mostre uma contagem regressiva na tela para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles
#procurar biblioteca para espara de tempo ???

import time

print('\n\t \033[1;33mContagem regressiva para a queima de fogos com o laço for\033[m\n')

for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
  
print('\n Os fogos foram estourados!')
