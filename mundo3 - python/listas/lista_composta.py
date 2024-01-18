# Faça um programa que leia nome e peso de várias pessoas,                                      
# guardando tudo em uma lista. No final, mostre:                                                                                                    
#   A) Quantas pessoas foram cadastradas.                                                                                                                
#   B) Uma listagem com as pessoas mais pesadas.                                                                                                    
#   C) Uma listagem com as pessoas mais leves.

lista_pessoa = []
pessoas = []

while True: 
    try: 
        nome = str(input('Informe o nome e peso da pessoa ou insira a letra C para sair: '))
        if nome.lower() == 'c':
            break
        peso = int(input('Informe o peso da peso => '))
        pessoas.append(nome, peso)
        lista_pessoa.append(pessoas)
    except ValueError:
        print('Por favor, insira um valor numérico válido.')