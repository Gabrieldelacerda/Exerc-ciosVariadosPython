from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('O computador escolheu {}'.format(itens[computador]))
jogador = int(input('Escolha a jogada '))
print('0 pedra, 1 papel, 2 tesoura')
print('O computador escolheu {}'.format(computador))
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    else:
        print('jogador perdeu')
elif computador == 1:
    if jogador == 0:
        print('jogador perdeu.')
    elif jogador == 1:
        print('empate')
    else:
        print('jogador venceu')
else:
    if jogador == 0:
        print('jogador venceu')
    elif jogador == 1:
        print('jogador perdeu')
    else:
        print('empate')