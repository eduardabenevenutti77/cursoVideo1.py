#condiçoes aninhadas (encaixe de condições);
#if, else & elseif(elif);
#sempre ver as outras possibilidades!
#estrutura aninhada: condições são desenvolvidas dentro de outra/s condições;
#sempre deve possuir o if, mas o elif e else são opcionais;
#pode haver vários elif dentro da condição, porém deve haver somente um else;
#formado de ninho ou boneca russa;

#prática de estrutura de condição aninhada:
nome = str(input(" Informe ao sistema o seu nome => ")).upper()
if nome=='MARIA':
    print(" Que nome bonito!")
elif nome=='PEDRO' or nome=='PAULO' or nome=='FELIPE':
    print(' O seu nome é bem popular no Brasil.')
elif nome in 'CLÁUDIA AMANDA ANA JULIANA FERNANDA':
    print(' Parabéns, você possui um belo nome feminino!')
else:
    print(" Você possui um nome bem normal..")
print(" Tenha um Bom dia, {}!".format(nome))