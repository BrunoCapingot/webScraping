import time
import concurrent.futures
from Projeto.Controle.Engine.ProcessosExternos.Web import Web
from Projeto.Controle.Engine.ProcessosExternos.Downloads import Downloads


class ProcessosExternos():
    def __init__(self):
        pass

    def scrapingSequencial(self, dataInput):
        self.download = Downloads()
        time.sleep(5)
        list2 = []
        for k in dataInput:
            list2.append(k)
        list = list2[0]
        for k in range(0, len(list[1])):
            for nomeAssunto in list[1][k]:
                self.web = Web()
                print('openWeb')
                self.web.openLink(list[0])
                print('WebOpen')
                #print(list[0] + ' Chegou aqui agora')
                #print(nomeAssunto + ' Chegou aqui agora')
                for comando in list[1][k][nomeAssunto]:
                    retorno = self.web.clickElementoPorComando(comando)
                    time.sleep(3)
                    #print(comando)
                    for pdfLink in retorno:
                        if '.pdf' in pdfLink:
                            cond = True
                            #print(pdfLink)
                            self.download.iniciarDownload(pdfLink, nomeAssunto)


    def scrapingParalelo(self, dataInput):
        self.web = Web()
        self.download = Downloads()
        time.sleep(5)
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            print('Etapa: ' + x + ' iniciada com sucesso')
            executor.submit(web.Scraping)
            print('Aguardando a conclusão do scraping...')
