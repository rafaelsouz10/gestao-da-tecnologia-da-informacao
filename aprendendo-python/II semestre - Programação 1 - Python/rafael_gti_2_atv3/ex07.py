qtd_morango= float(input("Quantos kg de morangos você deseja: "))
qtd_maca= float(input("Quantos kg de maçãs você deseja? "))

if qtd_morango<0 or qtd_maca<0:
    print('Quantidade inválida.')
    exit()

#morango
if qtd_morango<=5:
    preco_morango= qtd_morango*2.50
else:
    preco_morango= qtd_morango*2.20
    
#maçã
if qtd_maca<=5:
    preco_maca= qtd_maca*1.80
else:
    preco_maca= qtd_maca*1.50

print(f"""\nQuantidade de morangos comprado: {qtd_morango} kg
Quantidade de maçãs comprado: {qtd_maca} kg""")

preco_total= preco_maca+preco_morango

if (qtd_maca+qtd_morango)>8:
    print("Peso ultrapassa 8kg. Você tem 10% de desconto.")
    
    desconto= (preco_maca+preco_morango)*0.1
    preco_total= preco_total-desconto
    print(f'Preço total a pagar: R$ {preco_total:.2f}.\n')
else:
    print(f'Preço total a pagar: R$ {preco_total:.2f}.\n')