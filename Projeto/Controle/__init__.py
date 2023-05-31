from Projeto.Controle.Engine import Engine


class Controle():
    def __init__(self):
        self.engine = Engine()

    def execEngine(self):
        self.engine.varreduraWeb()
        print('uma vez')

    def execParalelEngine(self):
        #self.engine.varreduraWeb()
        print('uma vez')
