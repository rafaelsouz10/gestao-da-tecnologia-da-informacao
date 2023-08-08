saque= float(input('\nCaixa Eletrônico\n\nSaque disponível entre R$ 10,00 e R$ 600,00.\n\nQual o valor do saque?\n '))

if 10<=saque<=600:
    #notas de 100 reais
    qtd_cem= saque//100
    resto_cem= saque%100
    print(f'{qtd_cem} notas de R$ 100,00.\n')

    #notas de 50 reais
    qtd_cinquenta= int(resto_cem/50)
    resto_cinquenta= resto_cem%50
    print(f'{qtd_cinquenta} notas de R$ 50,00.\n')

    #notas de 10 reais
    qtd_dez= int(resto_cinquenta/10)
    resto_dez= resto_cinquenta%10
    print(f'{qtd_dez} notas de R$ 10,00.\n')

    #notas de 5 reais
    qtd_cinco= int(resto_dez/5)
    resto_cinco= resto_dez%5
    print(f'{qtd_cinco} notas de R$ 5,00.\n')

    #notas de 1 reais
    qtd_um= int(resto_cinco)
    resto_um= resto_cinco%1
    print(f'{qtd_um} notas de R$ 1,00.\n')

    #verificação de moedas
    if 0<resto_um<1:
        print(f'R$ {resto_um:.2f} em moedas indisponível. Saque liberado de R${int(saque)},00\n.')

else:
    print('\nVocê só pode sacar um valor entre R$ 10,00 e R$ 600,00 reais.\n')
