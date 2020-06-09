class CaminhaoEletrico():

    def informacoes(self):
        print("Esse veículo é um caminhão, e tem motorização elétrica")

class CaminhaoHibrido():

    def informacoes(self):
        print("Esse veículo é um caminhão, e tem motorização híbrida")

class CaminhaoCombustao():

    def informacoes(self):
        print("Esse veículo é um caminhão, e tem motorização de combustão")

class AutomovelEletrico():

    def informacoes(self):
        print("Esse veículo é um automóvel, e tem motorização elétrica")

class AutomovelHibrido():

    def informacoes(self):
        print("Esse veículo é um automóvel, e tem motorização híbrida")

class AutomovelCombustao():

    def informacoes(self):
        print("Esse veículo é um automóvel, e tem motorização de combustão")


def Factory(objeto):

    veiculos = {
        "CaminhaoEletrico"   : CaminhaoEletrico,
        "CaminhaoHibrido"    : CaminhaoHibrido,
        "CaminhaoCombustao"  : CaminhaoCombustao,
        "AutomovelEletrico"  : AutomovelEletrico,
        "AutomovelHibrido"   : AutomovelHibrido,
        "AutomovelCombustao" : AutomovelCombustao
    }

    return veiculos[objeto]()



#Exemplos da corretude da implementação

caminhao_eletrico = Factory("CaminhaoEletrico")
caminhao_eletrico.informacoes()

caminhao_hibrido = Factory("CaminhaoHibrido")
caminhao_hibrido.informacoes()

caminhao_combustao = Factory("CaminhaoCombustao")
caminhao_combustao.informacoes()


automovel_eletrico = Factory("AutomovelEletrico")
automovel_eletrico.informacoes()

automovel_hibrido = Factory("AutomovelHibrido")
automovel_hibrido.informacoes()

automovel_combustao = Factory("AutomovelCombustao")
automovel_combustao.informacoes()