arquivo= float(input("Insira o tamanho do arquivo em MB: "))
veloc_net= float(input("Insira a velocidade da internet em Mbps: "))

temp_downl= arquivo/(veloc_net/8)   #Cálculo para saber em segundos
temp_downl_min= temp_downl/60       #convertido para minutos

print(f"\nO Download será feito em {temp_downl_min} minutos.\n")