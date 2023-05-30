from Projeto.Controle.Engine import Engine

class Controle():
    def __init__(self):
        self.engine = Engine()
        self.execEngine()
    def execEngine(self):
        self.engine.varreduraWeb()

    def execParalelEngine(self):
        pass

Controle()
