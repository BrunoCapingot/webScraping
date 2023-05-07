import requests

class Pdf():
    def __init__(self,y):
        self.pdfLink = y
        self.pdfDownload()
    def pdfDownload(self):
        response = requests.get(''+str(self.pdfLink))

        if response.status_code == 200:
            print('Baixando pdf')
            with open('./pdfs/pdf_matriz_curricular_00.pdf', 'wb') as f:
                f.write(response.content)
                f.close()
        else:
            print('Erro ao solicitar o arquivo PDF')

