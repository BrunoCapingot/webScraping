from Projeto.Controle.Engine.ProcessosInternos.Arquivo import Arquivo

class ProcessosInternos():
    def __init__(self):
        self.defineArquivo = Arquivo()

    def construirArquivo(self):
        self.defineArquivo.defineCsv()
