import requests

class Pdf():
    def __init__(self):
        self.pdfTitle = None
        self.pdfLink = None

    def setTitulo(self,title):
        self.pdfTitle = title

    def setLink(self,link):
        self.pdfLink = link

    def download(self):
        response = requests.get('' + str(self.pdfLink))
        if response.status_code == 200:
            print('Baixando pdf')
            with open('.\Download\matrizes_curriculares\{}.pdf'.format(self.pdfTitle), 'wb') as f:
                f.write(response.content)
                f.close()
        else:
            print('Erro ao solicitar o arquivo PDF')

