class Motorizacao:
    def mostra_motor(self):
        pass

class Eletrico(Motorizacao):
    def mostra_motor(self):
        print("tem motorização elétrica")

class Hibrido(Motorizacao):
    def mostra_motor(self):
        print("tem motorização híbrida")

class Combustao(Motorizacao):
    def mostra_motor(self):
        print("tem motorização de combustão")


class Veiculo:
    def __init__(self,motorizacao):
        self.motorizacao = motorizacao

    def informacoes(self):
        pass

class Caminhao(Veiculo):
    def __init__(self,motorizacao):
        super().__init__(motorizacao)

    def informacoes(self):
        print("Esse veículo é um caminhão, e ",end="")
        self.motorizacao.mostra_motor()

class Automovel(Veiculo):
    def __init__(self,motorizacao):
        super().__init__(motorizacao)

    def informacoes(self):
        print("Esse veículo é um automóvel, e ",end="")
        self.motorizacao.mostra_motor()



#Exemplos da corretude da implementação

caminhao_eletrico = Caminhao(Eletrico())
caminhao_eletrico.informacoes()

caminhao_hibrido = Caminhao(Hibrido())
caminhao_hibrido.informacoes()

caminhao_combustao = Caminhao(Combustao())
caminhao_combustao.informacoes()


automovel_eletrico = Automovel(Eletrico())
automovel_eletrico.informacoes()

automovel_hibrido = Automovel(Hibrido())
automovel_hibrido.informacoes()

automovel_combustao = Automovel(Combustao())
automovel_combustao.informacoes()