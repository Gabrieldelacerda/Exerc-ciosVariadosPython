class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def exibir_caracteristicas(self):
        print(f"Modelo do carro: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Ano: {self.ano}")

carro1 = Carro("Ferrari", "Vermelho", 2020)
carro2 = Carro("Ferrari", "Azul", 2001)

carro1.exibir_caracteristicas()
carro2.exibir_caracteristicas()