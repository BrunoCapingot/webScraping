
from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Imagem import Imagem
from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Escrita import Escrita

class Arquivo():
    def __init__(self):
        self.imagem = Imagem()
        self.escrita = Escrita()


    def defineCsv(self):
        self.escrita.extrairTexto()
        self.escrita.prepararArquivos()