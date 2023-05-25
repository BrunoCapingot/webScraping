import requests

class Pdf():
    def __init__(self):
        self.pdfTitle = 'teste'
        self.pdfLink = None

    def setTituloPdf(self,title):
        self.pdfTitle = title

    def setPdfLink(self,link):
        self.pdfLink = link

    def pdfDownload(self,link):
        self.pdfLink = link
        response = requests.get('' + str(self.pdfLink))
        if response.status_code == 200:
            print('Baixando pdf')
            with open('.\{}.pdf'.format(self.pdfTitle), 'wb') as f:
                f.write(response.content)
                f.close()
        else:
            print('Erro ao solicitar o arquivo PDF')

