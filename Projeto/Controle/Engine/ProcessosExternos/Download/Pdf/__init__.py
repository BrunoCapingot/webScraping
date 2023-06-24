import requests
from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Os import Os


class Pdf:
    def __init__(self):
        self.pdfTitle = None
        self.pdfLink = None
        self.os = Os()

    def setTitulo(self, title):
        self.pdfTitle = title

    def setLink(self, link):
        self.pdfLink = link

    def download(self):
        print('Baixando o link: ' + str(self.pdfLink))
        response = requests.get('' + str(self.pdfLink))
        # response = requests.get('https://www.ifgoiano.edu.br/home/images/MHOS/Doc_cursos/PPC_Pedagogia_Novo_ConselhoSuperior.pdf')
        if response.status_code == 200:
            print('Baixando pdf')
            self.os.setHomePonteiro()
            self.os.setDiretorio('\webScraping\Projeto\Controle\Download\projetoPedagogicoCurso\{}.pdf'.format(self.pdfTitle))
            with open(r'{}'.format(self.os.getPonteiro()), 'wb') as f:
                f.write(response.content)
                f.close()
        else:
            print('Erro ao solicitar o arquivo PDF')
