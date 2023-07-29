#faça um programa que leia 3 números e mostre qual é o maior e o manor
n1 = int(input('\nDigite o 1º número => '))
n2 = int(input('\nDigite o 2º número => '))
n3 = int(input('\nDigite o 3º número => '))

nm1 = (n1>n2) #1>2 falso
nm2 = (n3>n2) #3>2 verdadeiro
nm3 = (n3>n1) #3>1 verdadeiro

if(nm3>nm2):
    print('\nMaior => {}'.format(nm3))
    print('\nMenor => {}'.format(nm2))
if(nm2>nm1):
    print('\nMaior => {}'.format(nm2))
    print('\nMenor => {}'.format(nm1))
if(nm1>nm2):
    print('\nMaior => {}'.format(nm1))
    print('\nMenor => {}'.format(nm2))
if(nm1>nm3):
    print('\nMaior => {}'.format(nm1))
    print('\nMenor => {}'.format(nm3))
if(nm2>nm1):
    print('\nMaior => {}'.format(nm2))
    print('\nMenor => {}'.format(nm1))
if(nm3>nm1):
    print('\nMaior => {}'.format(nm3))
    print('\nMenor => {}'.format(nm1))
