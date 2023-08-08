'''2- Faça um programa que receba do usuário uma string. O programa imprime a string
sem suas vogais.'''
palavra= input('Insira uma palavra: ').lower()
vogal= 'aeiou'
for letra in vogal:
    palavra= palavra.replace(letra,'')
print(palavra)