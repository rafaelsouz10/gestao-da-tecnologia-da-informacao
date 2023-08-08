jog1 = int(input('JOGO DE ADIVINHAÇÃO\n\nJOGADOR 1, escolha um número de 1 a 10: '))

if jog1<1 or jog1>10:
    print('Número não está entre 1-10.')
    exit()
tentativa= 1

jog2= int(input('JOGADOR 2, qual foi o número escolhido por JOGADOR 1? '))
while jog1 != jog2:
    tentativa += 1
    jog2= int(input('Você errou! Tente de novo: '))

print(f'\nParabéns, JOGADOR 2. Você acertou em {tentativa} tentativas.\n')