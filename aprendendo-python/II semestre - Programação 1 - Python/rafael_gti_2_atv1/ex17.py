tamanho_area= float(input("Insira o tamanho, em metros quadrados, da área a ser pintada: "))

cobertura_tinta= tamanho_area/6          #1L de tinta para cada 6 m²

#   LATA 18L
qtd_lata= int(cobertura_tinta/18)+1               #qtd de litros precisos para cada lata de 18L

#   GALÃO 3.6L
qtd_galao= int(cobertura_tinta/3.6)+1            #qtd de litros precisos para cada lata de 3.6L

# MISTURA LATA E GALÃO
qtd_lata_baixo= int(cobertura_tinta/18)
resto_lata= (cobertura_tinta/18)-(int(cobertura_tinta/18))
qtd_galao_lata= int(resto_lata)+1
taxa= ((qtd_lata_baixo*80)+(qtd_galao_lata*25))*0.1
total= (qtd_lata_baixo*80)+(qtd_galao_lata*25)+taxa

print(f"""
    ________________________________________________________________________
    Será preciso de {cobertura_tinta}L para {tamanho_area} m²

    -----------------------LATAS DE 18 LITROS--------------------------------
    Quantidade de Latas de 18 litros de tinta a serem compradas: {qtd_lata}
    Preço ser pago por {qtd_lata} latas: R$ {qtd_lata*80}.00

    -----------------------LATAS DE 3.6 LITROS-------------------------------
    Quantidade de galões de 3.6 litros de tinta a serem comprados: {qtd_galao}
    Preço ser pago por {qtd_galao} galões: R$ {qtd_galao*25}.00

    __________________________LATAS E GALÕES_________________________________
    OBS.: OS RESULTADOS ABAIXO SÓ SÃO VÁLIDOS PARA ÁREAS ACIMA DE 108 M².
    CASO CONTRÁRIO, DESCONSIDERE-OS!

    Quantidade de Latas de 18 litros de tinta a serem compradas: {qtd_lata_baixo}
    Quantidade de galões de 3.6 litros de tinta a serem comprados: {qtd_galao_lata}
    Preço ser pago por {qtd_lata_baixo} latas: R$ {qtd_lata_baixo*80}.00
    Preço ser pago por {qtd_galao_lata} galões: R$ {qtd_galao_lata*25}.00
    Taxa de 10% de folga: R$ {taxa}
    Total a pagar: R$ {total}
    
""")