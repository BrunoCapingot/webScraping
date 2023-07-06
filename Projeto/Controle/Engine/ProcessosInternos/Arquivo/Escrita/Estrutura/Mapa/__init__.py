class Mapa:
    def __init__(self):
        self._mapa_arquivos = None
        self._estruturaPrincipal = dict()
        self._camadaZero = None
        self._camadaUm = None
        self._camadaDois = None

    def getCondicional(self):
        return self._mapa_arquivos

    def setEstrutura(self, condicao):
        if condicao == 'extrairTexto':
            self._mapa_arquivos = {
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
            self._mapa_arquivos = {'BachareladoemAgronomia.txt': [
                ['-', 'BIBLIOGRAFIA BÁSICA', 'EMENTA', 'BIBLIOGRAFIA COMPLEMENTAR']
            ]}
    def get_estruturaPrincipal(self):
        return self._estruturaPrincipal

    def get_camadaZero(self):
        return self._camadaZero

    def get_camadaUm(self):
        return self._camadaUm

    def get_camadaDois(self):
        return self._camadaDois

    def setArquivoEndereco(self, camadaZero):
        self._camadaZero = camadaZero

    def setArquivoVerificacao(self, camadaUm):
        self._camadaUm = camadaUm

    def setArquivoCondicoes(self, camadaDois):
        self._camadaDois = camadaDois
    def estruturalInicial(self):
        self._estruturaPrincipal = dict()

    def adcionarElementos(self):
        print(self._camadaZero)
        print(self._camadaUm)
        print(self._camadaDois)
        print(self._mapa_arquivos)
        input('calma')
