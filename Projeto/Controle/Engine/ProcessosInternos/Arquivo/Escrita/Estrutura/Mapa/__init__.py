class Mapa:
    def __init__(self):
        self._estruturaPrincipal = None

    def get_estruturaPrincipal(self):
        return self._estruturaPrincipal

    def setEstruturaPrincipal(self, mapaCondicional):
        self._estruturaPrincipal = mapaCondicional

    def getCamadaDois(self, referencia_zero, referencia_um):
        for c in self._estruturaPrincipal.keys():
            if c == referencia_zero:
                camada_zero = self._estruturaPrincipal.get(c)
                for d in camada_zero.keys():
                    if d == referencia_um:
                        return camada_zero.get(d)[0]

    def getCamadaUm(self, referencia_zero):
        for c in self._estruturaPrincipal:
            if c == referencia_zero:
                return self._estruturaPrincipal.get(referencia_zero)
