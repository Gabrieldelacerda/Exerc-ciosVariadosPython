class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au au"

class Gato(Animal):
    def falar(self):
        return "Miau"

class Passaro(Animal):
    def falar(self):
        return "Piu piu"

def interagir(animal):
    print(animal.falar())

cachorro = Cachorro()
gato = Gato()
passaro = Passaro()

interagir(cachorro)
interagir(gato)
interagir(passaro)