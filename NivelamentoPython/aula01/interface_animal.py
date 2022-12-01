import abc

class InterfaceAnimal(abc.ABC):
    @abc.abstractmethod
    def fazer_barulho(self):
        pass #sem comportamento
    
    @abc.abstractmethod
    def brincar(self):
        pass
    
#similar ao typeScript, obrigatório o atributo dentro das classe