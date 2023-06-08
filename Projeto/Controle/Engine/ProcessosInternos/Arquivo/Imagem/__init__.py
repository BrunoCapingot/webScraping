from pdf2image import convert_from_path
import os
class Imagem():
    def __init__(self):
        self.pdfName = None
        self.especificacaoImage = []

    #agronomia
    #cienciasDaComputação
    #tecnologiaEmAlimentos
    #tecnologiaEmSistemasDaInternet
    def extractPdfToImage(self):
        """listPath = [
                    r'Controle/PdfDownload/BachareladoemAgronomia.pdf',
                    r'Controle/PdfDownload/BachareladoemCienciadaComputacao.pdf',
                    r'Controle/PdfDownload/TecnologiaemAlimentos.pdf',
                    r'Controle/PdfDownload/TecnologiaemSistemasparaInternet.pdf'
                    ]
        """

        diretorio = 'PdfDownload/'
        listPath = []

        for arquivo_name in os.listdir(diretorio):
            if arquivo_name == 'BachareladoemAgronomia.pdf' or arquivo_name == 'BachareladoemCienciadaComputacao.pdf' or arquivo_name == 'TecnologiaemAlimentos.pdf' or arquivo_name == 'TecnologiaemSistemasparaInternet.pdf':
                pdf_path = os.path.join(diretorio, arquivo_name)
                self.especificacaoImage.append([arquivo_name,pdf_path.replace('/','')])
                listPath.append(pdf_path)
        for pdf_path in listPath:
            images = convert_from_path(pdf_path)
            for i, image in enumerate(images):
                image_path = os.path.join(diretorio, f'{pdf_path.split("/")[-1].replace(".pdf","")}_pagina_{i + 1}.jpg')
                image.save(image_path, 'JPEG')


    def getEspecificacaoImage(self):
        return self.especificacaoImage

