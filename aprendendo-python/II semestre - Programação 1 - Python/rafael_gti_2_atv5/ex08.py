palavra= input('Insira uma palavra: ')
vogal= 'aeiou'

for letra in vogal:
    if letra in palavra:
        palavra= palavra.replace(letra,'')
print(palavra)