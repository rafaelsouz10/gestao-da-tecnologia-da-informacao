"""1- Crie as seguintes listas, derivadas de:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    Intervalo de 1 a 9
    Intervalo de 8 a 13
    Números pares
    Números ímpares
    Todos os múltiplos de 2, 3 e 4.
    Lista reversa
    Razão entre a soma do intervalo de 10 a 15 pelo intervalo de 3 a 9 (resultado float)."""
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
mult = []
for i in lista:
    if i % 2 == 0 and i % 3 == 0 and i % 4 == 0:
        mult.append(i)
print(f'''
    Intervalo 1-9: {lista[1:10]}
    Intervalo 8-13: {lista[8:14]}
    Números pares: {lista[::2]}
    Números ímpares: {lista[1::2]}
    Múltiplos de 2, 3 e 4: {mult}
    Lista reversa: {lista[::-1]}
    Razão: {sum(lista[10:])/sum(lista[3:10])}''')