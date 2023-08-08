num1= float(input("Insira o primeiro número: "))
num2= float(input("Insira o segundo número: "))
num3= float(input("Insira o terceiro número: "))

if num1 == num2 == num3:
    print("\nOs números são iguais\n.")
else:
    maior= num1
    if num2>maior:
        maior= num2
    if num3>maior:
        maior= num3
    print(f"\nO número {maior} é maior.")

    menor= num1
    if num2<menor:
        menor= num2
    if num3<menor:
        menor= num3
    print(f"O número {menor} é menor.\n")