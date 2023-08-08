compras = {1: ['Monitor LED 24', 599.99, 1],
           2: ['Teclado Wirelles', 49.26, 1],
           3: ['Mouse Wirelles', 19.90, 1],
           4: ['Cartucho Colorido', 54, 2]}

subtotal = []
print('\nCOD.    NOME           PREÇO     QUANT.    SUBTOTAL')
for codigo, produtos in compras.items():
    nome, preco, qtd = produtos
    subtotal.append(preco*qtd)
    print(f'{codigo}    {nome}    R$ {preco:.2f}    {qtd}    R$ {(preco*qtd):.2f}')
print(f'\nTotal da compra: R$ {sum(subtotal):.2f}.')