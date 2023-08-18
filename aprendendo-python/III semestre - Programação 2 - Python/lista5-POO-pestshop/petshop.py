class Pet:
    def __init__(self, nome, animal, raca, cor):
        self.nome = nome
        self.animal = animal
        self.raca = raca
        self.cor = cor


class Cliente:
    def __init__(self, nome, contato):
        self.nome = nome
        self.contato = contato


class Funcionario:
    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao
        

class Servico:
    def __init__(self, funcionario, cliente, pet):
        self.funcionario = funcionario
        self.cliente = cliente
        self.pet = pet

    def banho(self, servico):
        print('-'*30)
        print(f'Tipo Servico: {servico} \nPet: {self.pet.nome}')
        print(f'Cliente: {self.cliente.nome} \nFuncionario Responsável: {self.funcionario.nome}  {self.funcionario.funcao}')

    def consulta(self, ficha_medica):
        print('-'*30)
        print(f'Tipo Servico: Consulta \nPet: {self.pet.nome} Animal: {self.pet.animal} Raca: {self.pet.animal} Cor: {self.pet.cor}')
        print(f'Cliente: {self.cliente.nome} \nFuncionario Responsável: {self.funcionario.nome}  {self.funcionario.funcao}')
        print(f'Ficha médica \n{ficha_medica} \nValor Consulta: R$ 200.00.')


#principal
funcionario1 = Funcionario('José', 'Veterinário')
funcionario2 = Funcionario('José', 'Banhista')
cliente1 = Cliente('Rafael', '(77)99921-8737')
pet = Pet('Oreo', 'Gato', 'SRD','preto e branco')

#servico banho
servico1 = Servico(funcionario2, cliente1, pet)
servico1.banho('Tosa e Banho')
#servico consulta
servico1 = Servico(funcionario1, cliente1, pet)
servico1.consulta('Gato encontrado na rua; Anêmico; Plaquetas baixas; Desidratado')