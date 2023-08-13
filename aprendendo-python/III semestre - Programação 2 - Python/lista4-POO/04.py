'''4. Classe Carro: Implemente uma classe chamada Carro com as seguintespropriedades:
Um veículo tem um certo consumo de combustível (medido em km /litro) e uma certa quantidade de combustível no tanque;
O consumo é especificado no construtor e o nível de combustível inicialé 0;

Forneça um método andar() que simule o ato de dirigir o veículo por uma certa distância, reduzindo o 
nível de combustível no tanque de gasolina;

Forneça um método obter_gasolina(), que retorna o nível atual de combustível;

Forneça um método adicionar_gasolina(), para abastecer o tanque.
Exemplo de uso:
    meuFusca = Carro(15); # 15 quilômetros por litro de combustível. 
    meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
    meuFusca.andar(100); # anda 100 quilômetros. 
    meuFusca.obterGasolina() # Imprime o combustível que resta no tanque.'''

class Carro:
    def __init__(self, consumo_combustivel, qtd_combustivel_tanque=0):
        self.consumo_combustivel = consumo_combustivel
        self.qtd_combustivel_tanque = qtd_combustivel_tanque
    
    def andar(self, distancia_km):
        while True:
            if self.qtd_combustivel_tanque >0:
                litro_gasto = distancia_km/self.consumo_combustivel
                self.qtd_combustivel_tanque -= litro_gasto
                print(f'Qtd de combustível gasto: {litro_gasto}L.')
                break
            else:
                print('\nTanque Vazio.')
    
    def obter_gasolina(self):
        print(f'Nível atual do tanque: {self.qtd_combustivel_tanque:.2f}L.')
    
    def adicionar_gasolina(self, qtd_gasolina):
        self.qtd_combustivel_tanque =+ qtd_gasolina
        print(f'Nível atual do tanque: {self.qtd_combustivel_tanque:.2f}L.')

meuFusca = Carro(15); # 15 quilômetros por litro de combustível. 
meuFusca.adicionar_gasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100); # anda 100 quilômetros. 
meuFusca.obter_gasolina() # Imprime o combustível que resta no tanque.'''