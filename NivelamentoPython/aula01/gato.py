from animal import Animal, Animal_2;
from interface_animal import InterfaceAnimal;

class Gato:
    def __init__(self, idade, cor, nome):
        self.nome = nome
        self.idade = idade
        self.cor = cor
    
    def miar(self):
        return "miau"


class Gato(Animal_2, InterfaceAnimal):
    def __init__(self, idade, cor, nome, qtd_bolinhas):
        super().__init__(idade, cor, nome)
        self.qtd_bolinhas = qtd_bolinhas
        
    @property
    def qtd_bolinhas(self):
        return self.qtd_bolinhas

    def fazer_barulho(self):
        return "miau"

    def brincar(self):
        return "esta brincando no quintal!"