#crie um programa para jogar jokenpo com vc
import random
print('\n\t Vamos jogar Jokênpo!')

Opcao = ['Pedra','Papel','Tesoura']

Jogar = str(input('\n Deseja Jogar? => ')).upper()

if Jogar=='S' or Jogar=='SIM':
    UsuarioOpcao = str(input('\n Escolha entre: Papel, tesoura ou pedra => '))
    random.choice(Opcao)
    if Opcao=='Pedra' and UsuarioOpcao=='Papel':
        print('\n O usuário ganhou! - {} vs {}'.format(Opcao, UsuarioOpcao))
    elif Opcao=='Pedra' and UsuarioOpcao=='Tesoura':
        print('\n O sistema ganhou! - {} vs {}'.format(Opcao, UsuarioOpcao))
    elif Opcao=='Pedra' and UsuarioOpcao=='Pedra':
        print('\n O usuário ganhou! - {} vs {}'.format(Opcao, UsuarioOpcao))

    elif Opcao=='Papel' and UsuarioOpcao=='Pedra':
        print('\n O sistema ganhou! - {} vs {}'.format(Opcao,UsuarioOpcao))
    elif Opcao=='Papel' and UsuarioOpcao=='Tesoura':
        print('\n O usuário ganhou! - {} vs {}'.format(Opcao, UsuarioOpcao))
    elif Opcao=='Papel' and UsuarioOpcao=='Papel':
        print('\n O sistema ganhou! - {} vs {}'.format(Opcao, UsuarioOpcao))

    elif Opcao=='Tesoura' and UsuarioOpcao=='Pedra':
        print('\n O sistema ganhou! - {} vs {}'.format(Opcao,UsuarioOpcao))
    elif Opcao=='Tesoura' and UsuarioOpcao=='Tesoura':
        print('\n O usuário ganhou! - {} vs {}'.format(Opcao, UsuarioOpcao))
    elif Opcao=='Tesoura' and UsuarioOpcao=='Papel':
        print('\n O sistema ganhou! - {} vs {}'.format(Opcao, UsuarioOpcao))
else:
    print('\n Que pena, nós veremos novamente na próxima vez!')
