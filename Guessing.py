# by: Alex Lopes

from random import randint


def verificacao(humano, maquina):
    global tentativas

    if 0 <= humano <= 100:
        tentativas = tentativas + 1
        if humano == maquina:
            print(f'\nVocê ganhou!!\n  O número era {maquina}.')
            return 1

        elif humano < maquina:
            print(f'\nO número é maior {distancia(humano, maquina)}')
            return 0
        else:
            print(f'\nO número é menor {distancia(humano, maquina)}')
            return 0

    else:
        print('\nO número está entre 0 e 100')
        return 0


def distancia(numero_h, numero_m):
    dist = numero_m - numero_h
    if dist >= 0:
        if dist >= 50:
            return '>>>>>'
        elif dist >= 40:
            return '>>>>'
        elif dist >= 30:
            return '>>>'
        elif dist >= 20:
            return '>>'
        elif dist >= 1:
            return '>'
    else:
        dist = abs(dist)
        if dist >= 50:
            return '<<<<<'
        elif dist >= 40:
            return '<<<<'
        elif dist >= 30:
            return '<<<'
        elif dist >= 20:
            return '<<'
        elif dist >= 1:
            return '<'


#Principal:
numeroHumano = -1
intervalo = [0, 100]  # {min, max}
numeroMaquina = randint(intervalo[0], intervalo[1])
tentativas = 0

print(numeroMaquina)

print('-- Guessing Number Game: --')
print(f'O número está entre {intervalo[0]} e {intervalo[1]}. Adivinhe o número:\n')

while True:
    numeroHumano = int(input('digite um número:'))

    if verificacao(numeroHumano, numeroMaquina) == 1:
        print(f'\nTentativas válidas: {tentativas}\n ')
        break

