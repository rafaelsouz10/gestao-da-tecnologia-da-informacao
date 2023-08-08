'''6- Faça um programa que peça ao usuário para criar uma lista com o
nome e preço de diversos produtos (o usuário escolhe), um produto por
posição. Após criar a lista, apresente-a na tela, calcule e mostre o total da
compra.'''
import os

print(f"{'-'*4} LISTA DE PRODUTOS DO SUPERMECADO {'-'*4}\n")
nomes = [
    ("Arroz", 5.99),
    ("Feijão", 3.99),
    ("Macarrão", 2.49),
    ("Leite", 3.29),
    ("Café", 6.99),
    ("Azeite", 9.99),
    ("Sal", 1.49),
    ("Açúcar", 2.99),
    ("Farinha de Trigo", 2.79),
    ("Biscoito", 4.49)
]
for i, nome in enumerate(nomes):
    produto, precos = nome
    print(f"{i+1} - {produto} R$ {precos:.2f}")

compras = []
while True:
    posicao= int(input('\nInsira um produto à sua lista de compras pela posição: '))
    compras.append(nomes[posicao-1])
    print(f'{nomes[posicao-1]} Adicionado à lista de compras')
    para = input("\nPara finalizar inscrição de produtos, digite '0', caso contrário qualquer caracter: ") 
    if para == '0':
        os.system('cls')
        break
print(f"{'-'*4} SUA LISTA DE COMPRAS DO SUPERMECADO {'-'*4}\n")
for i, compra_lista in enumerate(compras):
    compra, preco = compra_lista
    print(f'{i+1} - {compra} R$ {preco:.2f}')

preco_compras=[]
for i in compras:
    preco_compras.append(i[1])
print(f'\nTOTAL COMPRA: R$ {sum(preco_compras):.2f}')