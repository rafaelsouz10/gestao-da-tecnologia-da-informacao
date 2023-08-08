"""10- Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um
crime. As perguntas são:
    1"Telefonou para a vítima?"
    2"Esteve no local do crime?"
    3"Mora perto da vítima?"
    4“Tinha dívidas com a vítima?"
    5"Já trabalhou com a vítima?“
O programa deve no final emitir uma classificação sobre a participação da pessoa no
crime. Se a pessoa responder positivamente a 2 questões, ela deve ser classificada como
"Suspeita“; entre 3 e 4, como "Cúmplice" e; 5 como "Assassina". Caso contrário, ela será
classificada como "Inocente"."""
perguntas= ["Telefonou para a vítima? ", 
            "Esteve no local do crime? ", 
            "Mora perto da vítima? ", 
            "Tinha dívidas com a vítima? ",
            "Já trabalhou com a vítima? "]
lista_resposta=[]

print("Responda com S-SIM ou outro caracter-NÃO\n")
for pergunta in perguntas:
    resposta= input(pergunta).upper()
    if resposta[0] == "S":
        lista_resposta.append(resposta)

if len(lista_resposta)<=1:
    print('Inocente')
elif len(lista_resposta)==2:
    print('Suspeita')
elif 3<=len(lista_resposta)<=4:
    print('Cumplice')
elif len(lista_resposta)==5:
    print('Assassina')