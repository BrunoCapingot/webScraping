from .Os import Os
from .Imagem import Imagem
from .Escrita import Escrita

class Arquivo():
    def __init__(self):
        self.imagem = Imagem()
        self.escrita = Escrita()


    def defineCsv(self):
        #self.imagem.extractPdfToImage()
        self.escrita.imageToText()