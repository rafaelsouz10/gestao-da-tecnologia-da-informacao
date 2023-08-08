num1= float(input("Insira um número: "))
num2= float(input("Insira outro número: "))

if num1 < num2:
    print(f"\n{num1}\n{num2}")
elif num2 < num1:
    print(f"\n{num2}\n{num1}")
else:
    print(f"\nNúmeros iguais\n{num1}\n{num2}")
