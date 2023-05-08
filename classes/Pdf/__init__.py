import requests

class Pdf():
    def __init__(self,y,title):
        self.pdfLink = y
        self.pdfTitle = title
        self.pdfDownload()
    def pdfDownload(self):
        response = requests.get(''+str(self.pdfLink))

        if response.status_code == 200:
            print('Baixando pdf')
            with open('./classes/pdfs/{}.pdf'.format(self.pdfTitle), 'wb') as f:
                f.write(response.content)
                f.close()
        else:
            print('Erro ao solicitar o arquivo PDF')

