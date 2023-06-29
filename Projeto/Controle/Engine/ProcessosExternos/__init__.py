import time
from Projeto.Controle.Engine.ProcessosExternos.Web import Web
from Projeto.Controle.Engine.ProcessosExternos.Download import Downloads


class ProcessosExternos():
    def __init__(self, dataInput):
        self.web = None
        self.dataInput = dataInput
        self.download = None

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
                print('Abrindo link: ' + list[0])
                for comando in list[1][k][nomeAssunto]:
                    print('Ação em: {} indentificando -> {}'.format(nomeAssunto, comando))
                    retorno = self.web.clickElementoPorComando(comando)
                    time.sleep(3)
                    for pdfLink in retorno:
                        if '.pdf' in pdfLink:
                            self.download = Downloads()
                            #print('Iniciando download do PDF: {}'.format(pdfLink))
                            self.download.iniciarDownload(pdfLink, nomeAssunto)
