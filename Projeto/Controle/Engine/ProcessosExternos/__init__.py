import time

from Projeto.Controle.Engine.ProcessosExternos.Web import Web
from Projeto.Controle.Engine.ProcessosExternos.Downloads import Downloads


class ProcessosExternos():
    def __init__(self):
        pass


    def scrapingSequencial(self,dataInput):
        self.web = Web()
        self.download = Downloads()
        time.sleep(5)
        for x in dataInput:
            self.web.openLink(x[0])
            for k in range(0,len(x[1])):
                for y in x[1][k]:
                    for z in x[1][k][y]:
                        retorno = self.web.clickElementoPorComando(z)
                        for x in retorno:
                            if '.pdf' in x:
                                self.download.iniciarDownload(x)
                        """input('aqui2')
                            if '.pdf' in x:
                                self.download.iniciarDownload(x)
                            input('aqui')
                        """
    def scrapingParalelo(self,dataInput):
            self.web = Web()
            #time.sleep(5)
            for x in dataInput:
                self.web.openLink(x[0])
                for k in range(0,len(x[1])):
                    for y in x[1][k]:
                        for z in x[1][k][y]:
                            #self.web.clickElementoPorComando(z)
                            input('esperando')



            #self.download = Downloads()


