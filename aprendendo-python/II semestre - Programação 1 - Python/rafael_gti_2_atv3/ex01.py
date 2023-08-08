nota1= float(input("Insira a primeira nota: "))
nota2= float(input("Insira a segunda nota: "))

media= (nota1+nota2)/2

if media<7:
    print("\nReprovado!\n")
elif 7<=media<10:
    print("\nAprovado!\n")
else:
    print("\nAprovado com Distinção!\n")