odom_inicio= float(input('Insira a marcação do odômetro em (km) do INÍCIO do dia: '))
odom_fim= float(input('Insira a marcação do odômetro em (km) do FIM do dia: '))
litro_combus= float(input('Insira quantos litros foram gastos: '))
total_passageiro= float(input('Insira o valor total recebido dos passageiros: '))

consumo= (odom_fim-odom_inicio)/litro_combus
gasto_combus= litro_combus*6
lucro_liquido= total_passageiro-gasto_combus

print(f'\nConsumo: {consumo} Km/L\nLucro Líquido: R$ {lucro_liquido:.2f}')