tamanho_area= float(input("Insira o tamanho, em metros quadrados, da área a ser pintada: "))

cobertura_tinta= tamanho_area/3         #1L de tinta para cada 3 m²
qtd_lata= cobertura_tinta//18 + bool(cobertura_tinta%18)         #qtd de litros precisos para cada lata de 18L


print(f"""
    Será preciso de {cobertura_tinta:.2f}L para {tamanho_area} m²
    Quantidade de Latas de 18 litros de tinta a serem compradas: {qtd_lata}
    Preço ser pago por {qtd_lata} latas: R$ {qtd_lata*80:.2f}
    """)