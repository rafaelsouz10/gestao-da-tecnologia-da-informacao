#zenit --- polar
frase= input('Digite uma mensagem: ').lower()
zenit = 'zenitpolar'
polar = 'POLARZENIT'
for i in range(len(zenit)):
    frase = frase.replace(zenit[i], polar[i])
print(frase.lower())