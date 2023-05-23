import time

from Projeto.Controle.Engine.ProcessosExternos.Web.Driver import Driver



class Web():
    def __init__(self):
        print('iniciando driver')
        self.driver = Driver()

    def getLinksAbertos(self):
        pass


    def openLink(self,link):
        self.driver.driverOpen("{}".format(link))
        time.sleep(50)


    def setTitle(self,title):
        pass
    def getElementoPorComando(self):
        pass

