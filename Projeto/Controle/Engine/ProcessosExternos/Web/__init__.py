import time
from Projeto.Controle.Engine.ProcessosExternos.Web.Driver import Driver





class Web():
    def __init__(self):
        print('iniciando driver')
        self.driver = Driver()

    def getLinksAbertos(self):
        pass


    def openLink(self,link):
        self.driver.open("{}".format(link))
        time.sleep(5)


    def setTitle(self,title):
        pass

    def clickElementoPorComando(self,comand):

        if 'id' in comand:
            self.driver.clickFromXpath(comand)
            return 'xpath'
        elif '/html' in comand:
            self.driver.clickFromXpath(comand)
            return 'xpath'
        elif 'content' in comand:
            self.driver.clickFromCssSelector(comand)
            return 'css_selector'
        elif 'pdfDownloadLinkUrl' in comand:
            return self.driver.getListLink()
        elif 'finishWeb' in comand:
            self.driver.quit()
            return 'finishWeb'


