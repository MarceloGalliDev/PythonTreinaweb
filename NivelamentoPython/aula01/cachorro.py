from animal import Animal

class Cachorro():
    idade = 4
    cor = "Preto"
    nome = "Toto"
    
    def latir(self):
        return "au au"

#constructor
#self é o mesmo que this do JS
#self é atribuir a váriavel dentro da nossa classe
class Cachorro_2():
    def __init__(self, idade, cor, nome):
        self.idade = idade
        self.cor = cor
        self.nome = nome
    
    def latir(self):
        return "au au"

#herança de classe
class Cachorro_3(Animal):
    def __init__(self, idade, cor, nome, qtd_bolinhas):
        super().__init__(idade, cor, nome)
        self.qtd_bolinhas = qtd_bolinhas
        
        #usado para que possamos acessar um atributo privado fora da classe
        @property
        def qtd_bolas(self):
            return self.__qtd_bolas

        #usado para que possamos alterar um atributo privado fora da classe
        @qtd_bolas.setter
        def qtd_bolas(self, qtd_bolas):
            self.__qtd_bolas = qtd_bolas
    
    def latir(self):
        return "au au"

class Cachorro_4(Animal):
    def __init__(self, idade, cor, nome, qtd_bolinhas):
        super().__init__(idade, cor, nome)
        self.qtd_bolinhas = qtd_bolinhas
        
        #usado para que possamos acessar um atributo privado fora da classe
        @property
        def qtd_bolas(self):
            return self.__qtd_bolas

        #usado para que possamos alterar um atributo privado fora da classe
        @qtd_bolas.setter
        def qtd_bolas(self, qtd_bolas):
            self.__qtd_bolas = qtd_bolas
    
    def fazer_barulho(self):
        return "au au"