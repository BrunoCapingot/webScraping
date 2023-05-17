import time

from ClassesControle.Web import Web
from ClassesControle.Os import Os
from ClassesControle.Pdf import Pdf


class Engine():
    def __init__(self):
        self.web = Web()
        self.pdf = Pdf()
        self.os = Os()
        self.dicionarioPrincipal = {
            'Bacharelado em Agronomia': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': [

                    '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[1]/div[1]/h2/a',
                    '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div[1]/ul[2]/li[4]/strong/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb',
                ]},
            'Bacharelado em Ciência da Computação': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': [
                    '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[2]/div[1]/h2/a',
                    '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div[1]/ul[2]/li[2]/strong/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb',
                ]},
            'Bacharelado em Química Industrial': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': [
                    '//*[@id="adminForm"]/div[2]/div[4]/div[1]/h2/a',
                    '//*[@id="content-section"]/div/div[1]/ul[2]/li[4]/strong/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb',
                ]},
            'Bacharelado em Zootecnia': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': [
                    '//*[@id="adminForm"]/div[2]/div[4]/div[1]/h2/a',
                    '//*[@id="content-section"]/div/div[1]/ul[2]/li[4]/strong/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb',
                ]},
            'Licenciatura em Pedagogia': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': [
                    '//*[@id="adminForm"]/div[2]/div[5]/div[1]/h2/a',
                    '//*[@id="content-section"]/div/div[1]/p[12]/strong/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb',
                ]},
            'Licenciatura em Química': {'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': [
                '//*[@id="adminForm"]/div[2]/div[7]/div[1]/h2/a',
                '//*[@id="content-section"]/div/div[1]/ul[2]/li[3]/strong/a',
                'pdfDownloadLinkUrl',
                'finishWeb',
            ]},
            'Tecnologia em Alimentos': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': [
                    '//*[@id="adminForm"]/div[2]/div[8]/div[1]/h2/a',
                    '//*[@id="content-section"]/div/div[1]/ul[2]/li[3]/strong/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb',
                ]},
            'Tecnologia em Sistemas para Internet': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': [
                    '//*[@id="adminForm"]/div[2]/div[8]/div[1]/h2/a',
                    '//*[@id="content-section"]/div/div[1]/ul[2]/li[3]/strong/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb',
                ]},

        }

    def buscaPorTipo(self):
        for x in self.dicionarioPrincipal.values():
            for k in x.keys():
                self.web.driverOpen(k)
                time.sleep(5)
                for i in x.get(k):
                    print(i)

                    if i != 'pdfDownloadLinkUrl' and 'finishWeb':
                        self.web.defTypeElement(i)
                        time.sleep(5)
                    elif i != 'finishWeb':
                        self.pdf.setTituloPdf("pdfJoaozinhoPdf")
                        self.pdf.setPdfLink(self.web.defTypeElement(i))
                        self.pdf.pdfDownload()
                    elif i == 'finishWeb':
                        self.web.driverClose()

    def buscaPorTexto(self):
        self.web.driverOpen("https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html")


    def defTypeCommand(self):
        pass
