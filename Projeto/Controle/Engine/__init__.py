from Projeto.Controle.Engine.ProcessosInternos import ProcessosInternos
from Projeto.Controle.Engine.ProcessosExternos import ProcessosExternos
from Projeto.Controle.Engine.DataInput import DataInput



class Engine():
    def __init__(self):
        self.dataInput = DataInput()
        #self.processosInternos = ProcessosInternos()
        self.processosExternos = ProcessosExternos()

    def varreduraWeb(self):
        self.processosExternos.scrapingSequencial(self.dataInput.getData())

    def processarObjetivos(self):
        pass