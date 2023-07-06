from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Imagem import Imagem
from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Escrita import Escrita
from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Os import Os


class Arquivo():
    def __init__(self):
        self.imagem = Imagem()
        self.escrita = Escrita()
        self.os = Os()
        self.diretorios_fracionados = None

    def defineCsv(self):
        self.escrita.prepararCondicionais(self.diretorios_fracionados)
        # self.escrita.extrairTexto()
        self.escrita.prepararArquivos()

    def setDiretoriosNecessarios(self):
        self.diretorios_fracionados = {'enderecos': {'csv': r'\webScraping\Projeto\Controle\Download\Csv',
                                                     'imagem': r'\webScraping\Projeto\Controle\Download\Imagens',
                                                     'texto': r'\webScraping\Projeto\Controle\Download\Textos',
                                                     'projetoPedagogico': r'\webScraping\Projeto\Controle\Download'
                                                                          r'\ProjetoPedagogicoCurso'}
                                       }
