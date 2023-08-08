peso= float(input("Insira quantos kg de peixe você tem: "))

excesso= bool((peso-50)>0)*(peso-50)
multa= bool(excesso>=1)*excesso*4

print(f"""
    Peso registrado: {peso} kg.

    OBS.: Todo peso que exceder 50 kg, estabelecido pelo regulamento de pesca do estado de São Paulo, 
    deverá pagar multa de R$ 4,00 por quilo extra!

    Segue abaixo sua possível multa a pagar!
    Peso excedido: {excesso:.2f} kg.
    MULTA a pagar: R$ {multa:.2f}
    """)