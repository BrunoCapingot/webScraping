import time
from Projeto.Controle.Engine.ProcessosExternos.Web import Web
from Projeto.Controle.Engine.ProcessosExternos.Download import Downloads


class ProcessosExternos():
    def __init__(self, dataInput):
        self.dataInput = dataInput

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
