class Veiculo:
    def __init__(self, marca, modelo, rodas):
        self.marca = marca
        self.modelo = modelo
        self.rodas = rodas
        self.__velocidade = 0

    def acelerar(self, valor):
        self.__velocidade += valor

    def frear(self, valor):
        self.__velocidade -= valor
        if self.__velocidade < 0:
            self.__velocidade = 0

    def get_velocidade(self):
        return self.__velocidade


class Carro(Veiculo):
    def __init__(self, marca, modelo, rodas, potencia):
        super().__init__(marca, modelo, rodas)
        self.potencia = potencia

    def imprimir_informacoes(self):
        print(
            f'Marca: {self.marca}\nModelo: {self.modelo}\nRodas:{self.rodas}')
        print(f'Potencia:{self.potencia}')


class Moto(Veiculo):
    def __init__(self, marca, modelo, rodas, partida_eletrica):
        super().__init__(marca, modelo, rodas)
        self.partida_eletrica = partida_eletrica

    def imprimir_informacoes(self):
        print(
            f'Marca: {self.marca}\nModelo: {self.modelo}\nRodas:{self.rodas}')
        print(f'Partida Eletrica:{self.partida_eletrica}')


class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, rodas, marchas, bagageiro):
        super().__init__(marca, modelo, rodas)
        self.bagageiro = bagageiro
        self.marchas = marchas

    def imprimir_informacoes(self):
        print(
            f'Marca: {self.marca}\nModelo: {self.modelo}\nRodas:{self.rodas}')
        print(f'Marchas:{self.marchas}\nBagageiro:{self.bagageiro}')


carro = Carro("Ford", "Ka", 4, 85.0)
moto = Moto("Honda", "Biz", 2, True)
bike = Bicicleta("Caloi", "Elite", 2, 18, True)

carro.acelerar(30)
carro.frear(10)
moto.acelerar(100)
moto.frear(20)
bike.acelerar(20)
bike.frear(5)

carro.imprimir_informacoes()   # imprime os valores carro
bike.imprimir_informacoes()    # imprime os valores bicicleta
moto.imprimir_informacoes()    # imprime os valores moto

# testar a velocidade atual
print("A Velocidade atual do Carro é:", carro.get_velocidade())       # 20
print("A Velocidade atual da Mot é:", moto.get_velocidade())         # 80
print("A Velocidade atual da Bicicleta é:", bike.get_velocidade())    # 15