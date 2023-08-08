preco1= float(input("Insira o preço do primeiro produto: "))
preco2= float(input("Insira o preço do segundo produto: "))
preco3= float(input("Insira o preço do terceiro produto: "))

if preco1==preco2==preco3:
    print(f"\nOs três produtos têm o mesmo valor.\n")
elif preco1==preco2 and preco2<preco3:
    print(f"\nO primeiro e o segundo produto, ambos de R$ {preco1:.2f}, são mais baratos que o terceiro produto de R$ {preco3:.2f}.\n")

elif preco1==preco3 and preco3<preco2:
    print(f"\nO primeiro e o terceiro produto, ambos de R$ {preco1:.2f}, são mais baratos que o segundo produto de R$ {preco2:.2f}.\n")

elif preco3==preco2 and preco2<preco1:
    print(f"\nO segundo e o terceiro produto, ambos de R$ {preco2:.2f}, são mais baratos que o terceiro produto de R$ {preco1:.2f}.\n")


elif preco2>preco1 and preco3>preco1:
   print(f"\nO primeiro produto de R$ {preco1:.2f} é mais barato")

elif preco1>preco2 and preco3>preco2:
   print(f"\nO segundo produto de R$ {preco2:.2f} é mais barato")

elif preco1>preco3 and preco2>preco3:
    print(f"\nO Terceiro produto de R$ {preco3:.2f} é mais barato")