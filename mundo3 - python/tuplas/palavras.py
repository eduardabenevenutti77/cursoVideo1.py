#crie uma tupla com várias palavras (não pode usar acentos). depois disso, mostre para cada palavra, quais são as suas vogais

palavras = ('abacate', 'limao', 'uva', 'carro', 'caminhar', 'correr', 'lutar', 'gostar', 'gastar', 'comer', 'cuidar', 'amar', 'levar')

for vogal in palavras:
  palavra_vogal = [letra for letra in vogal if letra.lower() in 'aeiou']
  print('As vogais em {} são: {}'.format(vogal, ', '.join(palavra_vogal)))
