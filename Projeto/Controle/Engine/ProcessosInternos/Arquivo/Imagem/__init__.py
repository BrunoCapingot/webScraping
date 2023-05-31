from pdf2image import convert_from_path

class Imagem():
    def __init__(self):
        self.pdfName = None

    #agronomia
    #cienciasDaComputação
    #tecnologiaEmAlimentos
    #tecnologiaEmSistemasDaInternet


    def extractPdfToImage(self):
        listPath = [r'C:/Users/CPGT/Desktop/webScraping/Projeto/Controle/Download/matrizes_curriculares/BachareladoemAgronomia.pdf',
                    r'C:/Users/CPGT/Desktop/webScraping/Projeto/Controle/Download/matrizes_curriculares/BachareladoemCienciadaComputacao.pdf',
                    r'C:/Users/CPGT/Desktop/webScraping/Projeto/Controle/Download/matrizes_curriculares/TecnologiaemAlimentos.pdf',
                    r'C:/Users/CPGT/Desktop/webScraping/Projeto/Controle/Download/matrizes_curriculares/TecnologiaemSistemasparaInternet.pdf'
                    ]
        for pdf_path in listPath:
            images = convert_from_path(pdf_path)
            for i, image in enumerate(images):
                image.save(f'{pdf_path.split("/")[-1]}_pagina_{i + 1}.jpg', 'JPEG')


