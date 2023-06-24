import time
from Projeto.Controle.Engine.ProcessosInternos import ProcessosInternos
from Projeto.Controle.Engine.ProcessosExternos import ProcessosExternos
from Projeto.Controle.Engine.DataInput import DataInput


class Engine:
    def __init__(self):
        self.dataInput = DataInput()
        self.processosInternos = ProcessosInternos()
        self.processosExternos = ProcessosExternos(self.dataInput.getData())

    def varreduraWeb(self):
        start_time = time.time()
        print("----Início da execução----", time.localtime())
        self.processosExternos.scrapingVelho()
        self.processosInternos.construirArquivo()
        print("Fim da execução:", time.localtime())
        end_time = time.time()
        execution_time = end_time - start_time
        print("----Tempo de execução----")
        print("Milissegundos: {:.2f} ms".format(execution_time * 1000))
        print("Segundos: {:.2f} s".format(execution_time))
        print("Minutos: {:.2f} min".format(execution_time / 60))
        print("Horas: {:.2f} h".format(execution_time / 3600))
        print("Dias: {:.2f} d".format(execution_time / 86400))
        print("----Algoritimo Finalizado----")
    def processarObjetivos(self):
        pass
