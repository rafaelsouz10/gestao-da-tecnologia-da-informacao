num = int(input('Insira um numero: '))

qtd=0; i= 0

while qtd < num:
    if i % 2 == 0:
        print(i)
        qtd += 1
        i += 2