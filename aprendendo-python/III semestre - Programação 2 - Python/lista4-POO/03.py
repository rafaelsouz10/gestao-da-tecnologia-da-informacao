'''3. Classe Bomba de Combustível: Faça um programa completo utilizando uma classe chamada Bomba Combustivel, 
com no mínimo esses atributos: tipo_combustivel, valor_litro e quantidade_combustivel;
Possua no mínimo esses métodos:
    abastecer_por_valor( ) – método onde é informado o valor a ser abastecido e mostra
        a quantidade de litros que foi colocada no veículo;
    abastecer_por_litro( ) – método onde é informado a quantidade em litros de combustível 
        e mostra o valor a ser pago pelo cliente;
    alterar_valor( ) – altera o valor do litro do combustível;
    alterar_combustivel( ) – altera o tipo do combustível;
    alterar_quantidade_combustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar aquantidade de combustível total na bomba.'''
from os import system

class Bomba_combustível():
    def __init__(self,tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        qtd_litro = valor / self.valor_litro
        self.quantidade_combustivel -= qtd_litro
        print(f'Quantidade colocada no veículo: {qtd_litro} L.')
    
    def abastecer_por_litro(self, litro):
        valor_pago = litro * self.valor_litro
        print(f'Quantidade a ser pago: {valor_pago:.2f} BRL.')
        self.quantidade_combustivel -= litro
    
    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
        print(f'\nCombustível com novo valor cadastrado: {self.valor_litro}L.\n')
        input('\nClique em algo para continuar...\n')
        system('cls\n')

    def alterar_quantidade_combustivel(self):
        print(f'Quantidade de litros na bomba: {self.tipo_combustivel} L.\n')
    
    def alterar_combustivel(self):    
        while True:
            print('''     TIPOS COMBUSTÍVEIS        \nGÁS       DIESEL\n        ETANOL''') 

            alterar_tipo_de_combustivel = input("Informe o tipo de combustivel: ").upper()
            if alterar_tipo_de_combustivel == "GÁS" or alterar_tipo_de_combustivel == "DIESEL" or alterar_tipo_de_combustivel == "ETANOL":
                self.tipo_combustivel = alterar_tipo_de_combustivel
                break
            else:
                print("Combustivel inválido! Digite o correto.\n")
        print(f'Novo Combustível na bomba: {self.tipo_combustivel}\n')  
        
bomba1 = Bomba_combustível('gasolina', 4.5, 200)
print('\nCombustível Gasolina, Valor do combustível R$ 4.50 e quantidade da bomba = 200 L.')
bomba1.abastecer_por_valor(9.0)
bomba1.abastecer_por_litro(4.5)
bomba1.alterar_quantidade_combustivel()

input('\nClique em algo para continuar...\n')
system('cls\n')
bomba1.alterar_valor(5.5)
bomba1.alterar_combustivel()
bomba1.abastecer_por_valor(4.5)
bomba1.abastecer_por_litro(4.5)
bomba1.alterar_quantidade_combustivel()