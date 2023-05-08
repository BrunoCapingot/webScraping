from classes.Web import Web
from classes.Os import Os
import concurrent.futures








class Controle():
    def __init__(self):
        self.dicionarioPrincipal = {
            'BachareladoAgronomia': {'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': [

                '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[1]/div[1]/h2/a',
                '//*[@id="content-section"]/div/div[1]/ul[2]/li[4]/strong/a',
                'pdfDownloadLinkUrl',
                'finishWeb',
            ]},
            'BachareladoCiênciaComputação': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': [
                    '//*[@id="adminForm"]/div[2]/div[2]/div[1]/h2/a',
                    '//*[@id="content-section"]/div/div[1]/ul[2]/li[2]/strong/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb',
                ]},
            'BachareladoZootecnia': {'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': [
                '//*[@id="adminForm"]/div[2]/div[4]/div[1]/h2/a',
                '//*[@id="content-section"]/div/div[1]/ul[2]/li[4]/strong/a',
                'pdfDownloadLinkUrl',
                'finishWeb',
            ]},
            'LicenciaturaPedagogia': {'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': [
                '//*[@id="adminForm"]/div[2]/div[5]/div[1]/h2/a',
                '//*[@id="content-section"]/div/div[1]/p[12]/strong/a',
                'pdfDownloadLinkUrl',
                'finishWeb',
            ]},
            'TecnologiaemAlimentos': {'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': [
                '//*[@id="adminForm"]/div[2]/div[7]/div[1]/h2/a',
                '//*[@id="content-section"]/div/div[1]/ul[2]/li[3]/strong/a',
                'pdfDownloadLinkUrl',
                'finishWeb',
            ]},
            'TecnologiaemSistemasparaInternet': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': [
                    '//*[@id="adminForm"]/div[2]/div[8]/div[1]/h2/a',
                    '//*[@id="content-section"]/div/div[1]/ul[2]/li[3]/strong/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb',
                ]}
        }
        self.execApp()



    def execApp(self):
        for x in self.dicionarioPrincipal.keys():
            print('Etapa: ' + x + ' iniciada com sucesso')
            print(x)
            web = Web(self.dicionarioPrincipal.get(x), x)
            web.Scraping()
            print('Etapa: ' + x + ' finalizada com sucesso')
        #os = Os("./classes/pdfs")
        #os.clearDir()

    def execParalelApp(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            for x in self.dicionarioPrincipal.keys():
                print('Etapa: ' + x + ' iniciada com sucesso')
                web = Web(self.dicionarioPrincipal.get(x), x)
                executor.submit(web.Scraping)
                print('Etapa: ' + x + ' adicionada à lista de tarefas')

            print('Aguardando a conclusão do scraping...')


if __name__ == '__main__':
    ctrl = Controle()
    print('SistemaFinalizado')