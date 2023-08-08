qtd_vogais= {}
vogais = 'aeiou'

texto = input('Insira um texto para saber a quantidade de cada vogal que aparece: ')

for vogal in vogais:
    if vogal in texto:
        qtd_vogais[vogal] = texto.count(vogal)
print(qtd_vogais)