'''4- Faça um programa que cria uma lista de 10 números inteiros, converta
cada um desses números para binário e mostre a sequência de 0s e 1s na
tela. Deve ser mostrado um abaixo do outro.
Exemplo:
    2 = 10
    10 = 1010
    ...'''
import random
num=[]; binario=[]
for i in range(10):
    num.append(random.randint(1,50))
    print(f'{num[i]} = {bin(num[i])[2:]}')