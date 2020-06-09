class Embalagem:
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost
class ComerAqui(Embalagem):
        cost = 0.0

class PraViagem(Embalagem):
        cost = 5.0

class Decorator(Embalagem):
    def __init__(self, embalagem):
        self.component = embalagem
    def getTotalCost(self):
        return self.component.getTotalCost() + Embalagem.getTotalCost(self)
    def getDescription(self):
        return self.component.getDescription() + " " + Embalagem.getDescription(self)

class Frango(Decorator):
    cost = 10.0
    def __init__(self, embalagem):
        Decorator.__init__(self, embalagem)
class Catupiry(Decorator):
    cost = 8.0
    def __init__(self, embalagem):
        Decorator.__init__(self, embalagem)
class Mussarela(Decorator):
    cost = 4.0
    def __init__(self, embalagem):
        Decorator.__init__(self, embalagem)
class MolhoTomate(Decorator):
    cost = 2.0
    def __init__(self, embalagem):
        Decorator.__init__(self, embalagem)
class Bacon(Decorator):
    cost = 12.0
    def __init__(self, embalagem):
        Decorator.__init__(self, embalagem)
class Cebola(Decorator):
    cost = 0.5
    def __init__(self, embalagem):
        Decorator.__init__(self, embalagem)

frango_catupiry_aqui = Frango(Catupiry(MolhoTomate(ComerAqui())))
print(frango_catupiry_aqui.getDescription()+ ": R$" + str(frango_catupiry_aqui.getTotalCost()))

bacon_mussarela_viagem = Bacon(Cebola(Mussarela(PraViagem())))
print(bacon_mussarela_viagem.getDescription()+ ": R$" + str(bacon_mussarela_viagem.getTotalCost()))

dois_queijos_viagem = Mussarela(Catupiry(MolhoTomate(PraViagem())))

print(dois_queijos_viagem.getDescription()+ ": R$" + str(dois_queijos_viagem.getTotalCost()))

