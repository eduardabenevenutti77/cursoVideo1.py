#leia 4 valores e guarde-os em uma tupla. no final mostre:
#a) quantas vezes apareceu o valor 4
#b) em que posição foi digitado o primeiro valor 3
#c) quais foram os números pares

valor01 = int(input('Informe o 1º valor => '))
valor02 = int(input('Informe o 2º valor => '))
valor03 = int(input('Informe o 3º valor => '))
valor04 = int(input('Informe o 4º valor => '))

valores = (valor01, valor02, valor03, valor04)
print(valores)

print('''\nSelecione a opção:
\n[1] Quantas vezes apareceu o valor 4
[2] Em qual posição foi digitado o primeiro valor 3
[3] Listar quais foram os números pares''')
opcao = str(input('Informe a opcão selecionada => '))

if opcao == '1':
  print('Quantidade de vezes que apareceu o valor 4: ')
  quantidade = valores.count(4)
  print(quantidade)
elif opcao == '2':
  print('Posição do 1º valor 3 digitado: ')
  posicao = valores.index(3)
  print(posicao)
elif opcao == '3':
  print('Números pares: ')
  valores_pares = [num for num in valores if num % 2 == 0]
  print('Valores pares dentro da tupla: ' + ', '.join(map(str, valores_pares)))
else:
  print('A opção selecionada é inválida')
