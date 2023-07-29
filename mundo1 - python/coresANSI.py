#\033[0;33;44m #style;text;back
#style: 0 -> sen, 1-> negrito. 4-> sublinhado, 0-> inverte a posição
#cor_text: 30-> white, 31->red, 32-> green, 33-> yellow, 34-> blue, 35-> purple, 36 -> blue light and 37 -> gray
print('\033[1;0;45molá mundo\033[m')
print('\033[7;30molá mundo\033[m')
print('\033[1;34;43molá mundo\033[m')

nome = 'maria'
print('é um pazer te conhecer, {}{}{}!'.format('\033[1;35m', nome, '\033[m'))
