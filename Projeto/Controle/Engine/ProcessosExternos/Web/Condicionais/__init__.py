from Projeto.Controle.Engine.ProcessosExternos.Web.Condicionais.Iguais import Iguais
from Projeto.Controle.Engine.ProcessosExternos.Web.Condicionais.NaoIguais import NaoIguais
from Projeto.Controle.Engine.ProcessosExternos.Web.Condicionais.Diferentes import Diferentes
from Projeto.Controle.Engine.ProcessosExternos.Web.Condicionais.Presenca import Presenca


class Condicionais():
    def __init__(self, dadoUm, dadoDois):
        self.igual = Iguais()
        self.diferente = Diferentes()
        self.naoIgual = NaoIguais()
        self.Presenca = Presenca()

        self.dadoOne = dadoUm
        self.dadoTwo = dadoDois

    def verfIgual(self):
        return self.igual.verifica(self.dadoOne, self.dadoTwo)

    def verfNaoIgual(self):
        return self.naoIgual.verifica(self.dadoOne, self.dadoTwo)

    def verfDiferente(self):
        return self.diferente.verifica(self.dadoOne, self.dadoTwo)

    def verfPresenca(self):
        return self.Presenca.verifica(self.dadoOne, self.dadoTwo)
