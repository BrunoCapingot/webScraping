from Projeto.Controle.Engine.ProcessosInternos.Arquivo import Arquivo

class ProcessosInternos():
    def __init__(self):
        self.arquivo = Arquivo()

    def construirArquivo(self):
        self.arquivo.setDiretoriosNecessarios()
        self.arquivo.defineCsv()
