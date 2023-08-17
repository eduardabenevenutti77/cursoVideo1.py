#faça um programa que leia um número e mostre o seu fatorial
#ex: 5! = 5*4*3*2*1 = 120

from math import factorial

n = int(input("Informe o número: "))
f = factorial(n)
print("O fatorial de {} é {}".format(n,f))
