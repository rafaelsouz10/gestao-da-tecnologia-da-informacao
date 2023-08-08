'''3- Faça um programa que receba uma palavra e calcule quantas vogais (a, e, i, o, u) possui
essa palavra. Entre com um caractere (vogal ou consoante) e substitua todas as vogais da
palavra dada por esse caractere.'''
palavra= input('Insira uma palavra: ').lower()
caracter= input('Insira um caracter para substituir na frase acima: ').lower()
vogal= 'aeiou'
cont= 0
nova= palavra
for letra in vogal:
    cont += palavra.count(letra)
    nova = nova.replace(letra, caracter)
print(cont, nova)
