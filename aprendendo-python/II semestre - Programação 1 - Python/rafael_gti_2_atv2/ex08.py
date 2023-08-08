ano= int(input('Insira um ano para saber se é bisexto ou não: '))
'''
anos bisextos são multiplos de 4
NÃO são multiplos de 100, exceto os mútiplos de 400
'''
if ano%4 == 0 and ano%100!=0 or ano%400==0:
    print(f'\nO ano de {ano} é bisexto.\n')             
else:
    print(f'\nO ano de {ano} não é bisexto.')
