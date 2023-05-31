from Projeto.Controle.Engine.ProcessosInternos import ProcessosInternos
from Projeto.Controle.Engine.ProcessosExternos import ProcessosExternos
from Projeto.Controle.Engine.DataInput import DataInput




class Engine():
    def __init__(self):
        self.dataInput = DataInput()
        self.processosInternos = ProcessosInternos()
        self.processosExternos = ProcessosExternos(self.dataInput.getData())

    def varreduraWeb(self):

        self.processosExternos.scrapingVelho()
        self.processosInternos.construirArquivo()

    def processarObjetivos(self):
        pass