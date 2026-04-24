from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')

while True:
    computador = randint(0, 2)

    print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

    jogador = int(input('Qual é a sua jogada? '))

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-=' * 11)

    print('O computador jogou {}'.format(itens[computador]))
    print('O jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)

    if computador == 0:  # PEDRA
        if jogador == 0: #jogador jogou pedra
            print('EMPATE!')
        elif jogador == 1: #jogador jogou papel
            print('JOGADOR VENCE!')
        elif jogador == 2: #jogador jogou tesoura
            print('COMPUTADOR VENCE!')

    elif computador == 1:  # PAPEL
        if jogador == 0: #jogador jogou pedra
            print('COMPUTADOR VENCE!')
        elif jogador == 1: #jogador jogou papel
            print('EMPATE!')
        elif jogador == 2: #jogador jogou tesoura
            print('JOGADOR VENCE!')

    elif computador == 2:  # TESOURA
        if jogador == 0: #jogador jogou pedra
            print('JOGADOR VENCE!')
        elif jogador == 1: #jogador jogou papel
            print('COMPUTADOR VENCE!')
        elif jogador == 2: #jogador jogou tesoura
            print('EMPATE!')

    # perguntar se quer continuar
    continuar = input('Quer jogar novamente? (s/n): ').lower()
    if continuar != 's':
        print('Obrigado por jogar!')
        break
