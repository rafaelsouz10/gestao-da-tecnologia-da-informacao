'''3- Escreva uma programa que solicite um texto ao usuário e conte a quantidade de vogais nele. 
Crie um dicionário utilizando as vogais como chave e a quantidade de cada vogal o seu respectivo valor.
Ao final imprima o dicionário.'''
dicionaio= {}
vogais = 'aeiou'
texto = input('Digite um texto: ').lower()

for vogal in vogais:
    if vogal in texto:
        dicionaio[vogal] = texto.count(vogal)
    '''if vogal in dicionaio:
            dicionaio[vogal] += 1           
        else:
            dicionaio[vogal] = 1'''
print(dicionaio)
for vogal, qtd in dicionaio.items():
    print(f"Vogal '{vogal}' aparece {qtd}x no texto.")