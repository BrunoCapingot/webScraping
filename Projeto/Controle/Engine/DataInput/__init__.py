class DataInput():

    def __init__(self):
        self.item = None

        self.dicionarioPrincipal = {
            'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': {
                0: {
                    'Bacharelado em Agronomia': [

                        '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[1]/div[1]/h2/a',
                        '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div[1]/ul[2]/li[4]/strong/a',
                        'pdfDownloadLinkUrl',
                        'finishWeb',
                    ]},
                1: {
                    'Bacharelado em Ciência da Computação': [
                        '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[2]/div[1]/h2/a',
                        '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div[1]/ul[2]/li[2]/strong/a',
                        'pdfDownloadLinkUrl',
                        'finishWeb',
                    ]},
                2: {
                    'Bacharelado em Química Industrial': [
                        '//*[@id="adminForm"]/div[2]/div[4]/div[1]/h2/a',
                        '//*[@id="content-section"]/div/div[1]/ul[2]/li[4]/strong/a',
                        'pdfDownloadLinkUrl',
                        'finishWeb',
                    ]},
                3: {
                    'Bacharelado em Zootecnia': [
                        '//*[@id="adminForm"]/div[2]/div[4]/div[1]/h2/a',
                        '//*[@id="content-section"]/div/div[1]/ul[2]/li[4]/strong/a',
                        'pdfDownloadLinkUrl',
                        'finishWeb',
                    ]},
                4: {
                    'Licenciatura em Pedagogia': [
                        '//*[@id="adminForm"]/div[2]/div[5]/div[1]/h2/a',
                        '//*[@id="content-section"]/div/div[1]/p[12]/strong/a',
                        'pdfDownloadLinkUrl',
                        'finishWeb',
                    ]},
                5: {
                    'Licenciatura em Química': [
                        '//*[@id="adminForm"]/div[2]/div[7]/div[1]/h2/a',
                        '//*[@id="content-section"]/div/div[1]/ul[2]/li[3]/strong/a',
                        'pdfDownloadLinkUrl',
                        'finishWeb',
                    ]},
                6: {
                    'Tecnologia em Alimentos': [
                        '//*[@id="adminForm"]/div[2]/div[8]/div[1]/h2/a',
                        '//*[@id="content-section"]/div/div[1]/ul[2]/li[3]/strong/a',
                        'pdfDownloadLinkUrl',
                        'finishWeb',
                    ]},
                7: {
                    'Tecnologia em Sistemas para Internet': [
                        '//*[@id="adminForm"]/div[2]/div[8]/div[1]/h2/a',
                        '//*[@id="content-section"]/div/div[1]/ul[2]/li[3]/strong/a',
                        'pdfDownloadLinkUrl',
                        'finishWeb',
                    ]},
            }
        }

    def getData(self):
        return self.dicionarioPrincipal.items()

    def definePosicao(self):
        pass

    def preencheDicionario(self):
        pass
