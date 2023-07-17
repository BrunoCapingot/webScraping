from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Imagem import Imagem
from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Escrita import Escrita


class Arquivo():
    def __init__(self):
        self.imagem = Imagem()
        self.escrita = Escrita()
        self.diretorios_fracionados = None

    def defineCsv(self):
        self.escrita.prepararCondicionais(self.diretorios_fracionados)
        #self.escrita.extrairTexto()
        self.escrita.prepararArquivos()

    def setDiretoriosNecessarios(self):
        self.diretorios_fracionados = {'enderecos': {'csv': [r'\webScraping\Projeto\Controle\Download\Csv'],
                                                     'imagem': [r'\webScraping\Projeto\Controle\Download\Imagens'],
                                                     'texto': [r'\webScraping\Projeto\Controle\Download\Textos'],
                                                     'projetoPedagogico': [r'\webScraping\Projeto\Controle\Download\ProjetoPedagogicoCurso']},

                                       'extrairTexto': {'BachareladoemAgronomia.pdf': ['BachareladoemAgronomia.pdf', 40, 106],
                                                        'BachareladoemCienciadaComputacao.pdf': ['BachareladoemCienciadaComputacao.pdf', [[9, 13], [51, 88]]],
                                                        'BachareladoemQuimicaIndustrial.pdf': ['BachareladoemQuimicaIndustrial.pdf', 49, 60],
                                                        'BachareladoemZootecnia.pdf': ['BachareladoemZootecnia.pdf', 50, 60],
                                                        'LicenciaturaemPedagogia.pdf': ['LicenciaturaemPedagogia.pdf', 34, 70],
                                                        'LicenciaturaemQuimica.pdf': ['LicenciaturaemQuimica.pdf', 37, 67],
                                                        'TecnologiaemAlimentos.pdf': ['TecnologiaemAlimentos.pdf', 49, 104],
                                                        'TecnologiaemSistemasparaInternet.pdf': ['TecnologiaemSistemasparaInternet.pdf', 49, 90]},

                                       'prepararArquivo': {'BachareladoemAgronomia.txt': [['-', 'BIBLIOGRAFIA BÁSICA', 'EMENTA', 'BIBLIOGRAFIA COMPLEMENTAR']],
                                                        'BachareladoemCienciadaComputacao.txt': [['-', 'BIBLIOGRAFIA BÁSICA', 'EMENTA', 'BIBLIOGRAFIA COMPLEMENTAR']],
                                                        'BachareladoemQuimicaIndustrial.txt': [['-', 'BIBLIOGRAFIA BÁSICA', 'EMENTA', 'BIBLIOGRAFIA COMPLEMENTAR']],
                                                        'BachareladoemZootecnia.txt': [['-', 'BIBLIOGRAFIA BÁSICA', 'EMENTA', 'BIBLIOGRAFIA COMPLEMENTAR']],
                                                        'LicenciaturaemPedagogia.txt': [['-', 'BIBLIOGRAFIA BÁSICA', 'EMENTA', 'BIBLIOGRAFIA COMPLEMENTAR']],
                                                        'LicenciaturaemQuimica.txt': [['-', 'BIBLIOGRAFIA BÁSICA', 'EMENTA', 'BIBLIOGRAFIA COMPLEMENTAR']],
                                                        'TecnologiaemAlimentos.txt': [['-', 'BIBLIOGRAFIA BÁSICA', 'EMENTA', 'BIBLIOGRAFIA COMPLEMENTAR']],
                                                        'TecnologiaemSistemasparaInternet.txt': [['-', 'BIBLIOGRAFIA BÁSICA', 'EMENTA', 'BIBLIOGRAFIA COMPLEMENTAR']]
                                       }
                                       }