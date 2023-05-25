from Projeto.Controle.Engine.ProcessosExternos.Downloads.Pdf import Pdf

class Downloads():
    def __init__(self):
        self.pdf = Pdf()

    def iniciarDownload(self,link):
        self.pdf.pdfDownload(link)
