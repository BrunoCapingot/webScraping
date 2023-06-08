import time
from Projeto.Controle.Engine.ProcessosExternos.Web import Web
from Projeto.Controle.Engine.ProcessosExternos.Downloads import Downloads
from Projeto.Controle.Engine.DataInput.Estrutura import Estrutura


class ProcessosExternos():
    def __init__(self,dataInput):
        self.est = Estrutura()
        self.dataInput = dataInput
        self.indexNumerico = 0
        self.list = []
        for x in self.dataInput:
            for y in x:
                self.list.append(y)
        self.estrutura = self.list[1]


    def indexNumericoMais(self,numero):
        self.indexNumerico = self.indexNumerico + numero

    def defineIndexNumerico(self,numero):
        self.indexNumerico = numero
        self.estrutura = self.list[1][self.indexNumerico]
        return self.estrutura

    def scrapingVelho(self):

        time.sleep(5)
        list2 = []
        for k in self.dataInput:
            list2.append(k)
        list = list2[0]
        for k in range(0, len(list[1])):
            for nomeAssunto in list[1][k]:
                self.web = Web()
                self.web.openLink(list[0])
                for comando in list[1][k][nomeAssunto]:
                    retorno = self.web.clickElementoPorComando(comando)
                    time.sleep(3)
                    for pdfLink in retorno:
                        if '.pdf' in pdfLink:
                            self.download = Downloads()
                            cond = True
                            self.download.iniciarDownload(pdfLink, nomeAssunto)




    def scrapingSequencial(self):
        #self.web = Web()

        #self.download = Downloads()
        #self.web.openLink('https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html')
        self.est.setDataEstrutucture(self.dataInput)
        self.est.setIndexNumerico(self.indexNumerico)
        self.indexNumericoMais(self.indexNumerico + 1)
        for x in self.est.getEstruturaNumeric():
            self.est.setIndexString(x)
        #print(self.est.getEstructureComand())
        for comand in self.est.getEstructureComand():
            print(comand)
        #    links = self.web.clickElementoPorComando(comand)
        #    for x in links:
        #        if '.pdf' in x:
        #            self.download.iniciarDownload(x,self.est.getIndexString())
        #        time.sleep(3)










