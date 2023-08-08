qtd_carne= float(input('Insira quantos kg de carne deseja: '))
tipo_carne= input("""
    1 - File Duplo R$ 4,90 por Kg R$ 5,80 por Kg
    2 - Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
    3 - Picanha R$ 6,90 por Kg R$ 7,80 por Kg

    Insira o caracter respectivo a carne desejada: """)

if tipo_carne=='1':     #File Duplo R$ 4,90 por Kg R$ 5,80 por Kg
    carne='File Duplo'
    if qtd_carne<=5:
        preco= qtd_carne*4.90
        
    else:
        preco= qtd_carne*5.80

elif tipo_carne=='2':   #Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
    carne='Alcatra'
    if qtd_carne<=5:
        preco= qtd_carne*5.90
    else:
        preco= qtd_carne*6.80

elif tipo_carne=='3':   #Picanha R$ 6,90 por Kg R$ 7,80 por Kg
    carne='Picanha'
    if qtd_carne<=5:
        preco= qtd_carne*6.90
    else:
        preco= qtd_carne*7.80
else:
    print('\nCaracter Invalido.\n')
    exit()

cartao= input("\nDigite 1 para utilizar CARTÃO GUANABARA ou outro caracter para utilizar OUTRO CARTÃO: ")


print('======NOTA FISCAL======')
if cartao=='1':
    desconto= preco*0.05
    preco= preco-desconto   #caso use cartão guanabara, preco atualizará com desconto
    print(f'    Desconto: R$ {desconto:.2f}')

print(f"""  Tipo de carne: {carne}
    Quantidade de carne: {qtd_carne}
    Preço total a pagar: R$ {preco:.2f}
""")