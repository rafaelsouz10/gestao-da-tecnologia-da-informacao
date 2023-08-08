"""3- Utilizando a string abaixo, calcule e escreva o número de caracteres, o
número de frases e o número de palavras nesta string. Escreva também
quantas vezes cada letra aparece.
string = "Hoje é dia de prova de Prog1. A prova está muito fácil. Vou tirar
uma boa nota."""
string = "Hoje é dia de prova de Prog1. A prova está muito fácil. Vou tirar uma boa nota."

qtd_frases = len(string.split(". ")) # split transforma a string em lista até onde tem ". "
qtd_palavras = len(string.split()) # split transforma a string em lista por padrão até onde tem espaço

print(f"""
Quantidade de caracter: {len(string)}
Quantidade de frases: {qtd_frases}
Quantidade de palavras: {qtd_palavras}
""")
string_conjunto = set(string)
for letra in string_conjunto:
    freq_letra = string.lower().count(letra.lower())
    print(f'O caracter {letra} aparece {freq_letra} vezes.')
