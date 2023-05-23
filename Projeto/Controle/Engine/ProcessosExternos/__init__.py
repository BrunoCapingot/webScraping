import time

from Projeto.Controle.Engine.ProcessosExternos.Web import Web
from Projeto.Controle.Engine.ProcessosExternos.Downloads import Downloads


class ProcessosExternos():
    def __init__(self):
        pass


    def scraping(self,dataInput):
        self.web = Web()

        time.sleep(5)
        for x in dataInput:
            self.web.openLink(x[0])
            time.sleep(5)

            for k in range(0,len(x[1])):
                self.web.openLink(x[1][k])
                print(x[1][k])
        #self.download = Downloads()


