"""5- Faça um programa que receba do usuário uma string. O programa
imprime a string sem suas vogais."""
vogais = 'aeiou'
string = input('Insira uma string: ').lower()
for vogal in vogais:
    if vogal in string:
        string = string.replace(vogal, '')
print(string)
