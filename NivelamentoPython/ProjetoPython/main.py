from cachorro import Cachorro, Cachorro_2, Cachorro_3;
from gato import Gato;
from dono import Dono

#classe
cachorro = Cachorro()
cachorro.name = "tata"
print(cachorro.nome)
print(cachorro.idade)
print(cachorro.cor)
print(cachorro.latir())

#constructor
cachorro_2 = Cachorro_2(10, "Branco", "tete")
print(cachorro_2.nome)
print(cachorro_2.idade)
print(cachorro_2.cor)

gato = Gato(1, "marrom", "mimi")
print(gato.nome)
print(gato.miar())

#herança
cachorro_3 = Cachorro_3(10, "Branco", "tete", 4)
print(cachorro_3.nome)
print(cachorro_3.idade)
print(cachorro_3.cor)
print(cachorro_3.qtd_bolinhas)#estamos acessando a property

#acessando um objeto dentro de uma classe atrelada a uma outra classe
cachorro_4 = Cachorro_3(10, "Branco", "tete", 4, dono=Dono('jose'))
print(cachorro_3.nome)
print(cachorro_3.idade)
print(cachorro_3.cor)
print(cachorro_3.qtd_bolinhas)#estamos acessando a property
print(cachorro.dono.nome)


#caso eu queira acessar um encapsulamento privado
# usa-se nome da classe seguida do atributo, _Cachorro__qtd_bolinhas (privado)
# um protected 