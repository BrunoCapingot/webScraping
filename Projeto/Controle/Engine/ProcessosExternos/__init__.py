import time
import concurrent.futures
from Projeto.Controle.Engine.ProcessosExternos.Web import Web
from Projeto.Controle.Engine.ProcessosExternos.Downloads import Downloads
from Projeto.Controle.Engine.DataInput.Estrutura import Estrutura


class ProcessosExternos():
    def __init__(self,dataInput):
        self.dataInput = dataInput
        self.indexNumerico = 0
        self.list = []
        for x in self.dataInput:
            for y in x:
                self.list.append(y)
        self.estrutura = self.list[1]

    def defineIndexNumerico(self,numero):
        self.indexNumerico = self.indexNumerico + numero
        self.estrutura = self.list[1][self.indexNumerico]
        print(self.estrutura)

        return self.estrutura

    def scrapingSequencial(self):

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


    def scrapingParalelo(self):
        est = Estrutura()
        est.setDataEstrutucture(self.dataInput)
        est.setIndexNumerico(0)
        est.setIndexString('Bacharelado em Agronomia')
        print(est.getEstrutura())
        input('esperando')

        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit()



