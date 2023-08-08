"""1- Faça um programa que lê uma palavra ou frase e transforma suas vogais em maiúsculo
e as consoantes em minúsculo. Em seguida imprime a palavra/frase resultante."""
frase= input('Insira uma palavra ou frase: ').lower()
vogais= 'ãáaeéiou'
for letra in vogais:
    frase= frase.replace(letra, letra.upper())
print(frase)