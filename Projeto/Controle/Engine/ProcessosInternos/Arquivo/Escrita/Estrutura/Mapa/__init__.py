class Mapa:
    def __init__(self):
        self.mapa_arquivos = None

    def getCondicional(self):
        return self.mapa_arquivos

    def setEstrutura(self, condicao):
        if condicao == 'extrairTexto':
            self.mapa_arquivos = {
                'BachareladoemAgronomia.pdf': ['BachareladoemAgronomia.pdf', 40, 106],
                'BachareladoemCienciadaComputacao.pdf': ['BachareladoemCienciadaComputacao.pdf', [[9, 13], [51, 88]]],
                'BachareladoemQuimicaIndustrial.pdf': ['BachareladoemQuimicaIndustrial.pdf', 49, 60],
                'BachareladoemZootecnia.pdf': ['BachareladoemZootecnia.pdf', 50, 60],
                'LicenciaturaemPedagogia.pdf': ['LicenciaturaemPedagogia.pdf', 34, 70],
                'LicenciaturaemQuimica.pdf': ['LicenciaturaemQuimica.pdf', 37, 67],
                'TecnologiaemAlimentos.pdf': ['TecnologiaemAlimentos.pdf', 49, 104],
                'TecnologiaemSistemasparaInternet.pdf': ['TecnologiaemSistemasparaInternet.pdf', 49, 90]
            }
        elif condicao == 'prepararArquivo':
            self.mapa_arquivos = mapaCondicional = {'BachareladoemAgronomia.txt': [
                ['-', 'BIBLIOGRAFIA BÁSICA', 'EMENTA', 'BIBLIOGRAFIA COMPLEMENTAR']
            ]}
