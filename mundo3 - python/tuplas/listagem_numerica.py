#crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#depois disso, mostre a listagem de números gerados e tabém indique o menor e o maio número da tupla

import random

valores = tuple(random.randint(1, 10) for _ in range(5))
print(valores)
